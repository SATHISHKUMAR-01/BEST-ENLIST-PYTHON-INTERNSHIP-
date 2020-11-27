#EXERCISE 1
def add(a,b):
    a1=a+b
    return a1
def sub(a,b):
    s1=a-b
    return s1
def mul(a,b):
    m1=a*b
    return m1
def div(a,b):
    d1=a/b
    return d1


def getvalue():
    x=int(input("ENTER THE FIRST VALUE:"))
    y=int(input("ENTER THE SECOND VALUE:"))
    print("ADDITION OF TWO NUMBERS ",add(x,y))
    print("SUBTRACTION OF TWO NUMBERS ",sub(x,y))
    print("MULTIPLICATION OF TWO NUMBERS ",mul(x,y))
    print("DIVISION OF TWO NUMBERS ",div(x,y))
getvalue()

#EXERCISE 2

def covid(pname,ptemp=98):
    print("PATIENT NAME :",pname)
    print("PATIENT'S BODY TEMPERATURE :",ptemp,"F")

x=input("ENTER THE PATIENT'S NAME :")
y=int(input("ENTER THE BODY TEMPERATURE OF THE PERSON :"))
print("Before using the default value")
covid(x,y)
print("After using the default value")
covid(x)
