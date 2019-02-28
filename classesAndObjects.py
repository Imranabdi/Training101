# a class is a blueprint or prototype ie collection of related properties and methods

class Student:
   # class variables are variables that are shared across all instances
    registrationNumber = ""
    grade = ""
    total = 0
    average = 0



    def __init__(self,math,eng,kisw,sci,sst):
       self.totalMarks(math,eng,kisw,sci,sst)
       self.calcAve(self.total)


    def totalMarks(self,math,eng,kisw,sci,sst):
        self.total = math+eng+kisw+sci+sst
        

    def calcAve(self,tot):
        self.average = tot/5

# variable brian is an object of a class
brian = Student(1,2,3,4,5)

print(brian.total)
