# task1
myInput = input("ENTER A STRING:")

if myInput == "yes" or myInput =="YES" or myInput=="Yes":
    print("Yes")
else:
    print("No")


# task2
def findLargest(a,b,c):
    x = int(a)
    y = int(b)
    z = int(c)
    if x > y and x > z:
        print(a + " is larger")
    elif y > x and y > z:
        print(b + " is larger")
    elif z > x and z > y:
        print(c + " is larger")
    return x,y,z

x = input("Enter first number:")
y = input("Enter second number:")
z = input("Enter third number:")
lar = findLargest(x,y,z)
print(lar)


# task3
def createList(list):
    list=[10,20,30,40,50]
    newlist = [list[0],list[-1]]
    return newlist

newL = createList(list)
print(newL)

# task4
askNumber = input("Enter a number of choice:")
convertToNumber = int(askNumber)

if convertToNumber % 2 == 0:
    print(askNumber + " Is an even number")
else:
    print(askNumber + " Is an odd number")




def determineTypeOfNUMBER(num):
    if num % 4 == 0 :
        return  "The number is multiple of 4"
    elif num % 2 == 0 :
        return "The number is even"
    else:
        return "The number is odd"

number = int(input("Enter a number"))
print(determineTypeOfNUMBER(number))

# task 5
tuple = (1,2,3,4,5,6,7,8,9,10)

tuple1 = tuple[:int (len(tuple)/2)]
tuple2 = tuple[int (len(tuple)/2):]

print(tuple1)
print(tuple2)

print(int (len(tuple)/2))