##Project by Wren Howell. I hereby declare that this work is my own
# Dot Product 


import numpy as np 
import math 
from numpy import linalg as LA

#vector a 
a = np.array([-1,4,-3])

#vector b
b = np.array([1,-2,-2])

#vector c
c = np.array([0,-1,-1])


#vector d my array
d = np.array([7,4,4])

#scalar e 
e =2

# scalar f
f = -1


# dot product between vector a and b 
print "The solution to Question 1 is " , np.dot(a,b)

# dot product between vector b and a 
print "The solution to Question 2 is " , np.dot(b,a)


# dot product between vector a  (b - scalar e vector c)  
# temporay variable to store the vector (b - scalar e vector c) 
temp = (b- e*c)
print "The solution to Question 3 is " , np.dot(a,temp)

## angle between vectors a and d 
print "The solution to Question 4 is "  ,  math.acos(np.dot(a,d)/(LA.norm(a) * LA.norm(d)))

##angle between vectors b and d 
print "The solution to Question 5 is "  ,  math.acos(np.dot(b,d)/(LA.norm(b) * LA.norm(d)))

##angle between vectors b and d 
print "The solution to Question 6 is "  ,  math.degrees(math.acos(np.dot(b,d)/(LA.norm(b) * LA.norm(d))))

##angle between vectors b and d 
print "The angle to Question 7 is " ,  math.acos(np.dot(a,c)/(LA.norm(a) * LA.norm(c)))
print "So, therefore, the angles are not orthogonal because the angle does not equal 0"



#scalar projection of d onto a 
print "The solution to Question 8 is " , np.dot(d,a)/LA.norm(a)  

#scalar projection of a onto d 
print "The solution to Question 9 is " , np.dot(a,d)/LA.norm(d)

#vector projection of d onto a 
print "The solution to Question 10 is " , np.dot(d,a)/LA.norm(a) **2*a 

#vector projection of a onto d 
print "The solution to Question 11 is " , np.dot(a,d)/LA.norm(d) **2*d 



#scalar projection of c onto a 
print "The solution to Question 12a is " , np.dot(c,a)/LA.norm(a)



#scalar projection of a onto c 
print "The solution to Question 12b is " , np.dot(a,c)/LA.norm(c)



 
##Question 1
## The advantage of storing the vector and scalrs into variables is that there is no need to retype the vectors that are using used. 
## This way makes code more readable and more efficent. 
##Question 2 
##Major difference between the two software packages is python does not give exact answers and Mathematica does. In python, this makes sense because many times in application 
## programming, the programmer is not looking for exact answers and approximate answers are good enough. 
## Both software packages have functions that can perform mathematical functions, in this case, dot product, even though Mathematica calculating scalar projection and vector projection are more straight forward than in python.


print "---------------------------------------------------end of Technology 3 ----------------------------------------------------------"

## Cross Product 

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
print tempOne
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
areaOfTriangle =  0.5*LA.norm(np.cross(vectorPQ,vectorPR)) 

print "The solution to Question 6 is " +  repr(areaOfTriangle)+  " units long" 

product= np.cross(b,c) /  (LA.norm(b) * LA.norm(c))




##Are vector b and c parallel 
#Stores the cross product between vectors b and vectors c 


print "solution to number 7 is: Since the cross product of vector b and vector c " +  repr(product) + " and not zero, lines are not parallel"

#Volume of parallelpided formed by vector a,b anc c
# stores the volume of a parallelpipid as a string
volumeOne =   LA.det([a,b,c])
print "The solution to Question 8 is " , volumeOne

#Volume of parallelpided formed by vector a,b anc d
# stores the volume of a parallelpipid as a string
volumeTwo = LA.det([a,b,d])#
print "The solution to Question 9a is " , volumeTwo
# cross product between vector c and d 
print "The solution to Question 9b is "  ,  np.cross(c,d)


##Question 1
## The advantage of storing the vector and scalrs into variables is that there is no need to retype the vectors that are using used. 
## This way makes code more readable and more efficent. 
##Question 2 
##Major difference between the two software packages is python does not give exact answers and Mathematica does. In python, this makes sense because many times in application 
## programming, the programmer is not looking for exact answers and approximate answers are good enough. By default, python has more significant figures than Mathmatica. However, there is a slight problem when using the repr function in python. 
# The repr function in python returns the 'offical' representation of how the object is stored in memory. When the repr function was used on the volues of the parallelpipids,
# the resulting answer were 47.000000000000014 and  61.99999999999995 , which are close to 47 and 62. To round to the nearest integer, the truncate method was used, but there was 
# a error stated that nump.py library object has no truncate attributes. Alternative methods such as math.floor and math.round were used, but type errors were given .Therefore, it can be concluded that the numpy library has its own method that rounds integers. To counter act this problem
# a the volumes of the parallelpipids were converted into a string. 


