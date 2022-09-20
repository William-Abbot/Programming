import Algorithm1 as A1
import Algorithm2 as A2
import Algorithm3 as A3
import Algorithm4 as A4
import numpy as np
import time
import math

#Programming Assignment
#William Abbot
#7/24/2020



fileIn = open("phw_input.txt", "r")
lst = fileIn.readline().split(',')#insert comma-seperated value from file into a list
for i in range(len(lst)):#convert to int
    lst[i] = int(lst[i])

fileIn.close()

result1 = A1.Algorithm_1(lst)
result2 = A2.Algorithm_2(lst)
L = 0
U = len(lst)-1
result3 = A3.MaxSum(lst,L,U)
result4 = A4.Algorithm_4(lst)


print("algorithm-1: " + str(result1) + "; " +
    "algorithm-2: " + str(result2) + "; " +
    "algorithm-3: " + str(result3) + "; " +
    "algorithm-4: " + str(result4) + "; ")
#finished with step 5
print()


nArray = [0]*19
term = 10
for i in range(19):
    nArray[i] = list(np.random.randint(-100,100,term))
    term = 5*(i+1)+10


#calculating run times for each algorithm
A1Time = [0]*19
N = 500
for i in range(len(nArray)):
    t0 = time.time()
    for x in range(N):
        A1.Algorithm_1(nArray[i])
    t1 = time.time()-t0
    
    t0 = time.time()
    for y in range(N):
        A1.Algorithm_1(nArray[i])
    t2 = time.time()-t0
    
    average = (t1+t2)/2
    A1Time[i] = round((average*1000),7)#convert to milliseconds


A2Time = [0]*19

for i in range(len(nArray)):
    t0 = time.time()
    for x in range(N):
        A2.Algorithm_2(nArray[i])
    t1 = time.time()-t0
    
    t0 = time.time()
    for y in range(N):
        A2.Algorithm_2(nArray[i])
    t2 = time.time()-t0
    
    average = (t1+t2)/2
    A2Time[i] = round((average*1000),7)


A3Time = [0]*19

for i in range(len(nArray)):
    t0 = time.time()
    for x in range(N):
        A3.MaxSum(nArray[i],0,len(nArray[i])-1)
    t1 = time.time()-t0
    
    t0 = time.time()
    for y in range(N):
        A3.MaxSum(nArray[i],0,len(nArray[i])-1)
    t2 = time.time()-t0
    
    average = (t1+t2)/2
    A3Time[i] = round((average*1000),7)


A4Time = [0]*19

for i in range(len(nArray)):
    t0 = time.time()
    for x in range(N):
        A4.Algorithm_4(nArray[i])
    t1 = time.time()-t0
    
    t0 = time.time()
    for y in range(N):
        A4.Algorithm_4(nArray[i])
    t2 = time.time()-t0
    
    average = (t1+t2)/2
    A4Time[i] = round((average*1000),7)



xAxis = [10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]



def T1(n):
    return ((7*(n**3)/6) + (11*(n**2)/2) - (11*n/3) + 3)/100
def T2(n):
    return ((6*(n**2)) - (3*n) + 3)/100
def T3(n):
    return ((23*n) + (15*n*(math.log(n,2))))/100
def T4(n):
    return (20*n + 4)/100

T1Time = [0]*19
T2Time = [0]*19
T3Time = [0]*19
T4Time = [0]*19
for i in range(19):
    T1Time[i] = round(T1(xAxis[i]),7)
    T2Time[i] = round(T2(xAxis[i]),7)
    T3Time[i] = round(T3(xAxis[i]),7)
    T4Time[i] = round(T4(xAxis[i]),7)

A0 = [0]*19
CompMatrix = np.array([A1Time,A2Time,A3Time,A4Time,T1Time,T2Time,T3Time,T4Time])

out = open('WilliamAbbot_phw_output.txt','w')
out.write("algorithm-1,algorithm-2,algorithm-3,algorithm-4,T1(n),T2(n),T3(n),T4(n)"+',\n')
for i in range(19):
    if(i!=0):
        out.write('\n')
    for x in range(8):
        out.write(str(CompMatrix[x][i])+',')
out.close()

'''
plt.plot(xAxis,A1Time)
plt.plot(xAxis,A2Time)
plt.plot(xAxis,A3Time)
plt.plot(xAxis,A4Time)
plt.plot(xAxis,T1Time)
plt.plot(xAxis,T2Time)
plt.plot(xAxis,T3Time)
plt.plot(xAxis,T4Time)
plt.ylabel('Run Time (us)')
plt.xlabel('N')
plt.legend(['Algorithm 1','Algorithm 2','Algorithm 3','Algorithm 4','T1(n)','T2(n)','T3(n)','T4(n)'])

plt.show()
'''