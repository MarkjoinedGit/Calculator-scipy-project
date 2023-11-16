from typing import Any
import pygame as pg
from OptimizeMinimize import buttons as bt
import pygame_gui
from OptimizeMinimize import BasicFunction 
from static import *

class Calculator:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pg.display.set_caption('Caculator')
        self.clock = pg.time.Clock()
        self.manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.calculator_surf = pg.image.load(r'OptimizeMinimize\assets\background\screen-background.png').convert()
        self.calculator_rect = self.calculator_surf.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))

        self.text_font = pg.font.Font(r'OptimizeMinimize\assets\font\montserrat\Montserrat-Light.otf',25)

        #text_input
        self.text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pg.Rect((320, 55), (359, 37)), manager=self.manager, object_id='#number_entry')
        self.result_text = ''
        self.result_rect = pg.Rect(320, 113, 359, 79)
        self.result_textbox = pygame_gui.elements.UITextEntryLine(relative_rect=self.result_rect, manager=self.manager, object_id="#result_entry")
        self.initailButtons()

    def initailButtons(self):
        # position of each buttons on calculator
        matrix = [
            ['C', 'CE', '<-', '(', ')'],
            [7, 8, 9, '/', '√'],
            [4, 5, 6, '*', '^2'],
            [1, 2, 3, '-', '^'],
            [0, '.', 'ans', '+', '=']
        ]
        self.number_list = []
        self.function_list = []
        for i in range(5):
            for j in range(5):
                if i == 0 or j >= 3:
                    Btn = bt.Button(self.screen, self.text_font, f'{matrix[i][j]}', 72, 72, (300 + 81*j, 213 + 81*i), False, 24, '#4E505F', '#646677', '#FFFFFF', '#FFFFFF')
                    self.function_list.append(Btn)
                else:
                    Btn = bt.Button(self.screen, self.text_font, f'{matrix[i][j]}', 72, 72, (300 + 81*j, 213 + 81*i), False, 24, '#2E2F38', '#393B4A', '#FFFFFF', '#FFFFFF')
                    self.number_list.append(Btn)

        #Back button
        self.back_btn = bt.Button(self.screen, self.text_font, 'Back', 153, 36, (22, 548), False, 30, '#FF9A24', '#F3B771', '#ffffff', '#ffffff')
    def Run(self):
        while True:
            UI_REFRESH_RATE = self.clock.tick(60)/1000
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.back_btn.check_click():
                        return
                    for btn in self.number_list:
                        if btn.check_click():
                            self.text_input.set_text(self.text_input.get_text() + btn.text)
                            print(btn.check_click())
                    for btn in self.function_list:
                        if btn.check_click():
                            if btn.text == '<--':
                                current_text =self.text_input.get_text()
                                if len(current_text):
                                    self.text_input.set_text(current_text[:-1])
                            elif btn.text == 'CE':
                                self.text_input.set_text('')
                                self.result_textbox.set_text('')
                            elif btn.text == '=':
                                result = BasicFunction.calculate_expression(self.text_input.get_text())
                                result_text = str(result)
                                self.result_textbox.set_text(result_text)
                                print(BasicFunction.calculate_expression(self.text_input.get_text()))
                            else:
                                self.text_input.set_text(self.text_input.get_text() + btn.text)
                            print(btn.check_click())

                if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#number_entry'):
                    result = BasicFunction.calculate_expression(self.text_input.get_text())
                    result_text = str(result)
                    self.result_textbox.set_text(result_text)
                    print(BasicFunction.calculate_expression(self.text_input.get_text()))
                    
                if (event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED and event.ui_object_id == '#result_entry'):
                    self.result_textbox.set_text(result_text)
                    

                self.manager.process_events(event)

            self.manager.update(UI_REFRESH_RATE)
            self.screen.fill('#2e1b5b')
            self.screen.blit(self.calculator_surf, self.calculator_rect)

            #Draw buttons on calculator
            for btn in self.number_list:
                btn.draw()  
            for btn in self.function_list:
                btn.draw()

            self.back_btn.draw()

            self.manager.draw_ui(self.screen)

            pg.display.update()
