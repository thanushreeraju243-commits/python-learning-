class book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"
    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.year})"
    def __eq__(self, other):
        if not isinstance(other, book):
            return False
        return (self.title == other.title and
                self.author == other.author and
                self.year == other.year)
    def __lt__(self, other):
        if not isinstance(other, book):
            return NotImplemented
        return self.year < other.year
book1 = book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book2 = book("To Kill a Mockingbird", "Harper Lee", 1960)
print(book1)
print(book2)
print(repr(book1))
print(repr(book2))
print(book1 == book2)
print(book1 < book2)
print(book1 > book2)

