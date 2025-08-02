import random
n=10000

count1=0
count2=0
count3=0
for i in range(n):
    l=[]
    for j in range(5):
        l.append(random.randint(1,6))
        
    p1=l[0]+l[1]
    p2=l[2]+l[3]+l[4]

    if (p1>p2):
        count1+=1
    if (p1<p2):
        count2+=1
    if (p1==p2):
        count3+=1      
        

print("Probability Player 1 wins: ",count1/n)        
print("Probability Player 2 wins: ",count2/n)        
print("Probability of a Tie: ",count3/n)        



        
        
   
    
    