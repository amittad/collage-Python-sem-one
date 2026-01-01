def tabale(n):
    for i in range(1,11):
        yield n * i
n=int(input("enter a  number="))
for i in tabale(n):
    print(i)        