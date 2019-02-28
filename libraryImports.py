from libraryClass import Library

techCampLib = Library(bks=1000,gen=['Comedy','Drama','Fiction'],mems=['Brian','Jose','Imran'])

print(techCampLib.books)
print(techCampLib.members)
print(techCampLib.genre)

techCampLib.lend()
print(techCampLib.booksNumber)

