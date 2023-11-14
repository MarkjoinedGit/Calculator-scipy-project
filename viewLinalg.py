from pygame.sprite import Group
from pygame.locals import *
from typing import Any

import sys
import pygame as pg
import pygame_gui 
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_agg import FigureCanvasAgg
import seaborn as sns
# Import ColorView.py
import ColorView as color
import SciPy_Linalg as spLinalg

#Load Image
defaultImg=pg.image.load('assets/img/default.png')

# bien toan cuc
view_width = 1200
view_height = 670
FPS=30
pg.font.init()
FONT1 = pg.font.SysFont('Arial', 15)
FONT2 = pg.font.SysFont('veraserif',15)
FONT3 = pg.font.SysFont('sans',15)
class DisplayViewLinalgBasic():
    def __init__(self):
        pg.init()
        pg.font.init()
        self.FONT1 = pg.font.SysFont('sans',24)
        self.FONT2 = pg.font.SysFont('sans',24)
        self.FONT3 = pg.font.SysFont('sans',24)
        self.screen = pg.display.set_mode((view_width,view_height))
        pg.display.set_caption("SciPy Linalg Basic")
        self.clock=pg.time.Clock()
        self.MANAGER = pygame_gui.UIManager((view_width,view_height))
        self.UI_Refesh_rate=pg.time.Clock().tick(60)/10000
        self.running=False
        self.res=""
        self.l=1
        self.u=2
        self.option_list=["+","-","x","/"]
        self.option_standard=['1','2','numpy.inf','fro']
        self.MatrixAB=np.array([])
        self.Matrix_show=np.array([[1,2],[3,4]])
        self.Matrix_show_text="Default:"
        #menu
        self.matrix1text="Matrix a"
        self.matrix2text="Matrix b"
        self.matrix3text="Matrix c"
        self.restext="Result"       
        # Notice
        self.notice="Illegal! There is no solution"
        
        # size matrix box input
        self.widthBox=180
        self.heightBox=200
        
        self.widthAns=790
        self.heightAns=140
        
        self.widthDef=30
        self.heightDef=30
        
        self.ButtonSize=(300,30)
        
        
        self.target_width, self.target_height=540,295
        self.target_x, self.target_y = 55,370
        
        
        self.choice_width, self.choice_height = 230,30
        #Scale Img
        self.defaultImg=pg.transform.scale(defaultImg,(self.widthDef,self.heightDef))
        #Matrix a
        self.Matrix1=np.array([])
        self.Matrix1Box =pygame_gui.elements.UITextEntryBox(relative_rect=pg.Rect((50,4),(self.widthBox,self.heightBox)),
                                                       manager=self.MANAGER,
                                                       object_id="#a_0_0",)
        #Matrix b
        self.Matrix2=np.array([])
        self.Matrix2Box =pygame_gui.elements.UITextEntryBox(relative_rect=pg.Rect((360,4),(self.widthBox,self.heightBox)),
                                                       manager=self.MANAGER,
                                                       object_id="#a_0_0")
        #Matrix c                                      
        self.Matrix3=np.array([])
        self.Matrix3Box =pygame_gui.elements.UITextEntryBox(relative_rect=pg.Rect((660,4),(self.widthBox,self.heightBox)),
                                                       manager=self.MANAGER,
                                                       object_id="#a_0_0")
        
        # Create a ComboBox
        self.comboBox = pygame_gui.elements.UIDropDownMenu(
            options_list=self.option_list,
            starting_option="+",
            relative_rect=pg.Rect((250, 80), (50, 30)),
            manager=self.MANAGER
        )
        #Create Result Box
        self.ResultBox = pygame_gui.elements.UITextEntryBox(relative_rect=pg.Rect((50,225),(self.widthAns,self.heightAns)),
                                                       manager=self.MANAGER,
                                                       object_id="#a_0_0"            
        )
        # Create a Button
        # Button = 
        self.ButtonCal=pygame_gui.elements.UIButton(relative_rect=pg.Rect((560,80),(50, 30)),
                                                    text="=",
                                                    manager=self.MANAGER,
                                                    )
        
        
        #Button Inverse Button
        self.ButtonInv=pygame_gui.elements.UIButton(relative_rect=pg.Rect((850,5),self.ButtonSize),
                                                    text="Inverse of matrix a",
                                                    manager=self.MANAGER,
                                                    )
        #Button  Det Button
        self.ButtonDet=pygame_gui.elements.UIButton(relative_rect=pg.Rect((850,35),self.ButtonSize),
                                                    text="Det of matrix a",
                                                    manager=self.MANAGER)
        
        # Button solve a@x = b
        self.ButtonSol=pygame_gui.elements.UIButton(relative_rect=pg.Rect((850,65),self.ButtonSize),
                                                    text = "Solve a@x = b",
                                                    manager=self.MANAGER)
        
        self.defaultSol=pygame_gui.elements.UIButton(relative_rect=pg.Rect((1150,65),(self.widthDef,self.heightDef)),
                                                    text="",
                                                    manager=self.MANAGER,
                                                    object_id="defaultSol"
                                                    )
        
        # self.defaultSol.image=self.defaultImg()
        # Button Solve the equation a x = b for x assuming a is banded matrix.
        self.ButtonSoLu=pygame_gui.elements.UIButton(relative_rect=pg.Rect((850,95),self.ButtonSize),
                                                    text = "Solve ax=b,LU factorization of a",
                                                    manager=self.MANAGER,)
        self.defaultSoLu=pygame_gui.elements.UIButton(relative_rect=pg.Rect((1150,95),(self.widthDef,self.heightDef)),
                                                    text="",
                                                    manager=self.MANAGER,)
        
        
        # Button solve the equation ax=b Solve equation a x = b.
        self.ButtonSolhBanded=pygame_gui.elements.UIButton(relative_rect=pg.Rect((850,125),self.ButtonSize),
                                                            text="Solve ax=b",
                                                            manager=self.MANAGER) 
        self.defaultSolhBanded=pygame_gui.elements.UIButton(relative_rect=pg.Rect((1150,125),(self.widthDef,self.heightDef)),
                                                    text="",
                                                    manager=self.MANAGER,)

        # Lstsq
        self.ButtonLstsq=pygame_gui.elements.UIButton(relative_rect=pg.Rect((850,155),self.ButtonSize),
                                                            text="Compute least-squares Ax = b",
                                                            manager=self.MANAGER)
        self.defaultLstsq=pygame_gui.elements.UIButton(relative_rect=pg.Rect((1150,155),(self.widthDef,self.heightDef)),
                                                    text="",
                                                    manager=self.MANAGER,)
           
        #Pinv
        self.ButtonPinv=pygame_gui.elements.UIButton(relative_rect=pg.Rect((850,185),self.ButtonSize),
                                                            text="Pseudo-inverse of A",
                                                            manager=self.MANAGER)
        self.defaultPinv=pygame_gui.elements.UIButton(relative_rect=pg.Rect((1150,185),(self.widthDef,self.heightDef)),
                                                    text="",
                                                    manager=self.MANAGER,
                                                    )
        #Norm
        self.ButtonNorm=pygame_gui.elements.UIButton(relative_rect=pg.Rect((850,215),(150,30)),
                                                            text="Norm of A",
                                                            manager=self.MANAGER)
        #standard comboBox
        self.StandardBox=pygame_gui.elements.UIDropDownMenu(relative_rect=pg.Rect((1050,215),(100,30)),
                                                            options_list=self.option_standard,
                                                            starting_option="2",
                                                            manager=self.MANAGER
                                                             )
        self.defaultNorm=pygame_gui.elements.UIButton(relative_rect=pg.Rect((1150,215),(self.widthDef,self.heightDef)),
                                                    text="",
                                                    manager=self.MANAGER,)
        # Eig
        self.ButtonEig=pygame_gui.elements.UIButton(relative_rect=pg.Rect((850,245),self.ButtonSize),
                                                            text="eigenvalue of A",
                                                            manager=self.MANAGER)
        self.defaultEig=pygame_gui.elements.UIButton(relative_rect=pg.Rect((1150,245),(self.widthDef,self.heightDef)),
                                                    text="",
                                                    manager=self.MANAGER,)
        # Svd
        self.ButtonSvd=pygame_gui.elements.UIButton(relative_rect=pg.Rect((850,275),self.ButtonSize),
                                                            text="Singular Value Decomposition of A",
                                                            manager=self.MANAGER)
        self.defaultSvd=pygame_gui.elements.UIButton(relative_rect=pg.Rect((1150,275),(self.widthDef,self.heightDef)),
                                                    text="",
                                                    manager=self.MANAGER,)
        # diagsvd
        self.ButtonDiagsvd=pygame_gui.elements.UIButton(relative_rect=pg.Rect((850,305),self.ButtonSize),
                                                            text="Sigma matrix from singular of A",
                                                            manager=self.MANAGER)
        self.defaultDiagsvd=pygame_gui.elements.UIButton(relative_rect=pg.Rect((1150,305),(self.widthDef,self.heightDef)),
                                                    text="",
                                                    manager=self.MANAGER,)
        # eigvals
        self.ButtonEigvals=pygame_gui.elements.UIButton(relative_rect=pg.Rect((850,335),self.ButtonSize),
                                                            text="Eigenvalues of A",
                                                            manager=self.MANAGER)
        self.defaultEigvals=pygame_gui.elements.UIButton(relative_rect=pg.Rect((1150,335),(self.widthDef,self.heightDef)),
                                                    manager=self.MANAGER,
                                                    text="",)
        
        #solve triangles
        self.ButtonSolTri=pygame_gui.elements.UIButton(relative_rect=pg.Rect((850,365),self.ButtonSize),
                                                            text="solve ax=b, a-triangular matrix",
                                                            manager=self.MANAGER)
        self.defaultSolTri=pygame_gui.elements.UIButton(relative_rect=pg.Rect((1150,365),(self.widthDef,self.heightDef)),
                                                    manager=self.MANAGER,
                                                    text="",)
        
        #solve Expm 
        self.ButtonExpm=pygame_gui.elements.UIButton(relative_rect=pg.Rect((850,395),self.ButtonSize),
                                                            text="matrix exponential of A",
                                                            manager=self.MANAGER)
        self.defaultExpm=pygame_gui.elements.UIButton(relative_rect=pg.Rect((1150,395),(self.widthDef,self.heightDef)),
                                                    manager=self.MANAGER,
                                                    text="",)
    
        # Sinm of A
        self.ButtonSinm=pygame_gui.elements.UIButton(relative_rect=pg.Rect((850,425),self.ButtonSize),
                                                            text="matrix sine of A",
                                                            manager=self.MANAGER)
        self.defaultSinm=pygame_gui.elements.UIButton(relative_rect=pg.Rect((1150,425),(self.widthDef,self.heightDef)),
                                                    manager=self.MANAGER,
                                                    text="",)
        # Sinm of A
        self.ButtonCosm=pygame_gui.elements.UIButton(relative_rect=pg.Rect((850,455),self.ButtonSize),
                                                            text="matrix cosine of A",
                                                            manager=self.MANAGER)
        self.defaultCosm=pygame_gui.elements.UIButton(relative_rect=pg.Rect((1150,455),(self.widthDef,self.heightDef)),
                                                    manager=self.MANAGER,
                                                    text="",)
        # Button show matrix
        self.ButtonMatrixA=pygame_gui.elements.UIButton(relative_rect=pg.Rect((610,380),(self.choice_width,self.choice_height)),
                                                            text="Show Matrix A",
                                                            manager=self.MANAGER)
        self.ButtonMatrixB=pygame_gui.elements.UIButton(relative_rect=pg.Rect((610,410),(self.choice_width,self.choice_height)),
                                                            text="Show Matrix B",
                                                            manager=self.MANAGER)
        self.ButtonMatrixC=pygame_gui.elements.UIButton(relative_rect=pg.Rect((610,440),(self.choice_width,self.choice_height)),
                                                            text="Show Matrix C",
                                                            manager=self.MANAGER)
        self.ButtonMatrixAB=pygame_gui.elements.UIButton(relative_rect=pg.Rect((610,470),(self.choice_width,self.choice_height)),
                                                            text="Show Matrix AB",
                                                            manager=self.MANAGER)
        
        
        
        #Set default
        self.default()
        # Mathplotlib
        self.fig = plt.figure(figsize=(3, 3), dpi=100)  # Decrease the size of the figure
        self.ax = self.fig.add_subplot(111, projection='3d')
        
        self.x, self.y =np.meshgrid(np.arange(self.Matrix_show.shape[0]), np.arange(self.Matrix_show.shape[1]))
        self.plot_surface = self.ax.plot_surface(self.x,self.y, self.Matrix_show, cmap='plasma', edgecolor='k', linewidth=0.5)
        
        
        self.points = self.ax.scatter(*np.meshgrid(np.arange(self.Matrix_show.shape[0]), np.arange(self.Matrix_show.shape[1])), self.Matrix_show, c='red', s=50, label='Points')

        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        # Adjust the view angle
        self.ax.view_init(elev=0, azim=0)
        # Display Matplotlib plot on Pygame surface
        self.canvas = FigureCanvasAgg(self.fig)
        
        self.ax.scatter(self.x, self.y, self.Matrix_show, c='green', s=50, label='Vertices')

        # Annotate each point with its coordinates
        # for i in range(self.x.shape[0]):
        #     for j in range(self.x.shape[1]):
        #         self.ax.text(self.x[i, j], self.y[i, j], self.Matrix_show[i, j], f'({i},{j},{self.Matrix_show[i, j]:.2f})', fontsize=8)
        for i in range(self.Matrix_show.shape[0]):
            for j in range(self.Matrix_show.shape[1]):
                x0, y0, z0 = i, j, self.Matrix_show[i, j]
                # print(f"{x0},{y0},{z0}")
                text = f'({x0}, {y0}, {z0})'
                self.ax.text(x0, y0, z0, text, color='red', fontsize=8, ha='center', va='center', fontweight='bold')
        self.canvas.draw()
        self.original_surface = pg.image.fromstring(self.canvas.tostring_rgb(), self.canvas.get_width_height(), "RGB")
        self.matplotlib_surface = pg.transform.scale(self.original_surface, (self.target_width,self.target_height))       
        self.rotate = False
        self.elev,self.azim = self.ax.elev,self.ax.azim    
        pg.display.flip()
    def default(self):
        self.comboBox.selected_option="+"
        self.Matrix1Box.set_text(spLinalg.matrixA_default)
        self.Matrix2Box.set_text(spLinalg.matrixB_default)
        self.Matrix3Box.set_text(spLinalg.matrixC_default)
        self.reset="0"
        self.addDataMatrix1_2()
        pass
    def addDataMatrix1_2(self):
        self.Matrix1=spLinalg.str_to_np_array(self.Matrix1Box.get_text())
        self.Matrix2=spLinalg.str_to_np_array(self.Matrix2Box.get_text())
        # print(self.Matrix1Box.get_text())
        # print(self.Matrix2Box.get_text())
        # print(self.Matrix1)
        # print(self.Matrix2)
    def NoticeERORR(self):
        self.matrix3text=""
        self.Matrix3Box.set_text("ERROR") 
    def solveCal(self):
        try:
            self.matrix3text = "Matrix c"
            try:
                if self.comboBox.selected_option=="+":  
                    self.addDataMatrix1_2()
                    self.Matrix3=spLinalg.add_matrices(self.Matrix1,self.Matrix2)
                    print(self.Matrix3)
                    self.Matrix3Box.set_text(np.array2string(self.Matrix3)) 
                if self.comboBox.selected_option=="-":
                    self.addDataMatrix1_2()
                    self.Matrix3=spLinalg.subtract_matrices(self.Matrix1,self.Matrix2)
                    print(self.Matrix3)
                    self.Matrix3Box.set_text(np.array2string(self.Matrix3))
                if self.comboBox.selected_option=="x":
                    self.addDataMatrix1_2()
                    self.Matrix3=spLinalg.multiply_matrices(self.Matrix1,self.Matrix2)
                    print(self.Matrix3)
                    self.Matrix3Box.set_text(np.array2string(self.Matrix3))
                if self.comboBox.selected_option=="/":
                    self.addDataMatrix1_2()
                    self.Matrix3=spLinalg.divide_matrices(self.Matrix1,self.Matrix2)
                    print(self.Matrix3)
                    self.Matrix3Box.set_text(np.array2string(self.Matrix3)) 
            except:
                self.ResultBox.set_text(f"{self.notice}") 
                self.NoticeERORR()
                pass
            # self.drawImage(self.Matrix1)
        except (SyntaxError, ValueError) as e  :
            pass
            print(f"Error converting string to NumPy array: {e}") 
    def solveInv(self):
        try:
            self.addDataMatrix1_2()
            self.Matrix3=spLinalg.inverse_matrix(self.Matrix1)
            print(self.Matrix3)
            self.Matrix3Box.set_text(np.array2string(self.Matrix3)) 
            self.matrix3text="Inverse of A"
            self.ResultBox.set_text("")
        except (SyntaxError, ValueError) as e  :
            print(f"Error converting string to NumPy array: {e}")
            self.ResultBox.set_text(f"{self.notice}because Matrix A doesn't have a inverse") 
            self.NoticeERORR()
    def solveDet(self):
        try:
            self.addDataMatrix1_2()
            self.res=spLinalg.det_matrix(self.Matrix1)
            print(self.res)
            self.ResultBox.set_text(str(self.res))
            self.restext="Det of A"
        except (SyntaxError, ValueError) as e  :
            print(f"Error converting string to NumPy array: {e}")
            self.ResultBox.set_text(f"{self.notice} because Matrix A doesn't have a inverse") 
            self.NoticeERORR()
    #Solve
    # Default
    def setDefaultSol(self):
        self.Matrix1Box.set_text(spLinalg.matrix_a_solText)
            
        # self.Matrix1=spLinalg.matrix_a_sol
        self.Matrix2Box.set_text(spLinalg.vector_b_solText)
        # self.Matrix2=spLinalg.vector_b_sol
        
    def solveSol(self):
        try:
            self.addDataMatrix1_2()
            try:
                self.matrix3text='matrix x'
                self.Matrix3=spLinalg.solve_linear_equation(self.Matrix1,self.Matrix2)
                # print(self.Matrix3)
                self.Matrix3Box.set_text(np.array2string(self.Matrix3))
                self.ResultBox.set_text("")
            except (SyntaxError, ValueError,AttributeError,IndexError,ImportError) as e:
                self.ResultBox.set_text(f"{self.notice}")
                self.NoticeERORR()
        except (SyntaxError, ValueError,AttributeError,IndexError,ImportError) as e  :
            print(f"Error converting string to NumPy array: {e}")
   
    #Solve Solve LU
        #Set default
    def setDefaultSolu(self):
        self.Matrix1Box.set_text(spLinalg.a_LU)
        self.Matrix2Box.set_text(spLinalg.b_LU)      
    def solveSoLu(self):
        try:
            # Ban dau de xet default de do nhap
            self.addDataMatrix1_2()
            # Tam thoi default
            self.matrix3text='matrix x:'
            self.Matrix3=spLinalg.lu_solve(self.Matrix1,self.Matrix2)
            print(self.Matrix3)
            self.Matrix3Box.set_text(np.array2string(self.Matrix3))
            self.ResultBox.set_text(spLinalg.lu_factor(self.Matrix1))
            self.restext="LU and piv of A:"
        except (SyntaxError, ValueError,AttributeError,IndexError,ImportError) as e  :
            print(f"Error converting string to NumPy array: {e}")
            self.ResultBox.set_text(f"{self.notice}")
            self.NoticeERORR()
    #Solve SolhBanded
        #Set default
    def setDefaultSolhBanded(self):
        self.Matrix1Box.set_text(spLinalg.MatrixA_1)
        self.Matrix2Box.set_text(spLinalg.MatrixB_1)
    def solveSolhBanded(self):
        try:
            # self.setDefaultSolhBanded()
            # Ban dau de xet default de do nhap
            self.addDataMatrix1_2()
            self.MatrixAB=spLinalg.matrix_to_banded_form(self.Matrix1)
            self.Matrix3=spLinalg.solveh_banded(self.MatrixAB,self.Matrix2)
            print(self.Matrix3)
            self.Matrix3Box.set_text(np.array2string(self.Matrix3))
            self.ResultBox.set_text("")
            self.matrix3text="matrix x"
        except (SyntaxError, ValueError,AttributeError,IndexError,ImportError) as e  :
            print(f"Error converting string to NumPy array: {e}")
            self.ResultBox.set_text(f"{self.notice}")
            self.NoticeERORR()
    #solve Lstsq
    def solveLstsq(self):
        try:
            self.addDataMatrix1_2()
            self.restext="Least-squares solution Ax=b"
            self.ResultBox.set_text(spLinalg.lstsq(self.Matrix1,self.Matrix2))
            self.Matrix3Box.set_text("")
        except (SyntaxError, ValueError,AttributeError,IndexError,ImportError) as e  :
            print(f"Error converting string to NumPy array: {e}")
            self.ResultBox.set_text(f"{self.notice}")
            self.NoticeERORR()
            
    def setDefaultLstsq(self):
        self.Matrix1Box.set_text(spLinalg.a1_lstsq)
        self.Matrix2Box.set_text(spLinalg.b1_lstsq)
    #solve pinv
    def solvePinv(self):
        try:
            self.addDataMatrix1_2()
            self.matrix3text="Pinv of A"
            self.Matrix3=spLinalg.pinv(self.Matrix1)
            print(self.Matrix3)
            self.Matrix3Box.set_text(np.array2string(self.Matrix3))
            self.ResultBox.set_text("")
        except (SyntaxError, ValueError,AttributeError,IndexError,ImportError) as e  :
            print(f"Error converting string to NumPy array: {e}")
            self.ResultBox.set_text(f"{self.notice}")
            self.NoticeERORR()
    def setDefaultPinv(self):
        self.Matrix1Box.set_text(spLinalg.matrixA_pinv)
    #Norm
    def setDefaultNorm(self):
        self.Matrix1Box.set_text(spLinalg.matrixA_norm)
    def solveNorm(self):
        try:
            
            self.addDataMatrix1_2()
            self.restext=f"Norm of A (standard: {self.StandardBox.selected_option})"
            self.ResultBox.set_text(spLinalg.norm(self.Matrix1, self.StandardBox.selected_option))
            self.Matrix3Box.set_text("")
        except (SyntaxError, ValueError,AttributeError,IndexError,ImportError) as e  :
            print(f"Error converting string to NumPy array: {e}")
            self.ResultBox.set_text(f"{self.notice}")
            self.NoticeERORR()
    #Eig
    def solveEig(self):
        try:
            self.addDataMatrix1_2()
            self.restext="Eig of A:"
            self.ResultBox.set_text(spLinalg.eig(self.Matrix1))
        except (SyntaxError, ValueError) as e  :
            print(f"Error converting string to NumPy array: {e}")          
    def setdefaultEig(self):
        self.Matrix1Box.set_text(spLinalg.a_eig)
    #Svd
    def solveSvd(self):
        try:
            self.addDataMatrix1_2()
            self.restext="Singular Value Decomposition of A:"
            self.ResultBox.set_text(spLinalg.svd(self.Matrix1))
            self.Matrix3Box.set_text("")
        except (SyntaxError, ValueError,AttributeError,IndexError,ImportError) as e  :
            print(f"Error converting string to NumPy array: {e}")
            self.ResultBox.set_text(f"{self.notice}")
            self.NoticeERORR()
    def setdefaultSvd(self):
        self.Matrix1Box.set_text(spLinalg.a_svg)
    #Diagsvd
    def solveDiagsvd(self):
        try:
            self.addDataMatrix1_2()
            self.restext="Diagonal Singular Value Decomposition of A:"
            self.ResultBox.set_text(spLinalg.diagsvd(self.Matrix1,'Matrix A'))
            self.Matrix3Box.set_text("")
        except (SyntaxError, ValueError,AttributeError,IndexError,ImportError) as e  :
            print(f"Error converting string to NumPy array: {e}")
            self.ResultBox.set_text(f"{self.notice}")
            self.NoticeERORR()
    def solveEigvals(self):
        try:
            self.addDataMatrix1_2()
            self.restext="eigenvalues from matrix A:"
            self.ResultBox.set_text(spLinalg.eigvals(self.Matrix1))
            self.Matrix3Box.set_text("")
        except (SyntaxError, ValueError,AttributeError,IndexError,ImportError) as e  :
            print(f"Error converting string to NumPy array: {e}")
            self.ResultBox.set_text(f"{self.notice}")
            self.NoticeERORR()
    def setdefaultEigvals(self):
        self.Matrix1=spLinalg.a_eigvals
    def solveSolTri(self):
        try:
            self.addDataMatrix1_2()
            self.matrix3text="matrix x:"
            self.Matrix3=spLinalg.solve_triangle(self.Matrix1,self.Matrix2,True)
            print(self.Matrix3)
            self.Matrix3Box.set_text(np.array2string(self.Matrix3))
            self.ResultBox.set_text("")
        except (SyntaxError, ValueError,AttributeError,IndexError,ImportError) as e  :
            print(f"Error converting string to NumPy array: {e}")
            self.ResultBox.set_text(f"{self.notice}")
            self.NoticeERORR()
    def setDefaultSolTri(self):
        self.Matrix1Box.set_text(spLinalg.A_triangle)
        self.Matrix2Box.set_text(spLinalg.B_triangle)
    def solveExpm(self):
        try:
            self.addDataMatrix1_2()
            self.matrix3text="Exp(A):"
            self.Matrix3=spLinalg.expm(self.Matrix1)
            print(self.Matrix3)
            self.Matrix3Box.set_text(np.array2string(self.Matrix3))
            self.ResultBox.set_text("")
        except (SyntaxError, ValueError,AttributeError,IndexError,ImportError) as e  :
            print(f"Error converting string to NumPy array: {e}")
            self.ResultBox.set_text(f"{self.notice}")
            self.NoticeERORR()
    def setDefaultExpm(self):
        self.Matrix1Box.set_text(spLinalg.a_expm)
    #sinm
    def solveSinm(self):
        try:
            self.addDataMatrix1_2()
            self.matrix3text="Sin(A):"
            self.Matrix3=spLinalg.sinm(self.Matrix1)
            print(self.Matrix3)
            self.Matrix3Box.set_text(np.array2string(self.Matrix3))
            self.ResultBox.set_text("")
        except (SyntaxError, ValueError,AttributeError,IndexError,ImportError) as e  :
            print(f"Error converting string to NumPy array: {e}")
            self.ResultBox.set_text(f"{self.notice}")
            self.NoticeERORR()
    def setDefaultSinm(self):
        self.Matrix1Box.set_text(spLinalg.a_sinm)
    #cosm
    def solveCosm(self):
        try:
            self.addDataMatrix1_2()
            self.matrix3text="Cos(A):"
            self.Matrix3=spLinalg.cosm(self.Matrix1)
            print(self.Matrix3)
            self.Matrix3Box.set_text(np.array2string(self.Matrix3))
            self.ResultBox.set_text("")
        except (SyntaxError, ValueError,AttributeError,IndexError,ImportError) as e  :
            print(f"Error converting string to NumPy array: {e}")
            self.ResultBox.set_text(f"{self.notice}")
            self.NoticeERORR()
    def setDefaultCosm(self):
        self.Matrix1Box.set_text(spLinalg.a_cosm)
    def showMatrixA(self):
        self.Matrix_show_text="Matrix A:"
        self.addDataMatrix1_2()
        self.Matrix_show=self.Matrix1
        
        if self.checkAllowDrawImage():
            self.ResultBox.set_text(str(self.Matrix1))
            self.draw_graph()
        else : self.ResultBox.set_text("Can not draw matrix! Because it's not square")
    def showMatrixB(self):
        self.Matrix_show_text="Matrix B:"
        self.addDataMatrix1_2()
        self.Matrix_show=self.Matrix2
        
        if self.checkAllowDrawImage():
            self.ResultBox.set_text(str(self.Matrix2))
            self.draw_graph()
        else : self.ResultBox.set_text("Can not draw matrix! Because it's not square")
    def showMatrixC(self):
        self.Matrix_show_text="Matrix C:"
        self.addDataMatrix1_2()
        self.Matrix_show=self.Matrix3
        if self.checkAllowDrawImage():
            self.ResultBox.set_text(str(self.Matrix3))
            self.draw_graph()
        else : self.ResultBox.set_text("Can not draw matrix! Because it's not square")
    def showMatrixAB(self):
        self.Matrix_show_text="Matrix AB:"
        self.addDataMatrix1_2() 
        self.Matrix_show=self.MatrixAB
        if self.checkAllowDrawImage():
            self.ResultBox.set_text(str(self.MatrixAB))
            self.draw_graph()
        else : self.ResultBox.set_text("Can not draw matrix! Because it's not square")
    def checkAllowDrawImage(self):
        if spLinalg.is_square_matrix(self.Matrix_show) : 
            return True
    def draw(self):
        self.running = True
         
        while self.running:
            for event in pg.event.get():
                # Pygame event
                if event.type == pg.USEREVENT:
                    # pygame_gui event
                    if event.user_type==pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element==self.ButtonMatrixA:
                            self.showMatrixA()
                        if event.ui_element==self.ButtonMatrixB:
                            self.showMatrixB()
                        if event.ui_element==self.ButtonMatrixC:
                            self.showMatrixC()
                        if event.ui_element==self.ButtonMatrixAB:
                            self.showMatrixAB()   
                        # ButtonCal
                        if event.ui_element==self.ButtonCal:
                            self.solveCal()
                        #Button Inverse
                        if event.ui_element==self.ButtonInv:
                            self.solveInv()
                        # Button det
                        if event.ui_element==self.ButtonDet:
                            self.solveDet()
                        #Button SOlve a@x=b
                        if event.ui_element==self.ButtonSol:
                            self.solveSol()
                        if event.ui_element==self.defaultSol:
                            self.setDefaultSol()
                        if event.ui_element==self.ButtonSoLu:
                            self.solveSoLu()
                        if event.ui_element==self.defaultSoLu:
                            self.setDefaultSolu()
                        if event.ui_element==self.ButtonSolhBanded:
                            self.solveSolhBanded()
                        if event.ui_element==self.defaultSolhBanded:
                            self.setDefaultSolhBanded()
                        if event.ui_element==self.ButtonLstsq:
                            self.solveLstsq()
                        if event.ui_element ==self.defaultLstsq:
                            self.setDefaultLstsq()
                        if event.ui_element==self.ButtonPinv:
                            self.solvePinv()
                        if event.ui_element==self.defaultPinv:
                            self.setDefaultPinv()
                        if event.ui_element==self.ButtonNorm:
                            self.solveNorm()
                        if event.ui_element==self.defaultNorm:
                            self.setDefaultNorm()
                        if event.ui_element==self.ButtonEig:
                            self.solveEig()
                        if event.ui_element==self.defaultEig:
                            self.setdefaultEig()
                        if event.ui_element==self.ButtonSvd:
                            self.solveSvd()
                        if event.ui_element==self.defaultSvd:
                            self.setdefaultSvd()
                        if event.ui_element==self.ButtonDiagsvd:
                            self.solveDiagsvd()
                        if event.ui_element==self.defaultDiagsvd:
                            self.setdefaultSvd()
                        if event.ui_element==self.ButtonEigvals:
                            self.solveEigvals()
                        if event.ui_element==self.defaultEigvals:
                            self.setdefaultEigvals()
                        if event.ui_element==self.ButtonSolTri:
                            self.solveSolTri()
                        if event.ui_element==self.defaultSolTri:
                            self.setDefaultSolTri()
                        if event.ui_element==self.ButtonExpm:
                            self.solveExpm()
                        if event.ui_element==self.defaultExpm:
                            self.setDefaultExpm()
                        if event.ui_element==self.ButtonSinm:
                            self.solveSinm()
                        if event.ui_element==self.defaultSinm:
                            self.setDefaultSinm()
                        if event.ui_element==self.ButtonCosm:
                            self.solveCosm()
                        if event.ui_element==self.defaultCosm:
                            self.setDefaultCosm()
                if event.type == pg.QUIT: 
                    pg.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button for rotation
                        self.rotate = not self.rotate
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:  # Left mouse button released
                        self.rotate = False
                if event.type == MOUSEMOTION:
                    if self.rotate and self.target_x <= event.pos[0]<=self.target_x+self.target_width and self.target_y <= event.pos[1] <=self.target_y+self.target_height:
                        dx, dy = event.rel
                        self.azim += dx
                        self.elev += dy
                        self.ax.view_init(elev=self.elev, azim=self.azim)
                        self.canvas.draw()
                        self.original_surface = pg.image.fromstring(self.canvas.tostring_rgb(), self.canvas.get_width_height(), "RGB")
                        self.matplotlib_surface = pg.transform.scale(self.original_surface, (self.target_width,self.target_height))
                self.MANAGER.process_events(event)
            self.screen.fill((color.Silver))
            self.MANAGER.draw_ui(self.screen)
            # Draw labels
            self.drawtext(self.screen,FONT1,self.matrix1text,color.Blue,5,4)
            self.drawtext(self.screen,FONT2,self.matrix2text,color.Red,305,4)
            self.drawtext(self.screen,FONT3,self.matrix3text,color.Green,590,4)
            self.drawtext(self.screen,FONT1,self.restext,color.Black,5,205)
            self.drawtext(self.screen,FONT3,"standard",color.Navy,1000,220)
            self.drawtext(self.screen,FONT3,self.Matrix_show_text,color.Black,5,380)
            #Draw Image Matrix
            if self.checkAllowDrawImage():
                self.drawImage()
            self.defaultSol.set_image(self.defaultImg)
            self.defaultSoLu.set_image(self.defaultImg)
            self.defaultSolhBanded.set_image(self.defaultImg)
            self.defaultLstsq.set_image(self.defaultImg)
            self.defaultPinv.set_image(self.defaultImg)
            self.defaultNorm.set_image(self.defaultImg)
            self.defaultEig.set_image(self.defaultImg)
            self.defaultSvd.set_image(self.defaultImg)
            self.defaultDiagsvd.set_image(self.defaultImg)
            self.defaultEigvals.set_image(self.defaultImg)
            self.defaultSol.set_image(self.defaultImg)
            self.defaultSol.set_image(self.defaultImg)
            self.defaultSolTri.set_image(self.defaultImg)
            self.defaultExpm.set_image(self.defaultImg)
            self.defaultSinm.set_image(self.defaultImg)
            self.defaultCosm.set_image(self.defaultImg)
            #Draw input boxes
            #Matrix A 5x5
            

            # self.drawBoxInput(self.screen,50,4,30,20)
            #Matrix B 5x5
            # self.drawBoxInput(self.screen,300,4,30,20)
            
            #Draw Ouput boxes
            #Matrix C 5x5
            # self.drawBoxOutput(self.screen,600,4,30,20)
            self.MANAGER.update(self.UI_Refesh_rate)
            pg.display.update()
            self.clock.tick(FPS)
        # self.running = False
    def drawtext(self,screen,font,text,color,x,y):
        text = font.render(text,True,color)
        screen.blit(text,(x,y))
    def drawImage(self):
        self.fig = plt.figure(figsize=(3, 3), dpi=100)  # Decrease the size of the figure
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.x, self.y =np.meshgrid(np.arange(self.Matrix_show.shape[0]), np.arange(self.Matrix_show.shape[1]))
        self.plot_surface = self.ax.plot_surface(self.x,self.y, self.Matrix_show, cmap='plasma', edgecolor='k', linewidth=0.5)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        # Adjust the view angle
        self.ax.view_init(elev=0, azim=0)

        # Display Matplotlib plot on Pygame surface
        self.canvas = FigureCanvasAgg(self.fig)
        
        for i in range(self.Matrix_show.shape[0]):
            for j in range(self.Matrix_show.shape[1]):
                x0, y0, z0 = i, j, self.Matrix_show[i, j]
                # print(f"{x0},{y0},{z0}")
                text = f'({x0}, {y0}, {z0})'
                self.ax.text(x0, y0, z0, text, color='red', fontsize=8, ha='center', va='center',fontweight='bold')
    
        self.ax.scatter(self.x, self.y, self.Matrix_show, c='green', s=50, label='Vertices')

        
        self.canvas.draw()
        self.matplotlib_surface = pg.transform.scale(self.original_surface, (self.target_width,self.target_height))
        self.screen.blit(self.matplotlib_surface, (self.target_x, self.target_y))
    def draw_graph(self):
       # Clear previous plot
        self.ax.cla()
        # Draw 3D surface plot
        self.x,self.y = np.meshgrid(np.arange(self.Matrix_show.shape[0]), np.arange(self.Matrix_show.shape[1]))
        self.ax.plot_surface(self.x, self.y, self.Matrix_show, cmap='viridis', edgecolor='k', linewidth=0.5)
        # Set labels
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.ax.scatter(self.x, self.y, self.Matrix_show, c='green', s=50, label='Vertices')
        # Adjust the view angle
        self.ax.view_init(elev=0, azim=0)
view = DisplayViewLinalgBasic()
view.draw() 
                 
                 