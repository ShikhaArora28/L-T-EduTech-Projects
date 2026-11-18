Title = input("Enter the title: ")
Auth = input("Enter the author name: ")
Page = int(input("Enter no of pages: "))
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print("Title :", self.title)
        print("Author:", self.author)
        print("Pages :", self.pages)


# Example usage
book1 = Book(Title, Auth , Page)
book1.display_info()