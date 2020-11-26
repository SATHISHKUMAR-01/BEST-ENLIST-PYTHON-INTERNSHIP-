#EXERCISE 1
def addtolist(list,a):
    list.append(a)
    print(list)
    

list=[1,2,3,4,5,6,7,8,9]
print("THE LIST IS :",list)
a=int(input("ENTER THE ELEMENT TO ADD IN THE LIST : "))
addtolist(list,a)

def delfromlist(list,x):
    list.remove(x)
    print(list)
      
x=int(input("ENTER THE ELEMENT TO DELETE FROM LIST :"))
delfromlist(list,x)

for i in list:
    min_int=min(list)
print("THE SMALLEST INTEGER :",min_int)

for j in list:
    max_int=max(list)
print("THE LARGEST INTEGER :",max_int)

#EXERCISE 2
tuple=("summer","winter","autumn","spring")
a=len(tuple)-1
for i in range(a,-1,-1):
    print(tuple[i])

#EXERCISE 3
tu=("ONE","TWO","THREE","FOUR","FIVE")
li=list(tu)
print(li)
