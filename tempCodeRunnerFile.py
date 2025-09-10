#cheack if a number enterd by the user is odd or even
num=int(input("Enter number:"))
if(num%2==0):
    print("num is even")
else:
    print("num is odd")

#to find greatest of 3 number entered by the user 
num1=int(input("Enter number:"))
num2=int(input("Enter number:"))
num3=int(input("Enter number:"))
if(num1>num2):
    if(num1>num3):
        print(num1,"is greatest")
    else:
        print(num3,"is greatest")
elif(num2>num3):
    print(num2,"is greatest")
else:
     print(num3,"is greatest")

#or easy
a=int(input("Enter number:"))
b=int(input("Enter number:"))
c=int(input("Enter number:"))
if(a>b and a>c):
    print("num1 greate")
elif(b>c):
    print("num2 greater ")
else:
    print("num3 greate ")

#check num is multiple of 7 or not

num4=int(input("Enter number:"))
if(num4%7==0):
    print(num4,"multiple of 7")
else:
    print(num4,"not multiple of 7")