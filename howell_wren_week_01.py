from math import sqrt

#problem 1a
problemOneaValueOfXOne = -2
problemOneaValueOfXTwo = -1
problemOneaValueOfYOne = 3
problemOneaValueOfYTwo=  5
problemOneaTempDistance = ((problemOneaValueOfXTwo - problemOneaValueOfXOne)**2) 
problemOneaTempDistance2 =(problemOneaValueOfYTwo - problemOneaValueOfYOne)**2 
problemOneaAddedDistance = problemOneaTempDistance + problemOneaTempDistance2
print "Distance for problem 1a is Squareroot is %d" %(problemOneaAddedDistance)

#problem 1b
problemOnebValueOfXOne = 4
problemOnebValueOfXTwo = 3
problemOnebValueOfYOne = -2
problemOnebValueOfYTwo=  -3
problemOnebValueOfZOne = -1
problemOnebValueOfZTwo = -2
problemOnebTempDistance = ((problemOnebValueOfXTwo - problemOnebValueOfXOne)**2) 
problemOnebTempDistance2 =(problemOnebValueOfYTwo - problemOnebValueOfYOne)**2 
problemOnebTempDistance3 =(problemOnebValueOfZTwo - problemOnebValueOfZOne)**2 
problemOnebAddedDistance = problemOnebTempDistance + problemOnebTempDistance2 + problemOnebTempDistance3
print "Distance for aa is Squareroot is %d" %(problemOnebAddedDistance)

#problem2a

approxmimateDistanceProblemTwoA = sqrt(problemOneaAddedDistance)
print approxmimateDistanceProblemTwoA



#problem2b
approxmimateDistanceProblemTwoB = sqrt(problemOnebAddedDistance)
print approxmimateDistanceProblemTwoB