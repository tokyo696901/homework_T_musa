class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def display_info(self):
        print(f"Название: {self.title}, Автор: {self.author}, Год издания: {self.year}, Количество страниц: {self.pages}")

    def change_pages(self, new_pages):
        self.pages = new_pages

    def __str__(self):
        return f"{self.title}, {self.author}, {self.year}, {self.pages} страниц"

book1 = Book("Война и мир", "Лев Толстой", 1869, 1225)
book2 = Book("1984", "Джордж Оруэлл", 1949, 328)

book1.display_info()
book2.display_info()

book1.change_pages(1300)
book1.display_info()

print(str(book2))
