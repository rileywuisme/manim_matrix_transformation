from manim import *
import numpy as np

row1 = [2, 1]
row2 = [1, 1]

class Matrix(LinearTransformationScene):
    def __init__(self):
                LinearTransformationScene.__init__(
                    self, 
                    show_coordinates=True, 
                    leave_ghost_vectors=True, 
                    show_basis_vectors=True, 
                )
        
    def construct(self):

        matrix = [row1, row2]

        matrix_tex = MathTex(
            fr"A = \begin{{bmatrix}} {row1[0]} & {row1[1]} \\ {row2[0]} & {row2[1]} \end{{bmatrix}}"
        ).to_edge(UL).add_background_rectangle()

        unit_square = self.get_unit_square()
        text = always_redraw(lambda : Tex("Det(A)").set(width=0.7).move_to(unit_square.get_center()))

        vect = self.get_vector([1, 1], color = PURPLE)

        self.add_transformable_mobject(vect, unit_square)
        self.add_background_mobject(matrix_tex, text)
        self.apply_matrix(matrix)

        self.wait(3)