#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import cmath


# In[2]:


# Polynomial of the type: x^2 + 5x + 6

try:
    input0 = int(input("Warning: this is a simple second order polynomial solver so the x^2 value can only be 1. \ninput0: "))
    input1 = int(input("input1: "))

    B = np.arange(-100,100,1)
    C = np.arange(-100,100,1) # Range of values can cause problems to find all the solutions if out of range

finally:
    #print("The result is " + str(input0) + " x " + str(input1) + " = " + str(A) + "\n")
    
    B = B.tolist()
    C = C.tolist()
    #print("B = " + str(B))
    #print("C = " + str(C))


# In[3]:


p = []
p2 = []

# This section multiplies out and adds each number in the two arrays 'B' and 'C' with the other 
# and stores the results and the two numbers used in a new array

for i in range(len(B)):
    for j in range(len(C)):
        p.append([(B[i]*C[j]),(B[i]+C[j]),B[i],C[j]]) # The format here is "factor 1 * factor 2, factor 1 + factor 2, factor 1, factor 2"


# In[4]:


#This section tries to filter the results from the nested for loop above first - this is the factoring method.
#If the the factoring method doesn't work it finds the solutions with the quadratic formula.
#The quadratic formula method uses the 'cmath' function which supports complex numbers.
#The 'round' function eliminates the imaginary symbol so its added back by multiplying by an imaginary number, 1j
# p2 is defined above

for i in range(len(p)):
    for j in range(2):
        if p[i] not in p2 and p[i][0] == input1 and p[i][1] == input0:
            p2.append(p[i])
        else:
            Result1 = (-input0 + cmath.sqrt(((input0)**2)-(4*1*input1)))/(2*1)
            Result2 = (-input0 - cmath.sqrt(((input0)**2)-(4*1*input1)))/(2*1)
            Result1 = Result1.real + (round(Result1.imag, 2)*1j)
            Result2 = Result2.real + (round(Result2.imag, 2)*1j)

#print(str(Result1) + '  ' + str(Result2))

# This section is to remove any imaginary number which is 0 and correct the sign of the real part of the solution if its been changed by the "abs" function

if Result1.imag == 0:
    Result1 = abs(Result1)*((Result1.real)/abs(Result1.real))
if Result2.imag == 0:
    Result2 = abs(Result2)*((Result2.real)/abs(Result2.real))


# In[5]:


# This section prints the results for x when the polynomial is set to equal zero
if len(p2) == 0:
    print("Result1 is: " + str(Result1) + '\n' + "Result2 is: " + str(Result2) + '\n' + "By the method of the quadratic formula")
else:
    Result_1 = p2[0][2]*(-1)
    Result_2 = p2[1][2]*(-1)
    print("Result1 is: " + str(Result_1) + '\n' + "Result2 is: " + str(Result_2) + '\n' + "By the method of factoring")


# In[6]:


# This section plots the polynomial and the y=0 horizontal line which is used to clearly see the intersections at y=0

x = np.linspace((Result2.real-20),(Result1.real+20),100)
y = (x**2)+(input0*x)+input1
plt.plot(x,y, '-r', label = 'y=(x^2)+('+str(input0)+')x+('+str(input1)+')')
plt.axhline(color='b')
plt.margins(0.1,0.2)
plt.title('Graph of the polynomial eqn')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper center')
plt.grid()
plt.show()


# In[ ]:


#Improvement to the factoring method:
# - Look at Samsung Notes to get the adjusted eqns. to account for x sqared terms higher than 1

