#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
import cmath


# In[ ]:


x = 0
p = int(input("Enter number of inputs:\n")) # Give at least 5 inputs to avoid some problems in the code. 
                                            # E.g. Due to the loop length being the no. of inputs - 2, 
                                            # the power element may show up for no. of inputs < 5 even when it's the wrong answer
A = []

for i in range(p):
    x += 1
    s = (float(input("input" + str(x) + " : ")))
    A.append(s)
print('\n' + str(A))


# In[ ]:


list1 = np.arange(-200,201,1).tolist()

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


# In[ ]:


for i in range(p-1): # This means that the last two inputs can be ignored as they will be missed by the algorithm
    if A[i]**2 == A[i+1] and A[i+1]**2 == A[i+2]:
        squared += 1
    for j in range(int(len(list1)/2)):
        try:
            if A[i]+list1[201:401:1][j] == A[i+1] and A[i]+(2*list1[201:401:1][j]) == A[i+2]: # Is A[i]+x = A[i+1] && is A[i+1]+x = A[i+2] (written differently in the script)
                addition2 += 1
                addition3.append(list1[201:401:1][j])
                for p in range(len(addition3)):
                        A_add.append([A[i],A[i+1]])
            elif A[i]+list1[0:200:1][j] == A[i+1] and A[i]+(2*list1[0:200:1][j]) == A[i+2]: # Adding the A[i+2] verification means that this algorithm is looking for linear relationships, and not non-linear relationships
                subtraction2 += 1
                subtraction3.append(list1[0:200:1][j])
                for p in range(len(subtraction3)):
                        A_sub.append([A[i],A[i+1]])
            elif A[i]/list1[0:200:1][j] == A[i+1] and A[i+1]/list1[0:200:1][j] == A[i+2]:
                    divide2 += 1
                    divide3.append(list1[0:200:1][j])
                    for p in range(len(divide3)):
                        A_div.append([A[i],A[i+1]])
            elif A[i]/list1[201:401:1][j] == A[i+1] and A[i+1]/list1[201:401:1][j] == A[i+2]:
                    divide2 += 1
                    divide3.append(list1[201:401:1][j])
                    for p in range(len(divide3)):
                        A_div.append([A[i],A[i+1]])
            elif A[i] != 0 and A[i]**list1[0:200:1][j] == A[i+1] and A[i+1]**list1[0:200:1][j] == A[i+2]:
                power2 += 1
                power3.append(list1[0:200:1][j])
                for p in range(len(power3)):
                    A_pow.append([A[i],A[i+1]])
            elif A[i] != 0 and A[i]**list1[201:401:1][j] == A[i+1] and A[i+1]**list1[201:401:1][j] == A[i+2]:
                power2 += 1
                power3.append(list1[201:401:1][j])
                for p in range(len(power3)):
                    A_pow.append([A[i],A[i+1]])
        except IndexError as error:
            break
        except OverflowError as oe:
            power3 = [0]
            break
    for z in range(int(len(list1))):
        try:
            if A[i]*list1[0:401:1][z] == A[i+1] and A[i+1]*list1[0:401:1][z] == A[i+2]:
                multiply2 += 1
                multiply3.append(list1[0:401:1][z])
                for p in range(len(multiply3)):
                    A_mult.append([A[i],A[i+1]])
        except OverflowError as oe:
            power3 = [0]
            break
        except IndexError as error:
            break

print('A = ' + str(A) + "\n")

if subtraction2 == 0:
    print("No subtraction element\n")
    subtraction3 = [0]

if addition2 == 0:
    print("No addition element\n")
    addition3 = [0]

if power2 == 0:
    print("No power element\n")
    power3 = [0]
    
if multiply2 == 0:
    print("No multiplying element\n")
    multiply3 = [0]
    
if divide2 == 0:
    print("No dividing element\n")
    divide3 = [0]
    
    
# ******** Put the equations together here, for the most probable of the above iterate them
#          over a new function to trial and error *********** DO THIS FIRST before the animation

    

if len(A)-2 == squared:
    print("The eqn. is x[i+1]=x[i]^2")
elif len(A)-2 == addition2:
    print("The eqn. is x[i+1]=x[i]+" + str(addition3[0]))
elif len(A)-2 == subtraction2:
    print("The eqn. is x[i+1]=x[i]" + str(subtraction3[0]))
elif len(A)-2 == power2:
    print("The eqn. is x[i+1]=x[i]^" + str(power3[0]))
elif len(A)-2 == multiply2:
    print("The eqn. is x[i+1]=" + str(multiply3[0]) + "*x[i]")
elif len(A)-2 == divide2:
    print("The eqn is x[i+1]=x[i]/(" + str(divide3[0]) + ")")
else:
    results.append([(squared,"The eqn. is x[i+1]=x[i]^2"),((addition2),"The eqn. is x[i+1]=x[i]+" 
    + str(addition3)),((subtraction2),"The eqn. is x[i+1]=x[i]" + str(subtraction3)),
    ((power2),"The eqn. is x[i+1]=x[i]^" + str(power3)),((multiply2),"The eqn. is x[i+1]=" + str(multiply3) + "*x[i]"),
    ((divide2),"The eqn. is x[i+1]=x[i]/(" + str(divide3) + ")")])
    print("The exact equation cannot be found.\n")
    
    for i in range(len(results[0])):
        if results[0][i][0]==(max(results[0])[0]):
            closest_results.append([results[0][i][0],results[0][i][1]])

    print("closest: " + str(closest_results))


#******** CORRECT this to include powers of zero *********


# In[ ]:


# print(A_mult)
# print(A_div)
# print(A_add)
# print(A_pow)
# print(A_sub)

print(subtraction2,addition2,divide2,multiply2,power2,squared)


# In[ ]:


x = np.linspace(min(A)-500, max(A)+100,100) # This whole section can be replaced simply by plotting x[i] on the x-axis and x[i+1] on the y-axis.
                                            # Simply get x[i] and x[i+1] from A.

if subtraction2>addition2&divide2&multiply2&power2&squared:
    y = x-subtraction3[0]
    plt.plot(x,y, '-r', label = 'x[i+1]=x[i]' + str(subtraction3[0]))
elif addition2>subtraction2&divide2&multiply2&power2&squared:
    y = x+addition3[0]
    plt.plot(x,y, '-r', label = 'x[i+1]=x[i]+' + str(addition3[0]))
elif divide2>addition2&subtraction2&multiply2&power2&squared:
    y = x/divide3[0]
    plt.plot(x,y, '-r', label = "x[i+1]=x[i]/(" + str(divide3[0]) + ")")
elif multiply2>addition2&divide2&subtraction2&power2&squared:
    y = x*multiply3[0]
    plt.plot(x,y, '-r', label = "x[i+1]=" + str(multiply3[0]) + "*x[i]")
elif power2>addition2&divide2&multiply2&subtraction2&squared:
    y= x**power3[0]
    plt.plot(x,y, '-r', label = "x[i+1]=x[i]^" + str(power3[0]))
elif squared>addition2&divide2&multiply2&power2&subtraction2:
    y=x**2
    plt.plot(x,y, '-r', label = "x[i+1]=x[i]^2")
    
plt.margins(0.1,0.2) # Try autoscale
plt.title('Graph of the eqn')
plt.xlabel('x [i]')
plt.ylabel('x [i+1]')
plt.legend(loc='upper center')
plt.grid()
plt.show()


# In[ ]:


# # How to update the graph for every equation iteration

# %matplotlib notebook
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# from matplotlib.widgets import Slider
# import numpy as np


# def fermi(E: float, E_f: float, T: float) -> float:
#     k_b = 8.617 * (10**-5) # eV/K
#     return 1/(np.exp((E - E_f)/(k_b * T)) + 1)

# # Create figure and add axes
# fig = plt.figure(figsize=(6, 4))
# ax = fig.add_subplot(111)

# # Get colors from coolwarm colormap
# colors = plt.get_cmap('coolwarm', 10)

# # Temperature values
# T = np.linspace(100, 1000, 10)

# # Create variable reference to plot
# f_d, = ax.plot([], [], linewidth=2.5)

# # Add text annotation and create variable reference
# temp = ax.text(1, 1, '', ha='right', va='top', fontsize=24)

# # Set axes labels
# ax.set_xlabel('Energy (eV)')
# ax.set_ylabel('Fraction')

# # Animation function
# def animate(i):
#     x = np.linspace(0, 1, 100)
#     y = fermi(x, 0.5, T[i])
#     f_d.set_data(x, y)
#     f_d.set_color(colors(i))
#     temp.set_text(str(int(T[i])) + ' K')
#     temp.set_color(colors(i))

# # Create animation
# ani = FuncAnimation(fig, animate, frames=range(len(T)), interval=500, repeat=True)

# # Ensure the entire plot is visible
# fig.tight_layout()

# # Save and show animation
# ani.save('AnimatedPlot.gif', writer='imagemagick', fps=2)
# plt.show()


# In[ ]:


# Look at: linear regression examples, classical optimal theory and the quickest language for this is C

