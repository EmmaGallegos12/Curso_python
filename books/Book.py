import csv
import os

class Book:
    def __init__(self, id, image_name, image_url, title, author, genre_id, genre):
        self.id = str(id)
        self.image_name = image_name
        self.image_url = image_url
        self.title = title
        self.author = author
        self.genre_id = int(genre_id)
        self.genre = genre

    def __str__(self):
        return f"{self.title:<50} by {self.author:<20} - Genre: {self.genre}"

    def __repr__(self):
        return f"Book(id='{self.id}', title='{self.title}', author='{self.author}', genre='{self.genre}')"

    def to_dict(self):
        return {
            'id': self.id,
            'image_name': self.image_name,
            'image_url': self.image_url,
            'title': self.title,
            'author': self.author,
            'genre_id': self.genre_id,
            'genre': self.genre
        }

def load_books(filename:str):
        # Implementar la lógica para cargar datos desde un archivo CSV
        books = []
        if not os.path.isabs(filename):
            base_path = os.path.dirname(__file__)
            filename = os.path.join(base_path, filename)
            
        with open(filename, 'r', encoding='utf-8') as file: 
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 7:
                    books.append(Book(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

        return books

if __name__ == "__main__":
    book = Book(1, "Dune.jpg", "https://m.media_amazon.com/images/I/81Ua99CURsL._SL1500_.jpg", "Dune", "Frank Herbert", 1, "Science Fiction")
    print(book)

    books = load_books("booklist2000.csv")
    if books:
        print(f"Loaded {len(books)} books.")
        print(f"Example book: {books[3]}")
    else:
        print("No books loaded.")