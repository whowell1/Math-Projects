##Project by Wren Howell. I hereby declare that this work is my own

import numpy as np 
import math 
from numpy import linalg as LA

#vector a 
a = np.array([3,-2,4])

#vector b
b = np.array([0,1,-3])

#vector c
c = np.array([-2,4,5])


#vector d my array
d = np.array([7,4,4])

#scalar e 
e =-2

# scalar f
f = 1


# cross product between vector a and d 
print "The solution to Question 1 is " , np.cross(a,d)

# cross product between vector  and a 
print "The solution to Question 2 is " , np.cross(d,a)


# cross product between vector a  (vector d - scalar f vector c)  
# temporary variable to store the vector (b - scalar e vector c) 
tempOne = (d-(f*c))

print "The solution to Question 3 is " , np.cross(a,tempOne)

# cross product between vector a cross (vec b cross vector c )
# temporary variable to store cross product of vec b cross c 
tempTwo = np.cross(b,c)
print "The solution to Question 4 is "  ,  np.cross(a,tempTwo)

#Vector b (vector a dot product vector c) + vector c (dot product vector a vector b )
tempVec = np.dot(a,c)
tempVecTwo = np.dot(a,b)

print "The solution to Question 5 is " ,  b*tempVec + c*tempVecTwo

#Area of triangle with vertices p (-2,3,1) q (1,1,2) and r (4,2,-3)
vectorP=np.array([-2,3,1])
vectorQ= np.array([1,1,2])
vectorR= np.array([4,2,-3])
vectorPQ = vectorQ-vectorP
vectorPR = vectorR- vectorP


print "The solution to Question 6 is "  , 0.5*np.cross(vectorPQ,vectorPR)

##Are vector b and c parallel 
 np.sin(np.cross(b,c)/(LA.norm(a) * LA.norm(b))
print "solution to number 7 is: Since the cross product of vector b and vector c is not zero, these are not paralle vectors"


#Volume of parallelpided formed by vector a,b anc c
print "The solution to Question 8 is " ,  LA.det([a,b,c])

#Volume of parallelpided formed by vector a,b anc d
print "The solution to Question 9a is " ,  LA.det([a,b,d])

# cross product between vector c and d 
print "The solution to Question 9b is "  ,  np.cross(c,d)


##Question 1
## The advantage of storing the vector and scalrs into variables is that there is no need to retype the vectors that are using used. 
## This way makes code more readable and more efficent. 
##Question 2 
##Major difference between the two software packages is python does not give exact answers and Mathematica does. In python, this makes sense because many times in application 
## programming, the programmer is not looking for exact answers and approximate answers are good enough. 
## Both software packages have functions that can perform mathematical functions, even though Mathematica calculating scalar projection and vector projection are more straight forward than in python.


