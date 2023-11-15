import pygame
import math
from pygame.locals import *
from sympy import symbols, lambdify, sympify
from scipy import integrate as scipy_integrate

def tinh_tich_phan(function, a, b):
    x = symbols('x')
    python_function = lambdify(x, function, "numpy")
    result, error = scipy_integrate.quad(python_function, a, b)
    return result, error

def Integral():
    # Khởi tạo Pygame
    pygame.init()

   # Kích thước cửa sổ
    window_width, window_height = 1000, 600
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Integrate")
    #background_color = (255, 255, 0)  # Màu vàng cho nền cửa sổ

    # Tải hình ảnh nền
    background_image = pygame.image.load("Calculator-scipy-project\Background\\background3.png")
    # Tạo một bản sao nền có kích thước phù hợp với cửa sổ
    background_scaled = pygame.transform.scale(background_image, (window_width, window_height))

    # Màu sắc
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Font
    font = pygame.font.Font(None, 30)
    button_font = pygame.font.Font(None, 50)  # Kích thước chữ nút là 50

    # Biến
    function = ""
    lower_limit = ""
    upper_limit = ""
    result_text = ""

    active_input = None

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    try:
                        lower_limit_expr = sympify(lower_limit)
                        upper_limit_expr = sympify(upper_limit)

                        # Đánh giá giới hạn dưới và giới hạn trên
                        lower_limit_value = lower_limit_expr.evalf(subs={'pi': math.pi})
                        upper_limit_value = upper_limit_expr.evalf(subs={'pi': math.pi})

                        result, error = tinh_tich_phan(function, lower_limit_value, upper_limit_value)
                        result_text = f"Result: {result}\nError: {error}"
                    except Exception as e:
                        result_text = f"Error: {str(e)}"
                        print("Có lỗi xảy ra:", str(e))
                elif event.key == K_BACKSPACE:
                    if active_input == "lower_limit":
                        lower_limit = lower_limit[:-1]
                    elif active_input == "upper_limit":
                        upper_limit = upper_limit[:-1]
                    else:
                        function = function[:-1]
                else:
                    if active_input == "lower_limit":
                        lower_limit += event.unicode
                    elif active_input == "upper_limit":
                        upper_limit += event.unicode
                    else:
                        function += event.unicode
            elif event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if 254 <= x <= 441 and 69 <= y <= 129:
                    active_input = "lower_limit"
                elif 254 <= x <= 441 and 199 <= y <= 259:
                    active_input = "upper_limit"
                elif 860 <= x <= 920 and 340 <= y <= 400:  # Kiểm tra xem có nhấn vào nút "=" không
                    try:
                        lower_limit_expr = sympify(lower_limit)
                        upper_limit_expr = sympify(upper_limit)

                        # Đánh giá giới hạn dưới và giới hạn trên
                        lower_limit_value = lower_limit_expr.evalf(subs={'pi': math.pi})
                        upper_limit_value = upper_limit_expr.evalf(subs={'pi': math.pi})

                        result, error = tinh_tich_phan(function, lower_limit_value, upper_limit_value)
                        result_text = f"Result: {result}\nError: {error}"
                    except Exception as e:
                        result_text = f"Error: {str(e)}"
                        print("Có lỗi xảy ra:", str(e))
                else:
                    active_input = None

        # Hiển thị nội dung
        screen.blit(background_scaled, (0, 0))
        #funtion
        function_label = font.render("Enter function f(x):", True, black)
        screen.blit(function_label, (52, 310))
        # Vẽ ô nhập biểu thức với màu trắng và chữ màu đen
        function_rect = pygame.Rect(52, 342, 800, 60)
        pygame.draw.rect(screen, white, function_rect)
        pygame.draw.rect(screen, white, function_rect, 2)

        function_text = font.render(function, True, black)
        screen.blit(function_text, (52, 362))
        #giới hạn dưới
        lower_limit_label = font.render("Lower limit a:", True, black)
        screen.blit(lower_limit_label, (100, 69))
        # Vẽ ô nhập giới hạn dưới với màu trắng và chữ màu đen
        lower_limit_rect = pygame.Rect(254, 69, 187, 60)
        pygame.draw.rect(screen, white, lower_limit_rect)
        pygame.draw.rect(screen, white, lower_limit_rect, 2)

        lower_limit_text = font.render(lower_limit, True, black)
        screen.blit(lower_limit_text, (254, 89))
        #giới hạn trên
        upper_limit_label = font.render("Upper limit b:", True, black)
        screen.blit(upper_limit_label, (100, 199))
        # Vẽ ô nhập giới hạn trên với màu trắng và chữ màu đen
        upper_limit_rect = pygame.Rect(254, 199, 187, 60)
        pygame.draw.rect(screen, white, upper_limit_rect)
        pygame.draw.rect(screen, white, upper_limit_rect, 2)

        upper_limit_text = font.render(upper_limit, True, black)
        screen.blit(upper_limit_text, (254, 219))

        # Vẽ nút tính toán (hình tròn màu trắng, chữ "=" màu đen)
        calculate_button = pygame.draw.circle(screen, white, (890, 370), 30)
        pygame.draw.circle(screen, white, (890, 370), 30, 2)
        equal_sign = button_font.render("=", True, black)
        screen.blit(equal_sign, (880, 350))        
        
         # Hiển thị kết quả tích phân
        result_rect = pygame.Rect(52, 437, 900, 100)
        pygame.draw.rect(screen, white, result_rect)
        pygame.draw.rect(screen, white, result_rect, 2)

        result_text_lines = result_text.split('\n')
        for i, line in enumerate(result_text_lines):
            line_surface = font.render(line, True, black)
            screen.blit(line_surface, (62, 447 + i * 30))

        pygame.display.flip()

if __name__ == "__main__":
    Integral()
