import random
count1=0
count2=0

for i in range(10000):
    x=random.randint(1,6)
    y=random.randint(1,6)
    if (x==y):
        count1+=1
    if (x+y>9):
        count2+=1
print("Probability of same no.:",count1/10000)    
print("Sum greater than 9:",count2/10000)    
    
        
    
