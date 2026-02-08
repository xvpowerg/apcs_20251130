class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def __str__(self):
        return f"{self.title}:{self.author}:{self.price}"

books = [Book("Java","Ken",500),
         Book("C#","Iris",600),
         Book("Pythn","Joy",800),
         Book("Golan","Sean",400)]
for b in books:
    print(b)
