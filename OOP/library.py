
class Library:


    def __init__(self):
        self.books = {"English" : "Author1", "Nepali" : "Author2"}

    # Remove books from the library
    def remove(self, key):
        del (self.books)[key]

    # Add new books to the library
    def add(self, key, value):
        (self.books)[key] = value


l1 = Library()
print(l1.books)
l1.remove("English")
print(l1.books)
l1.add("NewBook", "Author")
