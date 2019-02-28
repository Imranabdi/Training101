#a function is a block of code that is used to perform a related function
# A function is a block of code which only runs when it is called.
# to define a function we use a key work def:

# def chapisha(sth):
#     print(sth)
#
# chapisha("Hello world")
def totalMarks(math,eng,kisw,sci,ssr):
    total= math + eng + kisw + sci + ssr
    return total

def average(total):
    avg = total/5
    return avg


def findGrade(average):
    if average >= 80 and average < 101:
        return "GRADE A"
    elif average >= 70:
         return "GRADE B"
    elif average >= 60:
        return "GRADE C"
    elif average >= 50:
        return "GRADE D"
    else:
     return "GRADE E"