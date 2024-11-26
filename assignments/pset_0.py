import math
import numpy
import pylab

x = float(input("Enter number x: "))
y = float(input("Enter number y: "))
print(f"x**y = {x**y}")
print(f"log(x) = {math.log2(x)}")
print(f"log(x) in numpy = {numpy.log2(x)}")
print(f"log(x) in pylab = {pylab.log2(x)}")