from Variables_OOP import *
from Simple_Eqn_finder_1_OOP import Entries
import numpy as np
import matplotlib.pyplot as plt
import cmath

B = Entries.generate_inputs()

list1 = Variables.list1

for i in range(len(B)-1): # This means that the last input can be ignored as it will be missed by the algorithm
    if B[i]**2 == B[i+1] and B[i+1]**2 == B[i+2]:
        Entries.update('squared')
    for j in range(int(len(list1)/2)):
        try:
            if B[i]+list1[201:401:1][j] == B[i+1] and B[i]+(2*list1[201:401:1][j]) == B[i+2]: # Is B[i]+x = B[i+1] && is B[i+1]+x = B[i+2] (written differently in the script)
                Entries.update('addition2')
                ADD3.append(list1[201:401:1][j])
                for p in range(len(ADD3)):
                        ADD.append([B[i],B[i+1]])
            elif B[i]+list1[0:200:1][j] == B[i+1] and B[i]+(2*list1[0:200:1][j]) == B[i+2]: # Adding the B[i+2] verification means that this algorithm is looking for linear relationships, and not non-linear relationships
                Entries.update('subtraction2')
                SUB3.append(list1[0:200:1][j])
                for p in range(len(SUB3)):
                        SUB.append([B[i],B[i+1]])
            elif B[i]/list1[0:200:1][j] == B[i+1] and B[i+1]/list1[0:200:1][j] == B[i+2]:
                    Entries.update('divide2')
                    DIV3.append(list1[0:200:1][j])
                    for p in range(len(DIV3)):
                        DIV.append([B[i],B[i+1]])
            elif B[i]/list1[201:401:1][j] == B[i+1] and B[i+1]/list1[201:401:1][j] == B[i+2]:
                    Entries.update('divide2')
                    DIV3.append(list1[201:401:1][j])
                    for p in range(len(DIV3)):
                        DIV.append([B[i],B[i+1]])
            elif B[i] != 0 and B[i]**list1[0:200:1][j] == B[i+1] and B[i+1]**list1[0:200:1][j] == B[i+2]:
                Entries.update('power2')
                PW3.append(list1[0:200:1][j])
                for p in range(len(PW3)):
                    PW.append([B[i],B[i+1]])
            elif B[i] != 0 and B[i]**list1[201:401:1][j] == B[i+1] and B[i+1]**list1[201:401:1][j] == B[i+2]:
                Entries.update('power2')
                power3.append(list1[201:401:1][j])
                for p in range(len(PW3)):
                    PW.append([B[i],B[i+1]])
        except IndexError as error:
            break
        except OverflowError as oe:
            power3 = [0]
            break
    for z in range(int(len(list1))):
        try:
            if B[i]*list1[0:401:1][z] == B[i+1] and B[i+1]*list1[0:401:1][z] == B[i+2]:
                Entries.update('multiply2')
                MUL3.append(list1[0:401:1][z])
                for p in range(len(MUL3)):
                    MUL.append([B[i],B[i+1]])
        except OverflowError as oe:
            PW3 = [0]
            break
        except IndexError as error:
            break

print('A = ' + str(B) + "\n")

Entries.check_weights()

from Simple_Eqn_finder_1_OOP import SQR,ADD2,SUB2,PW2,MUL2,DIV2 # This line is needed as these variables are set global in 
                                                                     # the 'update' function in Simple_Eqn_finder_1_OOP.py
                                                                     # and therefore the same variables in Variables.py are not updated
if len(B)-2 == SQR:
    Entries.print('SQR')
elif len(B)-2 == ADD2:
    Entries.print('ADD3')
elif len(B)-2 == SUB2:
    Entries.print('SUB3')
elif len(B)-2 == PW2:
    Entries.print('POW3')
elif len(B)-2 == MUL2:
    Entries.print('MUL3')
elif len(B)-2 == DIV2:
    Entries.print('DIV3')
else:
    Rst.append([(SQR,"The eqn. is x[i+1]=x[i]^2"),((ADD2),"The eqn. is x[i+1]=x[i]+" 
    + str(ADD3)),((SUB2),"The eqn. is x[i+1]=x[i]" + str(SUB3)),
    ((PW2),"The eqn. is x[i+1]=x[i]^" + str(PW3)),((MUL2),"The eqn. is x[i+1]=" + str(MUL3) + "*x[i]"),
    ((DIV2),"The eqn. is x[i+1]=x[i]/(" + str(DIV3) + ")")])
    print("The exact equation cannot be found.\n")
    
    for i in range(len(Rst[0])):
        if Rst[0][i][0]==(max(Rst[0])[0]):
            Cl_Rst.append([Rst[0][i][0],Rst[0][i][1]])

    print("closest: " + str(Cl_Rst))
