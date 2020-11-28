#EXERCISE 1
list1=[1,2,3,4,5,6,7,8,9]
print("THE ACTUAL LIST :",list1)
x=len(list1)
for i in range(0,x):
    list1[i]=list1[i]+2
print("THE LIST AFTER ADDING +2 :",list1)


#EXERCISE 2
print("PATTERN PRINTING")
x=int(input("ENTER THE ENDING VALUE OF PATTERN : "))
#ENTER 5 HERE

for i in range(1,x+1,1):
    for j in range((x+1)-i,0,-1):
        print(j,end="")
    print("\n")
      

#EXERCISE 3
n=int(input("ENTER THE NUMBER OF TERMS :"))
print("FIBONACCI SERIES ARE :")
a=0
b=1
print(a)
print(b)
for i in range(1,n-1,1):
    c=a+b
    print(c)
    a=b
    b=c

#EXERCISE 4
print("ARMSTRONG NUMBER")
print("***GET THE NUMBER OF DIGITS IN THE GIVEN NUMBER SAY N,THEN POWER THE EACH DIGIT IN THE NUMBER BY N, DO IT FOR ALL NUMBER ,THEN ADD THE RESULT,IF IT IS EQUAL TO THE GIVEN NUMBER, THEN IT IS A ARMSTRONG NUMBER***")
print("###example 153 is a armstrong number,the number of digits in the given number is 3, where 1^3 + 5^3 + 3^3 = 153, which is the given number")     
x=int(input("ENTER THE NUMBER TO CHECK WHETHER IT IS A ARMSTRONG NUMBER OR NOT ? "))
y=x
con=len(str(y))
add=0
last=0
power=0
while(x!=0):
    last=x%10
    power=last**con
    add=add+power
    x=x//10
if(y==add):
    print("THE GIVEN NUMBER IS A ARMSTRONG NUMBER")
else:
    print("THE GIVEN NUMBER IS NOT A ARMSTRONG NUMBER")

#EXERCISE 5
print("MULTIPLICATION TABLE OF 9")
x=9
for i in range(1,11,1):
    print("9 X ",i,"=",x*i)

#EXERCISE 6
x=int(input("ENTER THE NUMBER : "))
if(x>0):
    print("THE GIVEN NUMBER IS A POSITIVE NUMBER")
elif(x<0):
    print("THE GIVEN NUMBER IS A NEGATIVE NUMBER")
else:
    print("THE GIVEN NUMBER IS NEITHER A POSTIVE NOR A NEGATIVE NUMBER")

#EXERCISE 7
a=int(input("ENTER THE NUMBER OF DAYS : "))
yr=int(a/365)
dy=a%365
print(" THE AGE IS :",yr,"YEAR(S) AND ",dy," DAYS")

#EXERCISE 8

from math import *
print("TRIGONOMETRIC FUNCTION and SQUARE ROOT\n 1.sin \n 2.cos \n 3.tan \n 4.cosec \n 5.sec \n 6.cot \n 7.square root of a number ")
x=int(input("ENTER YOUR CHOICE OF TRIGONOMERTIC FUNCTION AND SQUARE ROOT:"))
if(x==1):
    y=int(input("ENTER THE DEGREE :"))
    val=sin(y)
    print("sin",y,"=",val)
elif(x==2):
    y=int(input("ENTER THE DEGREE :"))
    val=cos(y)
    print("cos",y,"=",val)
elif(x==3):
    y=int(input("ENTER THE DEGREE :"))
    val=tan(y)
    print("tan",y,"=",val)
elif(x==4):
    y=int(input("ENTER THE DEGREE :"))
    val=1/sin(y)
    print("cosec",y,"=",val)
elif(x==5):
    y=int(input("ENTER THE DEGREE :"))
    val=1/cos(y)
    print("sec",y,"=",val)
elif(x==6):
    y=int(input("ENTER THE DEGREE :"))
    val=1/tan(y)
    print("cot",y,"=",val)
elif(x==7):
    y=int(input("ENTER THE NUMBER:"))
    print(sqrt(y))


#EXERCISE 9
print("CALCULATOR \n 1.addition \n 2.subtraction \n 3.multiplication \n 4.division")
x=int(input("ENTER YOUR CHOICE OF OPERATION :"))
a=int(input("ENTER THE FIRST VALUE :"))
b=int(input("ENTER THE SECOND VALUE :"))
if(x==1):
    print("ADDITION OF TWO VALUES :",a+b)
elif(x==2):
    print("SUBTRACTION OF TWO VALUES :",a-b)
elif(x==3):
    print("MULTIPLICATION OF TWO VALUES :",a*b)
elif(x==4):
    print("DIVISION OF TWO VALUES :",a/b)
else:
    print("YOU HAVE ENTERED WRONG CHOICE")











    

    


    
    
