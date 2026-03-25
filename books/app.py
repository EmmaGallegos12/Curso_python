from flask import Flask, render_template, request
from Book import load_books
from book_function import create_author_dictionary

app = Flask(__name__)

filename = 'booklist2000.csv'
books = load_books(filename)
author_dict = create_author_dictionary(books)

# Populate author_dict for efficient searching
author_dict = {}
for book in books:
    author_lower = book.author.lower()
    if author_lower not in author_dict:
        author_dict[author_lower] = []
    author_dict[author_lower].append(book)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_by_author', methods=['GET', 'POST'])
def search_by_author():
    if request.method == 'POST':
        author = request.form['author']
        book_list = author_dict.get(author.lower(), [])
        return render_template('search_by_author.html', books_list=book_list)
    else:
        return render_template('search_by_author.html', books_list=books[:10])

if __name__ == '__main__':
    app.run(debug=True)
