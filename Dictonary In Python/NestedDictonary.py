student={
    "name":"Rahulkuumar",
    "subject":{
        "phy":23,
        "math":63,
        "eng":96

    }
}
print(student)
print(student["subject"])
print(student["subject"]["math"])
student.update({"city":"delhi","age":16})
print(student)