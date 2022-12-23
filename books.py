atomicHabits={'Author':'James Clear','First published': '10/16/2018','Price':'35'}
richDadPoorDad={'Author':'Robert','First published': '10/18/2018','Price':'20'}
allBooks={'atomic habits':atomicHabits,'money':richDadPoorDad}
user=str(input('Pick A Book '))
# print(allBooks.get(user))
def newbook():
    print ('''The book isn't available \n plese enter it as a new book ''') 
    book=str(input(''' Enter The Book's name : '''))  
    author=str(input(''' Enter The Author's name : '''))
    firstPublished=str(input(' Enter The First published date :  '))
    price=str(input(''' Enter The Books's price : '''))
    newBook={'Author':author,'First published': firstPublished,'Price':price}
    allBooks.update({book:newBook})
    print(allBooks)
    print('Book Added Successfully')

if (user in allBooks):
    print(allBooks.get(user))

else:
    newbook()


