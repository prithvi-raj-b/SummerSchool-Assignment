# -*- coding: utf-8 -*-
"""Jawhar_EE20B049.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UGUXuIbdo9DxdRl9lT8NdUaN8tgEjf2d

Code for Problem 1:
"""

import numpy as np
import math

y_hat = np.random.rand(100)
y = np.random.randint(0,2,100)

sum   = 0

for i in range(100):
  a = y_hat[i]
  b = 1-a
  sum = sum + y[i] * math.log2(a) + (1-y[i]) * math.log2(b)
  
O  = -sum/100
print(O)

"""Code for Problem 2:

"""

class dictop:
  def __init__(self,lst,target):
    self.dictionary = {}
    a = 1
    for i in range(len(lst)):
      for j in range(len(lst)):
        if(lst[i] + lst[j] == target):
          self.dictionary[a] = [i,j]
          a = a + 1
  def output(self):
    print(self.dictionary)         

lst  = [15,20,40,10,40,25,50]
target = 60

op = dictop(lst,target)
op.output()