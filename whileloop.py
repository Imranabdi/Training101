# a while loop tells python to repeat execution a certain statement or block of statements untill a specified condition is false

i = 0
numbers = [0,1,2,3,4,5]
while len(numbers)>0:
    print(numbers)
    numbers.pop()


while i<10:
    print("immy")
    i+=1


password_saved = "1234"
password = input("Enter your password")
tries = 1
while password != "1234" and tries <3 :
    maxTries -= 1
    password = input("please enter correct password "+maxtTries +  "triesleft".format(maxtries))
    tries+=1
if tries >= 3:
    print("pin blocked, your card is retained")
else:
 print("Hurray correct password entered")