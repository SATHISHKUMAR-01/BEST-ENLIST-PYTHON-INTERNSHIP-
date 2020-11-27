#EXERCISE 1

def operation(a,b):
    add=a+b
    print("ADDITION ",add)
    sub=a-b
    print("SUBTRACTION ",sub)
    div=a/b
    print("DIVISION ",div)
    mul=a*b
    print("MULTIPLICATION ",mul)


def getvalue():
    x=int(input("ENTER THE FIRST VALUE:"))
    y=int(input("ENTER THE SECOND VALUE:"))
    operation(x,y)

getvalue()

#EXERCISE 2

def covid(pname,ptemp=98):
    print("PATIENT NAME :",pname)
    print("PATIENT'S BODY TEMPERATURE :",ptemp)
S
x=input("ENTER THE PATIENT'S NAME :")
y=int(input("ENTER THE BODY TEMPERATURE OF THE PERSON :"))
covid(x,y)
