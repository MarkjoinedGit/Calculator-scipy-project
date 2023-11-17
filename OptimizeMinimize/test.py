import pygame as pg
from OptimizeMinimize import buttons as bt
import pygame_gui
from OptimizeMinimize import MinimizeCaculator
from OptimizeMinimize import ExpressionPlotter

class MinimizeFunction:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1000, 600))
        pg.display.set_caption('Minimize function')
        self.clock = pg.time.Clock()
        self.manager = pygame_gui.UIManager((1000, 600))

        #text
        self.text_font = pg.font.Font(r'OptimizeMinimize\assets\font\montserrat\Montserrat-Light.otf',30)
        self.text_font_smaller = pg.font.Font(r'OptimizeMinimize\assets\font\montserrat\Montserrat-Light.otf',15)

        #store result
        self.result = []
        self.Result_label = self.text_font_smaller.render('Result:', True, 'white')
        self.Result_board = pygame_gui.elements.UITextBox('', relative_rect=pg.Rect((441, 63), (543, 104)), manager=self.manager, object_id='#result_board')

        self.Graph_image = ''
        self.Graph_label = self.text_font_smaller.render('Graph:', True, 'white')
        #self.Graph_board_rect = pg.Rect((441, 215), (543, 345))

        #input
        #   Expression
        self.Expression_text = self.text_font_smaller.render('Expression input:', True, 'white')
        self.Expression_rect = pg.Rect((22, 63), (313, 33))
        self.Expression_input = pygame_gui.elements.UITextEntryLine(relative_rect=self.Expression_rect, manager=self.manager, object_id='#expression_entry')
        self.expression = ''

        #   Contraint
        self.Constraint_text = self.text_font_smaller.render('Constraint input:', True, 'white')
        self.Constraint_rect = pg.Rect((22, 134), (313, 33))
        self.Constraint_input = pygame_gui.elements.UITextEntryLine(relative_rect=self.Constraint_rect, manager=self.manager, object_id='#constraint_entry')
        #Show the constraint
        self.constraints = []
        self.constraints_text = ''
        self.Constraint_label = self.text_font_smaller.render('Constraint:', True, 'white')
        self.Constraint_board = pygame_gui.elements.UITextBox('', relative_rect=pg.Rect((22, 215), (313, 202)), manager=self.manager, object_id='#constraint_board')
        # take the index input from user to remove specific constraint
        self.constraint_index = 0
        self.Index_label = self.text_font_smaller.render('Index:', True, 'white')
        self.Index_input = pygame_gui.elements.UITextEntryLine(relative_rect=pg.Rect((83, 428), (78, 42)), manager=self.manager, object_id='#index_entry')

        # buttons
        self.submit_btn = bt.Button(self.screen, self.text_font, 'Submit', 153, 36, (22, 501), False, 30, '#FF9A24', '#F3B771', '#ffffff', '#ffffff')
        self.back_btn = bt.Button(self.screen, self.text_font, 'Back', 153, 36, (22, 548), False, 30, '#FF9A24', '#F3B771', '#ffffff', '#ffffff')
        self.add_constraint_btn = bt.Button(self.screen, self.text_font_smaller, '+', 40, 33, (343, 134), False, 30, '#FF9A24', '#F3B771', '#ffffff', '#ffffff')
        self.remove_constraint_btn = bt.Button(self.screen, self.text_font_smaller, 'Remove constraint', 167, 42, (166, 428), False, 30, '#FF9A24', '#F3B771', '#ffffff', '#ffffff')
        
        #Error: display error:
        self.error_message = self.text_font_smaller.render('', True, 'red')

    def drawConstraintsBoard(self):
        instruction_text = 'Constraints must be specified as gi(x)>=0 (e.g: if constraint is x+2y>=1, you have to write x+2y-1 in constraint_input, and then press +) \n'
        constraints_text = '\n'.join(f'{i+1}. {text}' for i, text in enumerate(self.constraints))
        self.Constraint_board.html_text = instruction_text+constraints_text
        self.Constraint_board.rebuild()

    def drawComponents(self):
        # draw text
        self.screen.blit(self.Expression_text, (22, 35))
        self.screen.blit(self.Constraint_text, (22, 106))
        self.screen.blit(self.Constraint_label, (22, 187))
        self.screen.blit(self.Index_label, (22, 439))
        self.screen.blit(self.Result_label, (439, 35))
        self.screen.blit(self.Graph_label, (441, 184))
        self.screen.blit(self.error_message, (22, 0))
        # draw buttons
        self.submit_btn.draw()
        self.back_btn.draw()
        self.add_constraint_btn.draw()
        self.remove_constraint_btn.draw()
        # get the constraints to display on screen
        self.drawConstraintsBoard()
        if self.Graph_image != '':
            self.screen.blit(self.Graph_image, (441, 215))

    def drawMinimizeFunction(self):
        plotter = ExpressionPlotter.ExpressionPlotter(size=(1000, 600))
        while True:
            try:
                UI_REFRESH_RATE = self.clock.tick(24)/1000
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        exit()
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if self.submit_btn.check_click():
                            self.error_message = self.text_font_smaller.render('', True, 'red')
                            self.expression = self.Expression_input.get_text()
                            if self.expression:
                                minimizePoint = MinimizeCaculator.MinimizePoint(self.expression, self.constraints)
                                self.result = minimizePoint.MinimizeResult()
                                self.Result_board.html_text = f'Expression: {self.expression} \n Result: \n {str(self.result)}'
                                self.Result_board.rebuild()
                                self.Graph_image = plotter.plot(self.expression, self.result)
                        if self.back_btn.check_click():
                            return
                        if self.add_constraint_btn.check_click():
                            if self.Constraint_input.get_text() != '':
                                self.constraints.append(self.Constraint_input.get_text())
                        if self.remove_constraint_btn.check_click():
                            if self.constraints and self.Index_input.get_text() != '':
                                self.constraints.pop(int(self.Index_input.get_text())-1) 

                self.manager.process_events(event)
                self.manager.update(UI_REFRESH_RATE)
                self.screen.fill("#8488f4")
                # draw components managed by UIManager
                self.drawComponents()
                # if self.expression != '':
                #     plotter.plot(self.expression, point=self.result, position=(441, 215))
                self.manager.draw_ui(self.screen)
                pg.display.update() 
            except Exception as e:
                self.error_message = self.text_font_smaller.render(f'#{e}', True, 'red')
                print(e)  

if __name__ == "__main__":
    MinimizeFunction().drawMinimizeFunction()
