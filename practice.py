class Books():

    def __init__(self, titel ,auther ,page):
        self.titel = titel
        self.auther = auther
        self.page = page

    def info(self):
        return f"Titel :{self.titel}, Auther :{self.auther}, Pages :{self.page}"
    
    def in_long_page(self):
        return self.page > 120
    
new_book =Books("The Great Boy" ,"L .Scott fitzgertlad",127 )
book_another =Books("War and Peace" ,"Leo Tolstoy" ,689)

print(new_book.info())
print(new_book.in_long_page())

print(book_another.info())
print(book_another.in_long_page())