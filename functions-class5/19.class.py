'''
What about a Book class?
may be we only care about year of publication and the title of the book
let's create a class
'''












class Book():
    # title = "Python Programming"
    # year = 2021

    # class variable
    count_of_books = 0

    # title and name are encapsulated
    # constructor
    def __init__(self, title, year):
        self.title = title # object variables
        self.year = year
        Book.count_of_books +=1


    # method
    def get_title(self):
        return self.title


    def get_year(self):
        return self.year


    def set_year(self, year):
        self.year = year

    def __str__(self):
        return f'Title is {self.title} and year is {self.year}'



# b1 = Book()
# b2 = Book()
# print(b1.title)
# print(b1.year)


b1 = Book("Python", 2020)
b2 = Book("Java", 2021)
print(b1.get_title())
print(b1.get_year())
print(b2.get_title())
print(b2.get_year())
b2.set_year(3000)
print(b2.get_year())
print(b2)
print(Book.count_of_books)
print(b2.count_of_books)

Book.count_of_books = 400
b3=Book("php", 1900)
print(Book.count_of_books)



class ChildrenBook(Book):
    pass

c1 = ChildrenBook("Kiddo", "Nice")
print(c1)

