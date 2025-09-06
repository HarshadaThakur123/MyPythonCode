marks=int(input("marks:"))

if(marks >= 90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("C")
else:
    print("D")

marks2=int(input("marks:"))
if(marks >= 90):
   grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
else:
    grade="D"
print("grade of student is:-->",marks2)