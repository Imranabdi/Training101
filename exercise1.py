sentence = "The dog finished the pie"

# Write a python program to answer below questions
# 1.How many words are in the string
convertToList = sentence.split()
print(len(convertToList))

# 2.What is the length of string sentence
print(len(sentence))


# 3.How many times does word dog appear
print(sentence.count("dog"))

# 4.write a new string similar to sentence except that all letters are capitals
print(sentence.upper())