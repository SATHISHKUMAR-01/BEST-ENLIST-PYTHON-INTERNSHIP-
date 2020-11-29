def newlist(list=["NAME","AGE","DOB"]):
    a=["NAME","AGE","DOB"]
    if(list==["NAME","AGE","DOB"]):
        print("THE SPECIFICATIONS IN LIST",list)
    else:
        a.extend(list)
        print("THE SPECIFICATIONS IN LIST",a)
