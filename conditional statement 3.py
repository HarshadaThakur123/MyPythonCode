A=int(input("A:"))
G=input("m/F:")

if((A==1 or A==2) and G=="M"):
    print("fee is 100")
elif(A==3 or A==4 or G=="F"):
    print("fee is 200")
elif(A==5 and G=="M"):
    print("fees is 300")
else:
    print("no fee")


    """ output we get A=5 and G=M
    first line :False or false =false
                false and True =False

    Second line :False or false =false
                 False or false =false

    third line: True and True= true  

    o/p: A=2 and  G=F
    first line :False or True =True
               True and False =False
    Second line :False or false =false
                 False or True =True

    """