###########################  TO CHECK A STRING WITH A GIVEN CASE  #############################################
import re

str=input("Enter the string : ")
str=str.replace(" ","")
x= re.search("\W",str)
if x:
    print("Wrong match....Your string contains special characters..Enter only alphabets and numbers")
else:
    print("Perfect string !!!!!!")

#########################  MATCHES A WORD CONTAINING 'ab' ######################################################
import re

str=input("Enter the string : ")
x = re.search("ab", str)
if x:
    print("Yes , there is word which match 'ab' in the given string")
else:
    print("There is no word matches with the given string containing 'ab'")

          
########################  CHECK FOR A NUMBER AT THE END OF A WORD/SENTENCE ######################################
import re

string=input("Enter the string : ")
x=re.search("\d$",string)
if x:
    print("THERE IS A NUMBER AT THE END OF THE WORD/SENTENCE")
else:
    print("THERE IS NO NUMBER PRESENT AT THE END OF THE WORD/SENTENCE")

######################## TO SEARCH FOR NUMBERS(0-9) OF LENGTH BETWEEN 1 TO 3 IN A GIVEN STRING  ####################
import re

str=input("Enter the string or word:")
if(re.search("\d",str)):
    print(str)
    x=re.finditer(r"([0-9]{1,3})",str)
    print("The numbers of length between 1 to 3 in the given string:")
    for i in x:
        print(i.group())
else:
    print("Enter a string with some values of numbers..")

    
####################### TO MATCH A STRING THAT CONTAINS ONLY UPPERCASE LETTERS ###############################
import re

x=input("Enter the string/word :")
y=re.findall("[A-Z]",x)
if y:
    print("There is a perfect match....It contains atleast one uppercase letter")
else:
    print("Not a perfect match......It does not contain any uppercase letter")


















    


    
