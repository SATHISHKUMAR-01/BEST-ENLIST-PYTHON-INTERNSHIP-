#exercise : to create a module and implement it in another py file
#mymodule
""" def newlist(list):
    a=["NAME","AGE","DOB"]
    a.extend(list)
    print(a)  """
#I have uploaded my module in github under the name "module"


import module
print("WELCOME TO BIO DATA")
a=input("do you want to add any specification (y/n) :")
c=[]
if(a=='y' or a=='Y'):
    b=int(input("how many elements to want to add in form :"))
    for i in range(1,b+1,1):
        d=input("ENTER  THE SPECIFICATION:")
        c.append(d)
    module.newlist(c)   
else:
    module.newlist()

#exercise using random module

import random

x=int(input("how many runs you want:"))
for i in range(1,x+1):
      a=random.randrange(1,100)
      print(a)









    
    
    
    

