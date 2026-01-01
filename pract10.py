class even_odd(Exception):
    pass

try:
    num=int(input("enter a number="))
    if num %2==0:
        print("enter a number is valid and even number")
    else:
        raise even_odd("enter number is not even ")

except even_odd as e:
    print("user defined error",e)        