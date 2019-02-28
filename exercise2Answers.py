taskList = [23,"Jane",["Lesson 23",560,{"currency":"KES"},987,(76,"John")]]

# 2.Print KES
print(taskList[2][2]["currency"])

# 3.Print 560
print(taskList[2][1])

# 5.Change 987 to 789 using an inbuilt function
c = taskList[2]
d = str(c[3])
print(int(d[::-1]))


