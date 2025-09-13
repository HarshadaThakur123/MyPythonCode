dict={
    "key":"value",
    "name":"harshu",
    "learning":"python",
    "age":21,
    "its adult":True,
    "marks":69.78,
    "subject":["python","c","java"],
    "tuples":("dict","set"),
    12:"harshu",
    99.15:"same" #in key we do not add list and dictonary because we want value those not change we also get tuple(immutable)


}
print(dict["name"])
print(dict["subject"])
print(type(dict))
dict["name"]="HonestHarshu" #change value (overwrite)
dict["hobby"]="Dancing" #add new value
print(dict)

null_dict={}  #null dictonary
print(null_dict)
null_dict["name"]="helo"
print(null_dict)