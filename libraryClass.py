class Library:
    genre = []
    books = 0
    members = []

    # define a constructor
    def __init__(self,gen,bks,mems):
        self.genre = gen
        self.booksNumber = bks
        self.members = mems

    def lend(self):
        self.booksNumber -=1