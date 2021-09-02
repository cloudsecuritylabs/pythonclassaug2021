class Book():
    number_of_books = 5000
    def __init__(self, name, year ):
        self.name = name
        self.year = year

    #setters and getters
    def set_name(self, name):
        self.name = name

    def get_name(self):
        self.name

book1 = Book("python", 2001)
print(book1.name)
book1.set_name("Java")
print(book1.name)
print(book1.year)
print(book1.number_of_books)

print(Book.number_of_books)




# book2 = Book()
# print(book2.name)
# print(book2.year)
