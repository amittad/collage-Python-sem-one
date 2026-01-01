s = input("Enter a string: ")

new=""
for i in range(len(s)):
    if i%2!=0:
        new+=s[i]
print(new)        