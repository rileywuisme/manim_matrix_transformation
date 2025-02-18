from manim import *
import numpy as np

row1 = [input("Please provide row 1 of a 2x2 matrix:")]
row2 = [input("Please provide row 2 of the 2x2 matrix:")]
matrix = np.array([row1, row2])
det_A = np.linalg.det(matrix)

if det_A == 0:
    print ("Gotta choose a nonsingular 2x2 matrix!")
#exit the program? 

"""
Outline:
* decompose it into elementary operations:
    1. eliminate 21
    2. divide 22 by its reciprocol
    3. eliminate 12
    ! each of the process results in an elementary matrix
* define the four types of transformation: 1, stretch. 2, reflection. 3, sheer. 4, rotation. 
* define the manim operations for each (in a function), and generate the animation based on 
    the transformation. The video should be 5 seconds long, and all types of transformation should
    be executed at the same time. 
"""

# def animation(matrix):
#     class Transformation:
#         def construct(self):