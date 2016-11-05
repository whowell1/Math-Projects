##Project by Wren Howell. I hereby declare that this work is my own

import numpy as np 
from math import sqrt
from numpy import linalg as LA

#vector a 
a = np.array([3,-2,5])

#vector b
b = np.array([-2,-1,2])

#vector c
c = np.array([2,0,-3])


#vector d my array
d = np.array([7,4,4])

#scalar e 
e =2

# scalar f
f = -1


# vector a - vector b
print "The solution to Question 1 is " , a-b


# vector a + vector b - scalere * vectorc
print "The solution to Question 2 is " , a+b -e*c

# vector a - (vector b - scaler e vectorc)
print "The solution to Question 3 is " , a-(b-e*c)

# scalar e * scalar f (vector b + vector d)
print "The solution to Question 4 is " , e*f *(b+d)

# magnitude of vector d
print   "The solution to Question 5 is " ,  LA.norm(d)

# mangnitude of vector -d
print "The solution to Question 6 is " , LA.norm(-d)

#magnitude of scalar f multiplied by vector - vector 
print "The solution to number 7 is of" , LA.norm(f*c -a)

#vector c divded by magnitude of c 
answerToNumber8 = (c/LA.norm(c))
print "The solution to Question 8 is " , answerToNumber8

#magnitude of vector c divided by magnitude of vector c
normOfNumberSeven = LA.norm(answerToNumber8)
print "The solution to Question 9 is " , normOfNumberSeven



#magnitude of vector = sqrt( (x1**2) + (y1**2) + (z1 **2))
#15 = sqrt (-1 **2) + (g**2) + (3**2)
# 15*15 = (1+9+g**2)
#225 = 10 +g**2
#225-10 = g**2
#215 = g**2
#g = sqrt of 215
print "the solution to number 10 is square root of 215"


## Adding vectors a and d multiplied by a scalar d
print "The solution to number 11 is" , (a+d)*e

##Question 1
## The advantage of storing the vector and scalrs into variables is that there is no need to retype the vectors that are using used. 
## This way makes code more readable and more efficent. 
##Question 2 
##Major difference between the two software packages is python does not give exact answers and Mathematica does. In python, this makes sense because many times in application 
## programming, the programmer is not looking for exact answers and approximate answers are good enough. 
## Both software packages have functions that can perform mathematical functions. 


