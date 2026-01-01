def getdata():
    student={
        "name":"amit",
        "age" : 22,
        "marks": 80

    }
    return student

def display(data):
    print(data["name"])
    print(data["age"])
    print(data["marks"])

display(getdata())    

