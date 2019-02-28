taskList = [23,"Jane",["Lesson 23",560,{"currency":"KES"},987,(76,"John")]]
# 1.Determine the type of variable taskList using an inbuilt function
print(type(taskList))


# 2.Print KES
x = taskList[2]
#print(x)
y = (x[2])
#print(y)
z = y.get("currency")
print(z)


# 3.Print 560
a = taskList[2]
#print(a)
b = a[1]
print(b)


# 4.Use a function to determine the length of tasklist
print(len(taskList))


# 5.Change 987 to 789 using an function
c = taskList[2]
d = str(c[3])
print(int(d[::-1]))


# 6.Change name "John" to "Jane
#not possible


