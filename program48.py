books = []
books.append("Asif")
books.append("Rana")
books.append("karim")
print(books)
books.pop()
print("Top book is",books[-1])
books.pop()
print("Top book is",books[-1])
books.pop()
if not books:
    print("No Books Available")
    