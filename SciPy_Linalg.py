import numpy as np
from scipy import  linalg

#set dèault matrix A, matrix 
matrixA_default="[[1,2],[3,4]]"
matrixB_default="[[4,5],[6,7]]"
matrixC_default="[]"
# function calculate inverse matrix
def inverse_matrix(a):
    return linalg.inv(a)
# solve the linear equation set a @ x = b for the unknown x for square a matrix
#1. check matrix is square matrix
def is_SquareMatrix(a):
    return a.shape[0]==a.shape[1]
#2. Order of sqaure matrix
def OrderMatrix(a):
    if is_SquareMatrix(a)==False: 
        return 0
    else: return a.shape[0]
#3. calculate x if known a,b with a@x=b
def Solve(a,b):
    if (is_SquareMatrix(a)==False or is_SquareMatrix(b)==False or OrderMatrix(a)==OrderMatrix(b)):
        return np.zeros((2,2))
    return linalg.solve(a,b)
# solve_banded(l_and_u, ab, b[, overwrite_ab, ...])
# Solve the equation a x = b for x, assuming a is banded matrix.
#ab[u + i - j, j] == a[i,j]
# Solve_banded ( l_and_u , ab , b , overwrite_ab = False , overwrite_b = False , check_finite = True )
#(l, u) (số nguyên, số nguyên), Số đường chéo dưới và trên khác 0
#ab ( l + u + 1, M) array_like
#check_finite bool, tùy chọn
# b (M,) hoặc (M,K) array_like Bên tay phải
# ghi đè_ab bool, tùy chọn
# Loại bỏ dữ liệu trong ab (có thể nâng cao hiệu suất)
# Có kiểm tra xem ma trận đầu vào chỉ chứa số hữu hạn hay không. Việc tắt có thể giúp tăng hiệu suất nhưng có thể gây ra sự cố (sự cố, không kết thúc) nếu đầu vào chứa vô số hoặc NaN.
#     [5  2 -1  0  0]       [0]
#     [1  4  2 -1  0]       [1]
# a = [0  1  3  2 -1]   b = [2]
#     [0  0  1  2  2]       [2]
#     [0  0  0  1  1]       [3]
#      [*  * -1 -1 -1]
# ab = [*  2  2  2  2]
#      [5  4  3  2  1]
#      [1  1  1  1  *]
# chuyển đổi a sang ab
def convert_to_banded_matrix(a, bandwidth):
    
    num_rows, num_cols = a.shape
    ab = np.zeros((2 * bandwidth + 1, num_cols))

    for i in range(num_rows):
        for j in range(max(0, i - bandwidth), min(num_cols, i + bandwidth + 1)):
            ab[bandwidth + i - j, j] = a[i, j]

    return ab
# def solveBanded(a,b,u,l):
#     ab[u+i-j,j]=a[i,j]
# Thuat toan + - * / 2 ma tran n n
import numpy as np
import scipy as sp
def input_matrix():
    m = int(input("Enter the number of rows (m): "))
    n = int(input("Enter the number of columns (n): "))
    print("Enter matrix elements:")
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            element = float(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)
        print(matrix)
    return np.array(matrix)
# kiem tra 2 ma trận có giống hàng giống cột không
def check_valid_operation(matrix_a, matrix_b):
    return matrix_a.shape == matrix_b.shape
# cong 2 ma tran
def add_matrices(matrix_a, matrix_b):
    # kiem tra co + - duoc khong
    if check_valid_operation(matrix_a, matrix_b):
        result = matrix_a + matrix_b
        return result
    else:
        print ("Matrices cannot be added. Dimensions are not the same.")
        return []
# Tru 2 ma tran 
def subtract_matrices(matrix_a, matrix_b):
    if check_valid_operation(matrix_a, matrix_b):
        result = matrix_a - matrix_b
        return result
    else:
        print ( "Matrices cannot be subtracted. Dimensions are not the same.")
        return []
#  nhan 2 ma tran 
def multiply_matrices(matrix_a, matrix_b):
    # kiem tra so cot cua a va so hang cua b
    if matrix_a.shape[1] == matrix_b.shape[0]:
        result = np.dot(matrix_a, matrix_b)
        return result
    else:
        print ("Matrices cannot be multiplied. Inner dimensions do not match.")
        return []
# / hai ma tran
def divide_matrices(matrix_a, matrix_b):
    # Check if matrix_b is invertible
    # kiem tra ma tran b co nghich dao nguoc duoc hay khong
    if np.linalg.det(matrix_b) != 0:
        result = np.dot(matrix_a, sp.linalg.inv(matrix_b))
        return result
    else:
        print ("Matrix division is not possible. Matrix B is not invertible.")
        return [0]
# Example Usage:
# matrix_a = input_matrix()
# matrix_b = input_matrix()
# result_addition = add_matrices(matrix_a, matrix_b)
# result_subtraction = subtract_matrices(matrix_a, matrix_b)
# result_multiplication = multiply_matrices(matrix_a, matrix_b)
# result_division = divide_matrices(matrix_a, matrix_b)
# print(a)
# print(b)
# print("\nResult of Addition:\n", result_addition)
# print("\nResult of Subtraction:\n", result_subtraction)
# print("\nResult of Multiplication:\n", result_multiplication)
# print("\nResult of Division:\n", result_division)
import ast
import numpy as np
def parse_str_to_np_array(input_str):
    # Replacing commas with spaces
    modified_str = input_str.replace(',', ' ')
    # Using ast.literal_eval to convert the modified string to a Python object (list of lists)
    # python_list = ast.literal_eval(modified_str)
    # # Converting the Python list to a NumPy array
    # np_array = np.array(python_list)
    return modified_str
# input_str = '[[1,2][3,4]]'
# result_array1 = parse_str_to_np_array(input_str)
# print(result_array1)
def str_to_np_array(input_str):
    try:
        # Sửa lỗi cú pháp chuỗi để trở thành hợp lệ cho mảng 2 chiều
        input_str = input_str.replace("[[", "[[").replace("][", "],[").replace("]]", "]]")       
        # Sử dụng ast.literal_eval để đánh giá cú pháp và chuyển đổi chuỗi thành mảng NumPy
        result_array = np.array(ast.literal_eval(input_str))     
        return result_array
    except (SyntaxError, ValueError) as e:
        print(f"Error converting string to NumPy array: {e}")
        return None
# Example usage
# input_str = '[[1,2][3,4]]'
# result_array = str_to_np_array(input_str)
# if result_array is not None:
#     print("NumPy Array:")
#     print(result_array)
import numpy as np
from scipy.linalg import det

def det_matrix(matrix):
    try:
        # Sử dụng hàm det của SciPy để tính định thức
        det_value = det(matrix)
        return det_value
    except ValueError as e:
        print(f"Error calculating determinant: {e}")
        return None
# Example usage
# matrix1 = np.array([[1, 2], [3, 4]])
# matrix2 = np.array([[1, 2], [1, 2]])
# determinant_result1 = det_matrix(matrix1)
# determinant_result2 = det_matrix(matrix2)
# if determinant_result1 is not None:
#     print(f"Determinant of matrix1 is {determinant_result1}")
# if determinant_result2 is not None:
#     print(f"Determinant of matrix2 is {determinant_result2}")
import numpy as np
from scipy import linalg
def solve_linear_equation(a, b):
    try:
        # Solve the linear equation set a @ x == b for x
        x = linalg.solve(a, b)
        return np.array(x)
    except ValueError as e:
        print(f"Error solving linear equation: {e}")
        return None
# Example usage
matrix_a_sol = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
matrix_a_solText="[[3, 2, 0], [1, -1, 0], [0, 5, 1]]"
vector_b_sol = np.array([2, 4, -1])
vector_b_solText="[2, 4, -1]"
# solution = solve_linear_equation(matrix_a_sol, vector_b_sol)
# # if solution is not None:
# print(f"Solution x: {solution}")
#solve_banded
import numpy as np
from scipy import linalg
MatrixA = "[[5,  2, -1,  0,  0],[1 , 4,  2, -1,  0],[0 , 1,  3 , 2, -1],[0 , 0 , 1,  2,  2],[0 , 0  ,0 , 1,  1]]"
MatrixAB = np.array([[0,  0, -1, -1, -1],[0,  2,  2,  2,  2],[5,  4,  3,  2,  1],[1,  1,  1,  1,  0]])
MatrixB = "[0, 1, 2, 2, 3]"
def solve_banded(l,u,ab,b):
    return linalg.solve_banded((l,u),ab,b) 
import numpy as np
from scipy import linalg
#  Function change a to ab not banded matrix
def matrix_to_banded_form(a):
    m, n = a.shape
    ab = np.zeros((m, n), dtype=a.dtype)
    if True:
        for i in range(m):
            if not np.all(a[i, :] == 0):
                for j in range(i + 1):
                    ab[i - j, j] = a[i, j]
    else:
        for i in range(m):
            if not np.all(a[i, :] == 0):
                for j in range(i, n):
                    ab[i - j + n - 1, j] = a[i, j]
    return ab
def solveh_banded(ab, b):
    try:
        x = linalg.solveh_banded(ab, b,lower=True)
        return x
    except Exception as e:
        print(f"An error occurred: {str(e)}")
# Example usage:
MatrixA_1= "[[ 4,  2, -1,  0,  0,  0],[ 2,  5,  2, -1,  0,  0],[-1 , 2,  6,  2, -1 , 0],[ 0 ,-1 , 2, 7,  2, -1] ,[ 0 , 0 ,-1 , 2,  8 , 2] ,[ 0  ,0 , 0 ,-1,  2,  9]]"
MatrixAB_1 = np.array([[ 4,  5,  6,  7, 8, 9],
               [ 2,  2,  2,  2, 2, 0],
               [-1, -1, -1, -1, 0, 0]])

MatrixB_1 = "[1, 2, 2, 3, 3, 3]"
abm=matrix_to_banded_form(str_to_np_array(MatrixA_1))
# print("ab:",abm)
# try:
#     result_x = solveh_banded(abm,str_to_np_array(MatrixB_1))
#     print("Solution Vector x:")
#     print(result_x)
#     res=np.dot(MatrixA_1,result_x)
#     print(res)
# except Exception as e:
#     print(f"An error occurred: {str(e)}")
# AB_1=matrix_to_banded_form(MatrixA)
# print(AB_1
#lstsq(a, b[, cond, overwrite_a, ...])
# Compute least-squares solution to equation Ax = b.
#2
#solve linear matrix equation Ax = B
# Giải hệ phương trình:
# 3x+2y=2
# x-y=4
# 4x-5y=8
# Có thể vô nghiệm
a1_lstsq="[[3,2],[1,-1],[4,-5]]"
b1_lstsq="[[2],[4],[8]]"
def lstsq(a,b):
    c1, resid, rank, sigma = linalg.lstsq(a,b)
    return f"Result:least-square solution {c1},\n Sums of residuals {resid} ,\n Rank: {rank} ,\n Singular values:{sigma}"
# c1, resid, rank, sigma = linalg.lstsq(str_to_np_array(a1_lstsq),str_to_np_array(b1_lstsq))
# #c - least-square solution
#resid - sums of residuals
# rank - rank of matrix a
# s - single values of a
# print(f"Result: {c1},\n {resid} ,\n {rank} ,\n {sigma}")
# print(lstsq(str_to_np_array(a1_lstsq),str_to_np_array(b1_lstsq)))
import numpy as np
from scipy import linalg
# #3 Tìm inverse, deverse, pesudo-inverse của 1 ma trận vuông
# p=np.array([[3,2],[1,-1]])
# # Calculate the inverse of matrix
# # print("Inverse: ",linalg.inv(p))
# # Calculate the determinant of matrix
# # print("diverse:",linalg.det(p))
# # Calculate the pseudo-inverse of matrix
matrixA_pinv="[[3,2],[1,-1],[1,-4]]"
def pinv(a):
    return linalg.pinv(a)
# print("pseudo-inverse:",linalg.pinv(str_to_np_array(matrixA_pinv)))
# #4 Chuẩn ma trận hoặc vector
z1=np.array([3,4])
# # Tính toán chuẩn 1 của vector z1
# # TÍnh toán chuẩn 2 của vector z1 = default
matrixA_norm="[3,4]"
def norm(x,standard):
    if standard =='fro':return f"{linalg.norm(x,'fro')}"
    if standard=="numpy.inf": return f"{linalg.norm(x,np.inf)}" 
    return f"{linalg.norm(x,int(standard))}"
# # print(f"linalg.norm(z1):{linalg.norm(z1)}")
# # print(f"linalg.norm(z1,1):{linalg.norm(z1,1)}")
# print(f"print(linalg.norm(z1,1)):{norm(z1,2)}")
# Eig
# eig(a[, b, left, right, overwrite_a, ...])
# Solve an ordinary or generalized eigenvalue problem of a square matrix.
a_eig="[[1,2],[3,4]]"

def eig(a):
    lamda,v=linalg.eig(a)
    return f"Lamda(eigenvalues):{lamda} \nEigenvectors:{v} \n"
# print(f"k:{eig(str_to_np_array(a_eig))}")
# Decompositions
# svd(a[, full_matrices, compute_uv, ...])
# Singular Value Decomposition.
a_svg="[[1,2,3],[3,4,5]]"
def svd(a):
    U,s,Vh = linalg.svd(a)
    return f"Left singular vectors: {U} \nRight singular vectors: {Vh} \nArray of singular values:{s}"
# print(f"k:{svd(str_to_np_array(a_svg))}")
# diagsvd
# Sig - Construct the sigma matrix  in SVD  from singular values (s)in size (m,n)
m,n=str_to_np_array(a_svg).shape

def diagsvd(a,text):
    U,s,Vh=linalg.svd(a)
    m,n=a.shape
    Sig=linalg.diagsvd(s,m,n)
    return f"Shape of {text}: {m},{n}\nArray of singular values:{s} \nConstruct the sigma matrix  in SVD  from singular values (s)in size ({m},{n}) of {text} : {Sig}"   
# print(f"k:{diagsvd(str_to_np_array(a_svg),'Matrix A')}")
# eigvals(a[, b, overwrite_a, check_finite, ...])
# Compute eigenvalues from an ordinary or generalized eigenvalue problem.
a_eigvals="[[1,2],[4,5]]"
def eigvals(a):
    return f"eigenvalues of A:{linalg.eigvals(a)}"
# Check Matrix is square
def is_square_matrix(matrix):
    # Kiểm tra xem ma trận có phải là ma trận vuông không
    try:
        return  matrix.size > 0 and matrix.shape[0] == matrix.shape[1]
    except : return False 
    
# solve triangle
A_triangle="[[3, 0, 0, 0], [2, 1, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1]]"
B_triangle="[4, 2, 4, 2]"
def solve_triangle(a,b,Lower):
    return linalg.solve_triangular(a,b,lower=Lower)

x=solve_triangle(str_to_np_array(A_triangle),str_to_np_array(B_triangle),True)
# print(f"k:{str_to_np_array(A_triangle).dot(solve_triangle(str_to_np_array(A_triangle),str_to_np_array(B_triangle),True))}")
# # print(f"k:{solve_triangle(np.array([[3, 0, 0, 0], [2, 1, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1]])),   np.array([4, 2, 4, 2]),lower=True)}")
# print(f"{str_to_np_array(A_triangle).dot(x)}")
# a = np.array([[3, 0, 0, 0], [2, 1, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1]])
# b = np.array([4, 2, 4, 2])
# x = linalg.solve_triangular(a, b, lower=True)

# Expm
a_expm="[[1,2],[4,5]]"
def expm(a):
    return linalg.expm(a)

# 	Compute the matrix sine.
a_sinm="[[1.0, 2.0], [-1.0, 3.0]]"
def sinm(a):
    return linalg.sinm(a)
# Compute the matrix cosine.
a_cosm="[[1.0, 2.0], [-1.0, 3.0]]"
def cosm(a):
    return linalg.cosm(a)

#lu_factor & lu_solve
a_LU="[[1,1,0],[1,0,1],[0,1,1]]"
b_LU="[1,2,1]"
def lu_factor(a):
    LU,piv=linalg.lu_factor(a)
    return f"LU={LU},\n piv={piv}"
def lu_solve(a,b):
    return linalg.lu_solve(linalg.lu_factor(a),b)
# print(f"k:{lu_solve(str_to_np_array(a_LU),str_to_np_array(b_LU))}")

# A = np.array([[2, 5, 8, 7], [5, 2, 2, 8], [7, 5, 6, 6], [5, 4, 4, 8]])
# lu, piv = lu_factor(A)
# print(f"LU={lu}, piv={piv}")