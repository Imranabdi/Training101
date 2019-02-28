myFirstString = "hello world"

# methods that manipulate strings

# capitalize the first letter of the string
print(myFirstString.capitalize())

# change the string to uppercase
print(myFirstString.upper())

# make every letter to lowercase
print(myFirstString.lower())

# check the number of characters on the string
print(len(myFirstString))

# count a specified letter in the string
print(myFirstString.count('o'))

# multi assignment
firstName,secondName = "Imran","Shaz"
print(firstName)
print(secondName)

# concatinating two strings
fullName = firstName + " " + secondName
print(fullName)

# GETTING THE FIRST LETTER OF THE STRING
firstLetter = fullName[0]

# CHECKING IF THE firstLetter is lowercase
print(firstLetter.islower())

# DETERMINING THE LENGTH OF A STRING
lengthOfMyString = len(fullName)
print(lengthOfMyString)

# two ways checking the last letter
lastLetter = fullName[-1]
lastLetter = fullName[len(fullName)-1]
print(lastLetter)

