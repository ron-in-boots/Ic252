import random
import math

n=int(input("Enter no. of trials: "))
count=0

for i in range(n):
    l=[50,50]
    for j in range(5):
        x=random.randint(0,1)
        l[x]-=1
    if l[0]==47 and l[1]==48:
        count+=1
    
print("probablity of 3 blue and 2 red is by simulation",count/n)   


prob=(math.comb(50,3)*math.comb(50,2)) /math.comb(100,5)  
print("probablity of 3 blue and 2 red is by combinatorics ",prob)   



  

