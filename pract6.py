'''Write a Python program to make a chain of function decorators (bold, italic, 
underline etc.) in Python. '''

def bold(func):
    def wrapper():
        return "<b>"+ func()+"</b>"
    return wrapper
def italic(func):
    def wrapper():
        return "<i>"+ func()+"</i>"
    return wrapper
@italic
@bold
def amit():
    return"amit"
print(amit())

