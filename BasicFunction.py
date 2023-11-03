

# Basic calculator + - * / ^ .

import numpy as np
import scipy as sp
import math 
import re
from word2number import w2n
# Nhập vào 1 chuỗi '(' ,  ')' ,  '+', '-' , '/' , '*', '^' '.'  và cả '%' cả '//'
# trả về giá trị 
def calculate_expression(expression):
    # Replace the square root symbol (√) with the Python math.sqrt function
    expression = re.sub(r'√(\d+(\.\d+)?)', r'math.sqrt(\1)', expression) 
    # Replace "^" with "**" for exponentiation ( chuyển sang ^ )
    expression = expression.replace('^', '**')
    # Replace dots with decimal points for numerical analysis ( chuyến sang dots)
    expression = expression.replace('.', '.')
    try:
        result = eval(expression)
        return result
    except Exception as e:
        # Trường hợp chuỗi sai cấu trúc sẽ báo lỗi
        return f"Error: {str(e)}"

#check float
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# nhập vào √ xuất ra giá trị căn bậc 2
def calculate_sqrt(n):
    if is_float(n)==False or float(n)<=0:
        return "ERORR"
    else:
        return str(math.sqrt(float(n)))
    
#nhap vào x^2 xuất ra giá trị mũ 2
def calculate_dot(n):
    if is_float(n)==False:
        return "ERROR"
    else:
        return str(math.pow(float(n),2))

# Input string
# input_string = '13%4'
# Calculate the result
# result = calculate_expression(input_string)

# print(f"Input string: {input_string}")
# print(f"Result: {result}")
# result1=calculate_sqrt("1.44")
# print (f"{result1}")
# result2=calculate_dot("1.2")
# print(f"{result2}")