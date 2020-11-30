################   ERRORS   ###################
from math import squareroot 

a=int(input("ENTER THE NUMBER:")) # VALUE ERROR , if other data types is given as input

print("number"+a)                 #TYPE ERROR

print(b)                          #NAME ERROR

print(a/0)                        #ZERO DIVISION ERROR

if(a>0)                           #SYNTAX ERROR
  print(a)

b=[a,23,4]
print(b[0])                       #INDEX ERROR

print(squareroot(a))              #IMPORT ERROR

################# DESIGN A SIMPLE CALCULATOR WITH TRY AND EXCEPT  #########################

print("CALCULATOR \n 1.addition \n 2.subtraction \n 3.multiplication \n 4.division")
x=int(input("ENTER YOUR CHOICE OF OPERATION :"))
a=int(input("ENTER THE FIRST VALUE :"))
b=int(input("ENTER THE SECOND VALUE :"))
if(x==1):
    try:
        c=a+b
        print("ADDITION OF TWO VALUES :",c)
    except:
        print("NOTHING WENT WRONG")
    else:
        print("addition is successfull")
      
elif(x==2):
    c=a-b
    print("SUBTRACTION OF TWO VALUES :",c)
    if(c<0):
        raise Exception("you can avoid entering a negative value as a second value, to ignore the negative value as a answer")
    
elif(x==3):
    c=a*b
    print("MULTIPLICATION OF TWO VALUES :",c)
    if(a==0 or b==0):
        raise Exception("Dont give '0' as a value , because any integer multiplying with  zero, will produce zero as a ouput")
    
elif(x==4):
    try:
        c=a/b
    except ZeroDivisionError:
        print("You can't divide a number by zero.....Otherwise zero division error will occur")
    else:
        print("DIVISION OF TWO VALUES :",c)

else:
    print("YOU HAVE ENTERED WRONG CHOICE")

################################### PRINT ONE MESSAGE IF TRY BLOCK RAISES NAME ERROR #######################

x=int(input("ENTER A  TWO DIGIT NUMBER :"))
y=int(input("ENTER THE NUMBER IN REVERSE :"))
try:
    print(x)
    print(o)
except NameError:
    print("NameError occurred.....pls check the code.....hope you understand it....")
except ValueError:
    print("ValueError occurred....pls enter integer as input........")
else:
    print("NO ERRORS .....PROGRAM SUCCESSFULL")

###################### WHEN TRY-EXCEPT SCENARIO IS NOT REQUIRED ##################################

"""ANSWER : TRY-EXCEPT SCENARIO IS NOT REQUIRED IN CASE OF SIMPLE PROGRAMS...WHEN THERE IS NO EXCEPTIONS IN THE PROGRAM,THIS SCENARIO IS NOT REQUIRED.....IT IS USEFUL IN CASE OF COMPLEX PROGRAMS....IN SOME PROGRAMS,TRY EXCEPT SCENARIO CAN CAUSE MISUNDERSTANDINGS IN THE PROGRAM"""


########################################### GETTING INPUT IN TRY BLOCK ###################################
x=int(input("Enter a number :"))
try:
    a=int(input("Enter anything which you want to add your first number:"))
    print("New number is :",a+x)
except ValueError:
    print("value error occurred.....Give  only number as input,which you want to add")




   
