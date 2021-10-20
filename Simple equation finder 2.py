#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'notebook')
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
import numpy as np
import cmath
import math
import time


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


# Possibly need a ML algorith here to narrow down the possible equations by looking at the graph of the inputs


# In[ ]:


def divide(y,x):
    return y/x
def add(y,x):
    return y+x
def multiply(y,x):
    return y*x
def power(y,x):
    return y**x


def print_this(A1,A2,L1,F):
    if F.__name__ == 'divide':
        print('x[i+1]=x[i]/'+str(L1))
    elif F.__name__ == 'add' and L1>-1:
        print('x[i+1]=x[i]+'+str(L1))
    elif F.__name__ == 'add' and L1<0:
            print('x[i+1]=x[i]'+str(L1))
    elif F.__name__ == 'multiply':
        print('x[i+1]='+str(L1)+'*x[i]')
    elif F.__name__ == 'power':
        print('x[i+1]=x[i]^'+str(L1))
    else:
        print('none')
    return print(str(A1)+ '  ' + str(A2) + '\n')


functions = [divide,add,multiply,power]
list1 = np.arange(-200,201,1).tolist()
Ad = []
B1 = []
B2 = []
B3 = []
B4 = []


# In[ ]:


# To be able to place A[i] in all the available places in the eqn., make a list of the type 
# [A[i],functions[A[i], functions[A[i],etc.]]] and then find a way to pass A[i] across all the places

print('A = ' + str(A) + '\n')

for i in range(p):
    for j in range(len(functions)):
        for z in range(len(list1)):
            try:
                if A[i+1] == functions[j](A[i],list1[z]) and A[i+2] == functions[j](A[i+1],list1[z]):
                    print_this(A[i],A[i+1],list1[z],functions[j])
                    Ad.append(list1[z])
            except ZeroDivisionError as error:
                break
            except IndexError as error:
                break
            except OverflowError as oe:
                break

G1 = 0
if Ad == []:
    for i in range(p):
        for z in range(len(list1)):
            try:
                B1.append([A[i],list1[z]])
                B2.append([A[i+1],list1[z]])
            except ZeroDivisionError as error:
                break
            except IndexError as error:
                break
            except OverflowError as oe:
                break
                                            
# Estimated computational time for ~ 61 million results is ~ 90 minutes


# In[ ]:


print(B2)


# In[ ]:


a = len(functions)
b = len(list1)
c = len(B1)
print(2*2*a*b*c)


# In[ ]:


for b in range(2):
    for u in range(2):
        for j in range(len(functions)):
            for v in range(len(list1)):
                for l in range(len(B1)): # --------- Up to here it is already 10,297,680 combinations to go through
                    try:
                        B3.append([functions[j](B1[l][b],B1[l][u]),list1[v]])
                        B4.append([functions[j](B2[l][b],B2[l][u]),list1[v]])
                        G1 += 1
                        print(str('{0:.2g}'.format((G1/4722924.8)*100)), end='\r')
                    except ZeroDivisionError as error:
                        break
                    except IndexError as error:
                        break
                    except OverflowError as oe:
                        break


# In[ ]:


print(len(B3),'\n',len(B4))


# In[ ]:


for i in range(len(B4)):
    for j in range(len(B4)):
        try:
            if B4[i] == B4[j]: # ************ NOT POSSIBLE because there are too many duplicate results to remove. Fix the code above and retry
                print(B4[j])
                B4.remove(B4[j])
        except IndexError as error:
            break


# In[ ]:


# ************ Make a function of if statement that deletes all duplicate results
print(len(B4),len(B3))


# In[ ]:


for o in range(len(functions)):
    for h in range(2):
        for m in range(2):
            for i in range(p):
                for k in range(len(B3)):
                    try:
                        if A[i+1] == functions[o](B3[k][h],B3[k][m]): # and A[i+2] == functions[o](B4[0][h],B4[0][m]):
                            # Output from here will be ~174 trillion results (unless duplicates are removed - however this could result in the loss of the true equation)
                            # 174 trillion results would take 100+ million minutes (250 years) to compute in python, 300+ (230 days) thousand minutes in C++
                            # Therefore I need to implement a ML neural net to decrease the number of results and keep the computing fast - i.e. simple trend detection CNN looking at the graph of the inputs
                            print(str(A[i]) + '  ' + str(A[i+1])  + '  ' + functions[j].__name__ + '  ' + str(list1[z]) + '  ' + functions[o].__name__ + '  ' + str(list1[v]) + '\n')
                    except ZeroDivisionError as error:
                        break
                    except IndexError as error:
                        break
                    except OverflowError as oe:
                        break


# In[ ]:


# ********* One implementation of machine learning is to plot the dataset using 'y' as x[i+1] and 'x' as x[i]
          # and run the neural net with filters from graphs set as x^2, x^3, x+2, etc.
          # This would speed up the process significantly


# def fermi(E: float,T: float) -> float:
#     y2 = (E**2)+(1/T)
#     return y2

# # Create figure and add axes
# fig = plt.figure(figsize=(6, 4))
# ax = fig.add_subplot(111)

# # ************************************** FIRST figure out the advanced equation trial and error method 
#                                        # and then work out the animation.
    
# # Temperature values
# T = np.linspace(10, 100, 10)

# # Create variable reference to plot
# f_d, = ax.plot([], [], linewidth=2.5)


# # Set axes labels
# ax.set_xlabel('x axis')
# ax.set_ylabel('y axis')

# # Animation function
# def animate(i):
#     x = np.linspace(0, 1, 100)
#     if time.time()> 5:
#         y = fermi(x, T[i])
#     elif time.time()<5: # Try to improve this so that the graph will be plotted for all the trial and error equations. 
#                         # Maybe requires for loops to run consecutevily?
#         y = x*(1/T[i])
#     f_d.set_data(x, y)
    

# # Create animation
# ani = FuncAnimation(fig, animate, frames=range(len(T)), interval=200, repeat=True)

# # Ensure the entire plot is visible
# fig.tight_layout()
# plt.show()


# In[ ]:


# from numpy import sin, cos
# import numpy as np
# import matplotlib.pyplot as plt
# import scipy.integrate as integrate
# import matplotlib.animation as animation

# G = 9.8  # acceleration due to gravity, in m/s^2
# L1 = 1.0  # length of pendulum 1 in m
# L2 = 1.0  # length of pendulum 2 in m
# M1 = 1.0  # mass of pendulum 1 in kg
# M2 = 1.0  # mass of pendulum 2 in kg


# def derivs(state, t):

#     dydx = np.zeros_like(state)
#     dydx[0] = state[1]

#     del_ = state[2] - state[0]
#     den1 = (M1 + M2)*L1 - M2*L1*cos(del_)*cos(del_)
#     dydx[1] = (M2*L1*state[1]*state[1]*sin(del_)*cos(del_) +
#                M2*G*sin(state[2])*cos(del_) +
#                M2*L2*state[3]*state[3]*sin(del_) -
#                (M1 + M2)*G*sin(state[0]))/den1

#     dydx[2] = state[3]

#     den2 = (L2/L1)*den1
#     dydx[3] = (-M2*L2*state[3]*state[3]*sin(del_)*cos(del_) +
#                (M1 + M2)*G*sin(state[0])*cos(del_) -
#                (M1 + M2)*L1*state[1]*state[1]*sin(del_) -
#                (M1 + M2)*G*sin(state[2]))/den2

#     return dydx

# # create a time array from 0..100 sampled at 0.05 second steps
# dt = 0.05
# t = np.arange(0.0, 20, dt)

# # th1 and th2 are the initial angles (degrees)
# # w10 and w20 are the initial angular velocities (degrees per second)
# th1 = 120.0
# w1 = 0.0
# th2 = -10.0
# w2 = 0.0

# # initial state
# state = np.radians([th1, w1, th2, w2])

# # integrate your ODE using scipy.integrate.
# y = integrate.odeint(derivs, state, t)

# x1 = L1*sin(y[:, 0])
# y1 = -L1*cos(y[:, 0])

# x2 = L2*sin(y[:, 2]) + x1
# y2 = -L2*cos(y[:, 2]) + y1

# fig = plt.figure()
# ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
# ax.set_aspect('equal')
# ax.grid()

# line, = ax.plot([], [], 'o-', lw=2)
# time_template = 'time = %.1fs'
# time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


# def init():
#     line.set_data([], [])
#     time_text.set_text('')
#     return line, time_text


# def animate(i):
#     thisx = [0, x1[i], x2[i]]
#     thisy = [0, y1[i], y2[i]]

#     line.set_data(thisx, thisy)
#     time_text.set_text(time_template % (i*dt))
#     return line, time_text

# ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)),
#                               interval=25, blit=True, init_func=init)

# # ani.save('double_pendulum.mp4', fps=15)
# plt.show()


# In[ ]:




