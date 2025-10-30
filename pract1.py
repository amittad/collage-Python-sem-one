#Sr. No. Programs 
#1 Write a code in python to count number of vowels in given string  
#Steps: 
 #a. Accept string from user in variable named STR1. 
# b. Count the number of vowels in STR1 and print.  
#Eg. 1.STR1 = 'COCONUT' => 3 
#      2.STR1 = 'CONFIDence' => 4 #

str1=str(input("enter a string="))
count=0
n1="aeiouAEIOU"
for i in str1:
    if i in n1:
        count+=1
print(count)