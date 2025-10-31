try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise Exception("Age is below 18 — Not Eligible!")
    else:
        print("Eligible! Age is valid:", age)
except Exception as e:
    print("Exception Caught:", e)
