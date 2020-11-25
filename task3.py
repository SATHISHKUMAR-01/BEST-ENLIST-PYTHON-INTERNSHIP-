                       #day3 #task 3
#EXERCISE 1
dict1={'NAME':'SATHISH','AGE':19}
dict2={'GENDER':'MALE','CITY':'CHENNAI'}
dict1.update(dict2)
print(dict1)

#EXERCISE 2
dict1={'FRUIT':'APPLE','VEGETABLE':'ONION'}
dict1.pop('FRUIT')   #the key 'fruit' is removed
print(dict1)

#EXERCISE 3
LIST1=["SEASON","MONTH","YEAR"]
LIST2=["SUMMER","APRIL",2019]
DICTIONARY=dict(zip(LIST1,LIST2))
print(DICTIONARY)

#EXERCISE 4
set={"CHENNAI","BANGALORE","MUMBAI","DELHI"}
print(len(set))

#EXERCISE 5
s1={100,200,300,400}
s2={400,500,600,700}
s1.difference_update(s2)
print(s1)
