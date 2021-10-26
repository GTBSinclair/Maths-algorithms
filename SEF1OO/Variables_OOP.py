import numpy as np

class Variables:

    squared = 0
    addition2 = 0
    subtraction2 = 0
    power2 = 0
    multiply2 = 0
    divide2 = 0
    
    addition3 = []
    subtraction3 = []
    power3 = []
    multiply3 = []
    divide3 = []
    
    A_div = []
    A_mult = []
    A_add = []
    A_sub = []
    A_pow = []

    results = []
    closest_results = []

    list1 = np.arange(-200,201,1).tolist()



ADD = Variables.A_add
SUB = Variables.A_sub
PW = Variables.A_pow
MUL = Variables.A_mult
DIV = Variables.A_div

SQR = Variables.squared
ADD2 = Variables.addition2
SUB2 = Variables.subtraction2
PW2 = Variables.power2
MUL2 = Variables.multiply2
DIV2 = Variables.divide2

ADD3 = Variables.addition3
SUB3 = Variables.subtraction3
PW3 = Variables.power3
MUL3 = Variables.multiply3
DIV3 = Variables.divide3

Rst = Variables.results
Cl_Rst = Variables.closest_results
