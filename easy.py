#EASY 1
#Given a string s consisting of words and spaces ,return the length of the last word in the string

def length(str):
	lis = list(str.split(" "))
	return len(lis[-1])


#example 1

s='hello world'
print(length(s))

#example 2
s='fly me to the moon'
print(length(s))

s = input("enter the string: ")
print("The length of last word is",length(s))