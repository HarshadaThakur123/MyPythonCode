student={
    "name":"Rahulkuumar",
    "subject":{
        "phy":23,
        "math":63,
        "eng":96

    }
}
#print keys
print(student.keys())

#typecast
print(list(student.keys()))

#total no of keys
print(len(student))
print(len(list(student.keys())))

# returns values 
print(student.values())
print(list(student.values()))

#keys values as tuples
print(student.items())
pair=list(student.items()) 
print(pair) #tuple convert in list
print(pair[0])

print(student["name"]) 
print(student.get("name"))
#print(student["name2"])  error return
print(student.get("name2")) #return None
 





