############  JSON OF ALL DATA TYPES #################

import json

x={
    "Name of the school" : "PSM",
    "Total number of students" : 1000,
    "Average percentage in public exams" : 88.9,
    "Address" : {"Street":"SaiNagar","City":"Chennai","State":"TamilNadu","Country":"India"},
    "Other branches located in Chennai" : ["T Nagar","Guindy","Ashok Nagar"],
    "Best school award in the year" : (2016,2017,2020),
    "Presence of qualified teachers" : True,
    "Any bad behaviour of students" : False,
    "Any faults" : None
}


y=json.dumps(x,indent=5)
print("The JSON FILE : \n",y)

