class Book:
    allbooks = {}

    def __init__(self, bookName, bookAuthor,price):
        self.name = bookName
        self.author = bookAuthor
        self.price = price
        
        Book.allbooks.update({self.name: self.author})
        print(Book.allbooks)
    def createBook(self):
        dictt={'name':self.name,'author':self.author,'price':self.price}
        Book.allbooks.update(dictt)
search=input('enter 1 for add \nenter 2 ')
while search:
    if search :
        user_pick=input('Pick a book ')
        if user_pick in Book.allbooks:
            print(Book.allbooks.get())
    Book(bookName=input('Enter book name'),
            bookAuthor=input('Enter book name'))
