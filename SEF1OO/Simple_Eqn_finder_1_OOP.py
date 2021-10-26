from Variables_OOP import *

class Entries():

    def generate_inputs():

        # Give at least 5 inputs to avoid some problems in the code. 
        # E.g. Due to the loop length being the no. of inputs - 2, 
        # the power element may show up for no. of inputs < 5 even when it's the wrong answer

        x = 0
        A = []
        for i in range(int(input("Enter number of inputs:\n"))):
            x += 1
            s = (float(input("input" + str(x) + " : ")))
            A.append(s)
        return A


    def check_weights():
        
        print(SQR, ADD2, SUB2, PW2, MUL2, DIV2, '\n')

        if SUB2 == 0:
            print("No subtraction element\n")
            SUB3 = [0]

        if ADD2 == 0:
            print("No addition element\n")
            ADD3 = [0]

        if PW2 == 0:
            print("No power element\n")
            PW3 = [0]
            
        if MUL2 == 0:
            print("No multiplying element\n")
            MUL3 = [0]
            
        if DIV2 == 0:
            print("No dividing element\n")
            DIV3 = [0]


    def update(name):
        global SQR, ADD2, SUB2, PW2, MUL2, DIV2 # Need this line otherwise the variables will be reassigned as local
        if name == 'squared':
            SQR += 1
        elif name == 'addition2':
            ADD2 += 1
        elif name == 'subtraction2':
            SUB2 += 1
        elif name == 'power2':
            PW2 += 1
        elif name == 'multiply2':
            MUL2 += 1
        elif name == 'divide2':
            DIV2 += 1


    def print(name):

        if name == 'SQR':
            print("The eqn. is x[i+1]=x[i]^2")

        if name == 'ADD3':
            print("The eqn. is x[i+1]=x[i]+" + str(ADD3[0]))

        if name == 'SUB3':
            print("The eqn. is x[i+1]=x[i]" + str(SUB3[0]))

        if name == 'POW3':
            print("The eqn. is x[i+1]=x[i]^" + str(PW3[0]))

        if name == 'MUL3':
            print("The eqn. is x[i+1]=" + str(MUL3[0]) + "*x[i]")

        if name == 'DIV3':
            print("The eqn is x[i+1]=x[i]/(" + str(DIV3[0]) + ")")


    
