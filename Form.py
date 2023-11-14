import pygame
import sys
from Integral import Integral
# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
window_width, window_height = 1000, 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Scipy")

# Màu sắc
white = (255, 255, 255)
black = (0, 0, 0)

# Tải hình ảnh nền
background_image = pygame.image.load("Background\\background.png")
background_image1 = pygame.image.load("Background\\background1.png")
background_image2 = pygame.image.load("Background\\background2.png")

# Tạo một bản sao nền có kích thước phù hợp với cửa sổ
background_scaled = pygame.transform.scale(background_image, (window_width, window_height))
background_scaled1 = pygame.transform.scale(background_image1, (window_width, window_height))
background_scaled2 = pygame.transform.scale(background_image2, (window_width, window_height))

def load_image(image_path):
    image = pygame.image.load(image_path)
    return image

def main():
    running = True
    current_interface = "interface1"
    
    # Load hình ảnh cho nút
    button_image = load_image("Button\Start.png")
    button_image = pygame.transform.scale(button_image, (300, 50))  # Chỉnh kích thước nút
    basic_image=load_image("Button\BASIC.png")
    basic_image=pygame.transform.scale(basic_image, (250, 50))
    complex_image=load_image("Button\COMPLEX.png")
    complex_image=pygame.transform.scale(complex_image, (250, 50))
    back_image=load_image("Button\BACK.png")
    back_image=pygame.transform.scale(back_image, (100, 30))
    matrix_image=load_image("Button\MATRIX.png")
    matrix_image=pygame.transform.scale(matrix_image, (200, 50))
    integral_image=load_image("Button\INTEGRAL.png")
    integral_image=pygame.transform.scale(integral_image, (200, 50))
    interpolate_image=load_image("Button\INTERPOLATE.png")
    interpolate_image=pygame.transform.scale(interpolate_image, (200, 50))
    minimalize_image=load_image("Button\MINIMALIZE.png")
    minimalize_image=pygame.transform.scale(minimalize_image, (200, 50))
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if current_interface == "interface1":
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        current_interface = "interface2"
                elif current_interface == "interface2":
                    if button1_rect.collidepoint(mouse_x, mouse_y):
                        # sang giao diện calculator
                        pass
                    elif button2_rect.collidepoint(mouse_x, mouse_y):
                        current_interface="interface3"
                    elif back_button_rect.collidepoint(mouse_x, mouse_y):
                        current_interface = "interface1"
                elif current_interface == "interface3":
                    if back_button_rect.collidepoint(mouse_x, mouse_y):
                        current_interface = "interface2"
                    elif button1_rect.collidepoint(mouse_x, mouse_y):
                       pass#giao diện matrix
                    elif button2_rect.collidepoint(mouse_x, mouse_y):
                        Integral();
                    elif button3_rect.collidepoint(mouse_x, mouse_y):
                       pass#giao diện Interpolate
                    elif button4_rect.collidepoint(mouse_x, mouse_y):
                       pass#giao diện minimalize
                        
        
        # Vẽ hình ảnh nền đã co dãn vừa với cửa sổ
        if current_interface == "interface1":
           screen.blit(background_scaled, (0, 0))
        elif current_interface == "interface2":
           screen.blit(background_scaled1, (0, 0))
        elif current_interface == "interface3":
           screen.blit(background_scaled2, (0, 0))


        if current_interface == "interface1":
            # Vẽ nút với hình ảnh
            button_width, button_height =300, 50  # Kích thước mới của nút
            button_x = (window_width - button_width) // 2  # Tọa độ X mới của nút
            button_y = (window_height - button_height) // 2 +60  # Tọa độ Y mới của nút
            button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
            screen.blit(button_image, button_rect)

        elif current_interface == "interface2":
            # Vẽ hai nút ở trung tâm
            button1_width, button1_height = 250, 50
            button1_x = (window_width - button1_width) // 2
            button1_y = (window_height - button1_height) // 3
            button1_rect = pygame.Rect(button1_x, button1_y, button1_width, button1_height)
            screen.blit(basic_image, button1_rect)

            button2_width, button2_height = 250, 50
            button2_x = (window_width - button2_width) // 2
            button2_y = (window_height - button2_height) // 1.7
            button2_rect = pygame.Rect(button2_x, button2_y, button2_width, button2_height)
            screen.blit(complex_image, button2_rect)

            # Vẽ nút ở góc bên trái phía trên
            back_button_width, back_button_height = 100, 30
            back_button_x = 20
            back_button_y = 20
            back_button_rect = pygame.Rect(back_button_x, back_button_y, back_button_width, back_button_height)
            screen.blit(back_image, back_button_rect)
            
        elif current_interface == "interface3":
            # Vẽ hai nút ở trung tâm
            button1_width, button1_height = 200, 50
            button1_x = (window_width - button1_width) // 2 -40
            button1_y = (window_height - button1_height) // 4
            button1_rect = pygame.Rect(button1_x, button1_y, button1_width, button1_height)
            screen.blit(matrix_image, button1_rect)
            
            button2_width, button2_height = 200, 50
            button2_x = (window_width - button2_width) // 2 -40
            button2_y = (window_height - button2_height) // 2.7
            button2_rect = pygame.Rect(button2_x, button2_y, button2_width, button2_height)
            screen.blit(integral_image, button2_rect)

            button3_width, button3_height = 200, 50
            button3_x = (window_width - button3_width) // 2 -40
            button3_y = (window_height - button3_height) // 2
            button3_rect = pygame.Rect(button3_x, button3_y, button3_width, button3_height)
            screen.blit(interpolate_image, button3_rect)
            
            button4_width, button4_height = 200, 50
            button4_x = (window_width - button4_width) // 2 -40
            button4_y = (window_height - button4_height) // 1.6
            button4_rect = pygame.Rect(button4_x, button4_y, button4_width, button4_height)
            screen.blit(minimalize_image, button4_rect)

            # Vẽ nút ở góc bên trái phía trên
            back_button_width, back_button_height = 100, 30
            back_button_x = 20
            back_button_y = 20
            back_button_rect = pygame.Rect(back_button_x, back_button_y, back_button_width, back_button_height)
            screen.blit(back_image, back_button_rect)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()