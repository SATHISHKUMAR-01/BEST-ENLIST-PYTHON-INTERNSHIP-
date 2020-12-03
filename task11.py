
########################### CREATE A MERGED LIST OF TUPLES FROM THE TWO LIST GIVEN #######################################

lis1 = [1,2,3,4,5]
lis2 = ['one','two','three','four','five']
print("THE GIVEN LISTS ARE : \n",lis1,"\n",lis2)
x=list(tuple(zip(lis1,lis2)))
print("THE MERGED LIST OF TUPLES FROM GIVEN TWO LISTS : \n",x)

########################### MERGE THE GIVEN LIST AND RANGE TOGETHER TO CREATE A NEW LIST OF TUPLES ########################


y = range(1,9,1)  
giv_list=["BIKE","CAR","BUS","AUTO","TRAIN","FLIGHT","SHIP","HELICOPTER"]    
print("THE GIVEN LIST IS : \n",giv_list)
new=tuple(zip(y,giv_list))
print("A NEW LIST OF TUPLES AFTER MERGING THE GIVEN LIST AND RANGE TOGETHER IS : \n",new)

########################### SORT THE LIST IN ASCENDING ORDER ###############################################################

print("WELCOME.... CREATE A LIST OF NUMBERS BY YOURSELF")
x=int(input("How many elements you want to present in your list :"))
a=[]
for i in range(0,x,1):
    u=int(input("Enter the element :")) 
    a.append(u)
    
print("THE LIST CREATED IS :",a)
a.sort()
print("THE LIST AFTER SORTING IT IN ASCENDING ORDER : \n",a)

########################### FILTER THE EVEN NUMBERS IN THE LIST AND PASS ONLY ODD NUMBERS TO THE NEW LIST ######################

def eve(l):
    if(l%2==1):
        return True
    else:
        return False
print("WELCOME.... CREATE A LIST OF NUMBERS BY YOURSELF")
x=int(input("How many elements you want to present in your list :"))
a=[]
for i in range(0,x,1):
    u=int(input("Enter the element :")) 
    a.append(u)
    
print("THE LIST CREATED IS :",a)  


fil=filter(eve,a)
new_lis=list(fil)
print("THE NEW LIST AFTER PASSING THE ODD NUMBERS IN THE OLD LIST :\n",new_lis)













