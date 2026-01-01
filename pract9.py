class ageexpection(Exception):
    pass
try:
    age=int(input("enter a age"))
    if age>18:
        print("age is acepted")
    else:
        raise ageexpection("age is below 18 not accepted"  )  
except ageexpection as e:
    print("user defined expectiom",e)  
except ValueError:
    print("Invalid input. Please enter a valid age.")      
