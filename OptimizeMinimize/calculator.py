from typing import Any
import pygame as pg
from pygame.sprite import Group
import buttons as bt
import pygame_gui
import BasicFunction 

pg.init()
screen = pg.display.set_mode((800, 650))
pg.display.set_caption('Caculator')
clock = pg.time.Clock()
manager = pygame_gui.UIManager((800, 650))

matrix = [
    ['C', 'CE', '<-', '(', ')'],
    [7, 8, 9, '/', '√'],
    [4, 5, 6, '*', '^2'],
    [1, 2, 3, '-', '^'],
    [0, '.', 'ans', '+', '=']
]

calculator_surf = pg.image.load(r'assets\background\screen-background.png').convert()
calculator_rect = calculator_surf.get_rect(center=(400, 325))

text_font = pg.font.Font(r'assets\font\montserrat\Montserrat-Light.otf',25)

#text_input
text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pg.Rect((220, 55), (359, 37)), manager=manager, object_id='#number_entry')
result_text = ''
result_rect = pg.Rect(220, 113, 359, 79)
result_textbox = pygame_gui.elements.UITextEntryLine(relative_rect=result_rect, manager=manager, object_id="#result_entry")

#Groups
number_list = []
function_list = []

for i in range(5):
    for j in range(5):
        if i == 0 or j >= 3:
            Btn = bt.Button(screen, text_font, f'{matrix[i][j]}', 72, 72, (202 + 81*j, 226 + 81*i), False, 24, '#4E505F', '#646677', '#FFFFFF', '#FFFFFF')
            function_list.append(Btn)
        else:
            Btn = bt.Button(screen, text_font, f'{matrix[i][j]}', 72, 72, (202 + 81*j, 226 + 81*i), False, 24, '#2E2F38', '#393B4A', '#FFFFFF', '#FFFFFF')
            number_list.append(Btn)

while True:
    UI_REFRESH_RATE = clock.tick(60)/1000
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            for btn in number_list:
                if btn.check_click():
                    text_input.set_text(text_input.get_text() + btn.text)
                    print(btn.check_click())
            for btn in function_list:
                if btn.check_click():
                    if btn.text == '<--':
                        current_text =text_input.get_text()
                        if len(current_text):
                            text_input.set_text(current_text[:-1])
                    elif btn.text == 'CE':
                        text_input.set_text('')
                    elif btn.text == '=':
                        result = BasicFunction.calculate_expression(text_input.get_text())
                        result_text = str(result)
                        result_textbox.set_text(result_text)
                        print(BasicFunction.calculate_expression(text_input.get_text()))
                    else:
                        text_input.set_text(text_input.get_text() + btn.text)
                    print(btn.check_click())

        if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#number_entry'):
            result = BasicFunction.calculate_expression(text_input.get_text())
            result_text = str(result)
            result_textbox.set_text(result_text)
            print(BasicFunction.calculate_expression(text_input.get_text()))
            
        if (event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED and event.ui_object_id == '#result_entry'):
            result_textbox.set_text(result_text)
            

        manager.process_events(event)

    manager.update(UI_REFRESH_RATE)
    screen.fill('#2e1b5b')
    screen.blit(calculator_surf, calculator_rect)

    for btn in number_list:
        btn.draw()
    
    for btn in function_list:
        btn.draw()

    manager.draw_ui(screen)

    pg.display.update()
