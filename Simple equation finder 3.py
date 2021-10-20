#!/usr/bin/env python
# coding: utf-8

# In[9]:


from __future__ import print_function;
import cv2;
import numpy as np;
import matplotlib.pyplot as plt;
import random;
import tqdm;
import keras
import tensorflow;
from tensorflow.keras import layers;
from tensorflow.keras import Model;


# In[8]:


def divide(y,x):
    return y/x
def add(y,x):
    return y+x
def multiply(y,x):
    return y*x
def power(y,x):
    return [y**x]

functions = [divide,add,multiply,power]
list1 = np.arange(-3,3,1).tolist()


# In[27]:


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


# In[30]:


Y = []

for i in range(len(A)-2):
    if A[i+1]-A[i]==A[i+2]-A[i+1]: # Equivalent of addition. This is a basic linear relation but decreases computational time considerably
        Y.append('+'+str(A[i+2]-A[i+1]))
    elif A[i]-A[i+1]==A[i+1]-A[i+2]: # Equivalent of subtraction
        Y.append('-'+str(A[i+1]-A[i+2]))
    elif (A[i+1]/A[i])==A[i] and (A[i+2]/A[i+1])==A[i+1]: # Expand on this method because it should be more efficient that Simple Equation Finder 2
        Y.append('^2')


# In[31]:


print(Y)


# In[ ]:


except ZeroDivisionError as error:
                break
            except IndexError as error:
                break
            except OverflowError as oe:
                break

