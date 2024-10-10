class Books:
    def __init__ (self,title ,author ,page):
        self.title =title
        self.author =author
        self.page =page

    def info(self):
        return f"Title : {self.title} , Author : {self.author} , Page : {self.page}"

    def in_long_page(self):
        return self.page >=100

class PriceBooks(Books):
    def __init__(self, title, author, page ,price):
        super().__init__(title, author, page)
        self.price =price

    def info(self):
        return f"Title : {self.title} , Author : {self.author} , Page : {self.page} , Price: {self.price}"

    def in_expensive(self):
        return self.price >=200

other_book = PriceBooks("War and Peace", "Leo Tolstoy", 230, 680)
another_book = PriceBooks("The Life of Prophet Muhammad S.A.W", "Martin Lings", 450, 890)

print(other_book.info())
print(f"Author: {other_book.author} ")
print(f"Title: {other_book.title}")
print(f"Price: {other_book.price}")
print(f"Page: {other_book.page}")


print(another_book.info())
print(f"Author: {another_book.author}")
print(f"Title: {another_book.title}")
print(f"Price: {another_book.price}")
print(f"Page: {another_book.page}")


