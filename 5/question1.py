class Book():
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"""Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"""


ru_book = Book("Преступление и наказание", "Ф.М.Достоевский", 1866)
print(ru_book.get_info())
