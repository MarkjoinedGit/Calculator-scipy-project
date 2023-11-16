import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, Text, Scrollbar, LEFT, TOP, BOTTOM, RIGHT, N, S, W
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.interpolate import CubicSpline

# Hàm nội suy bậc ba
def cubic_interpolation(x, x_values, y_values):
    cs = CubicSpline(x_values, y_values)
    return cs(x)

# Hàm tính toán và vẽ đồ thị
def calculate_interpolation():
    # Lấy dữ liệu từ ô nhập liệu
    x_values = entry_x_values.get().split()
    y_values = entry_y_values.get().split()
    x_new = entry_x_new.get()

    try:
        # Kiểm tra xem tất cả các ô nhập liệu có được điền hay không
        if not x_values or not y_values or not x_new:
            raise ValueError("Please fill in all input fields.")

        # Chuyển đổi chuỗi thành danh sách số
        x_values = list(map(float, x_values))
        y_values = list(map(float, y_values))
        x_new = float(x_new)

        # Kiểm tra độ dài của các danh sách
        if len(x_values) != len(y_values):
            raise ValueError("The number of X values must be equal to the number of Y values.")

        # Thực hiện nội suy bậc ba
        y_interpolated = cubic_interpolation(x_new, x_values, y_values)

        # Hiển thị kết quả
        result_text.delete(1.0, 'end')
        result_text.insert('end', f"Cubic Interpolation at x = {x_new}: {y_interpolated}\n")

        # Vẽ điểm nội suy mới mà không cần xóa và vẽ lại toàn bộ đồ thị
        plt.scatter(x_new, y_interpolated, color='#FF4500', label=f'Interpolation at x={x_new}')
        plt.legend(loc='upper left')
        canvas.draw()

    except ValueError as e:
        # Hiển thị thông báo lỗi
        result_text.delete(1.0, 'end')
        result_text.insert('end', f"Error: {str(e)}\n")

# Hàm đặt lại đồ thị
def reset_graph():
    plt.clf()
    result_text.delete(1.0, 'end')
    entry_x_values.delete(0, 'end')
    entry_y_values.delete(0, 'end')
    entry_x_new.delete(0, 'end')
    canvas.draw()

def back():
    root.destroy()

# Tạo giao diện
root = Tk()
root.title("Cubic Interpolation Calculator")

window_width = 1300
window_height = 600
window_x = (root.winfo_screenwidth() - window_width) // 2
window_y = (root.winfo_screenheight() - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Cấu hình giao diện
style = ttk.Style()
style.configure('TEntry', padding=(10, 5, 10, 5), fieldbackground='#FFD700')
style.configure('TFrame', background='#f0f8ff')  # Đổi màu nền của Frame

# Frame chứa các phần nhập liệu và kết quả
frame = ttk.Frame(root, padding="20", style='TFrame')
frame.grid(row=0, column=0, padx=10, pady=10, sticky=(N, S, W))

# Nhập liệu X
ttk.Label(frame, text="Enter X values (separated by spaces):", font=('Arial', 12, 'bold')).grid(row=0, column=0, sticky='w', pady=5)
entry_x_values = ttk.Entry(frame)
entry_x_values.grid(row=0, column=1, pady=5)

# Nhập liệu Y
ttk.Label(frame, text="Enter Y values (separated by spaces):", font=('Arial', 12, 'bold')).grid(row=1, column=0, sticky='w', pady=5)
entry_y_values = ttk.Entry(frame)
entry_y_values.grid(row=1, column=1, pady=5)

# Nhập liệu X mới
ttk.Label(frame, text="Enter the new X value for interpolation:", font=('Arial', 12, 'bold')).grid(row=2, column=0, sticky='w', pady=5)
entry_x_new = ttk.Entry(frame)
entry_x_new.grid(row=2, column=1, pady=5)

# Nút tính toán và vẽ đồ thị
ttk.Button(frame, text="Calculate and Display Graph", command=calculate_interpolation).grid(row=3, column=0, pady=10, columnspan=2)

# Nút đặt lại
ttk.Button(frame, text="Reset", command=reset_graph).grid(row=3, column=1, pady=10, columnspan=2)

# Nút back lại chương trình
ttk.Button(frame, text="Back", command=back).grid(row=3, column=2, pady=10, columnspan=2)

# Kết quả
result_text = Text(frame, wrap='word', height=5, width=50)
result_text.grid(row=4, column=0, columnspan=2, pady=10)

# Scrollbar cho kết quả
scrollbar = Scrollbar(frame, command=result_text.yview)
scrollbar.grid(row=4, column=2, sticky='nsew')
result_text['yscrollcommand'] = scrollbar.set

# Cấu hình cột và dòng của frame
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_rowconfigure(3, weight=1)
frame.grid_rowconfigure(4, weight=1)

# Frame chứa đồ thị
frame_graph = ttk.Frame(root, padding="20", style='TFrame')
frame_graph.grid(row=0, column=1, padx=10, pady=10)

# Subplot cho đồ thị
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=frame_graph)
canvas.draw()
canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

# kiểm tra xem ứng dụng có đang chạy không
running = True

# Chạy ứng dụng
def run():
    root.mainloop()
    
