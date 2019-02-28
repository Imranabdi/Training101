# initialize a list
emptylist=[]

# create a list
daysOfTheWeek=['mon','tue','wed','thurs','fri','sat','sun']
# print the list
print(daysOfTheWeek)
# print the list item at index 2
print(daysOfTheWeek[2])
# finding the length of the list
numberOfDaysInAWeek = len(daysOfTheWeek)
print(numberOfDaysInAWeek)

# list indexing
print(daysOfTheWeek[3:4])

details = ['immy',21,'imranabdi1616@gmail.com','Nairobi']
age = details[1]
location = details[3]
reverse = details [-1:]

numbers = [0,1,2,3,4,5,6,7,8,9,10]
# prints from the front
subNum = numbers[8:10]
print(subNum)
# printing from behind
subNum2 = numbers[-3:-1]
print(subNum2)

# adding an item to the end of the list
daysOfTheWeek.append("valentine")
print(daysOfTheWeek)

# removing all item/items from the list
daysOfTheWeek.clear()
print(daysOfTheWeek)

daysOfTheWeek.extend("hello world")
print(daysOfTheWeek)






