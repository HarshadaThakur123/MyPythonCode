for i in range(5):
    pass  #we dont want to write anything in there 

#write sum of first n numbers (using while)
n=int(input("enter:"))
i=1
sum=0
while i<=n:
    sum=sum+i
    i+=1
print(sum)

n=5
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

#find factorials of first n numbers(using for)
n=5
fac=1
for i in range(1,n+1):
    fac*=i
    i+=1
print(fac)
