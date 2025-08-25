a=int(input("enter angle:"))    
b=int(input("enter second angle:"))
c=int(input("enter third angle:"))

if(a==90 or b==90 or c==90 ):
    print("Right triangle")
elif(a>90 or b>90 or c>90):
       print("obtuse triangle")
else:
    print("It is acute triangle")

 