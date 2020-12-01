############## LAMBDA FUNCTION THAT MULTIPLIES ARGUMENT X WITH ARGUMENT Y  ###########

def lamb_func(a,b):
    lamb_assign=lambda a,b:a*b
    print("Multiplication of two arguments :",lamb_assign(a,b))
    
x=int(input("Enter the first number :"))
y=int(input("Enter the second number :"))
lamb_func(x,y)

############### FIBONACCI SERIES TO N USING LAMBDA ###################

print("FIBONACCI SERIES")
x=int(input("Enter the number upto which you want to print fibonacci series :"))
a=0
print(a)
b=1
print(b)
c=0
while(c<x):
    lamb_series=lambda a,b:a+b
    if(lamb_series(a,b) <= x):
        print(lamb_series(a,b))
    c=a+b
    a=b
    b=c

################## MULTIPLY EACH NUMBER OF GIVEN LIST WITH A GIVEN NUMBER ################

a=[]
h=int(input("How many elements you want to enter in the list:"))
for i in range(0,h,1):
    u=int(input("Enter the number:"))
    a.insert(i,u)   
print("The given list :",a)
y=int(input("Enter the number which you want to multiply with each element in list:"))
print("The list after multiplying ",x,"to each number in list : ",list(map(lambda x:x*y,a)))

################# NUMBERS DIVISIBLE BY 9 FROM A LIST OF INTEGERS #############################
a=[]
h=int(input("How many elements you want to enter in the list:"))
for i in range(0,h,1):
    u=int(input("Enter the number:"))
    a.insert(i,u)    
print("The given list :",a)
print("Numbers that are divisible by 9 in the given list : ",list(filter(lambda x:(x%9==0),a)))

################ COUNT THE EVEN NUMBERS IN THE GIVEN LIST OF INTEGERS #########################


a=[]
h=int(input("How many elements you want to enter in the list:"))
for i in range(0,h,1):
    u=int(input("Enter the number:"))
    a.insert(i,u)    
print("The given list :",a)
count=0;
for i in range(0,h,1):
    u=a[i]
    eve=lambda x:x%2==0
    if(eve(u)== True):
        count=count+1
print("The number of even integers in the given list is : ",count)


