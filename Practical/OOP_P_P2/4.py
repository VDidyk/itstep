# До вже реалізованого класу «Книга» додайте
# необхідні перевантажені методи та оператори.

def generate_data() -> list:
    return [{'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'genre': 'Classic'},
            {'title': '1984', 'author': 'George Orwell', 'genre': 'Dystopian'},
            {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'genre': 'Romance'},
            {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'genre': 'Classic'},
            {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'genre': 'Literary Fiction'},
            {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'genre': 'Fantasy'},
            {'title': 'The Diary of a Young Girl', 'author': 'Anne Frank', 'genre': 'Biography'},
            {'title': 'Moby Dick', 'author': 'Herman Melville', 'genre': 'Adventure'},
            {'title': 'War and Peace', 'author': 'Leo Tolstoy', 'genre': 'Historical Fiction'},
            {'title': 'The Divine Comedy', 'author': 'Dante Alighieri', 'genre': 'Epic Poetry'},
            {'title': 'Beloved', 'author': 'Toni Morrison', 'genre': 'Historical Fiction'},
            {'title': 'Invisible Man', 'author': 'Ralph Ellison', 'genre': 'Literary Fiction'},
            {'title': 'Don Quixote', 'author': 'Miguel de Cervantes', 'genre': 'Classic'},
            {'title': 'The Odyssey', 'author': 'Homer', 'genre': 'Epic Poetry'},
            {'title': 'Crime and Punishment', 'author': 'Fyodor Dostoevsky', 'genre': 'Philosophical Fiction'},
            {'title': 'Jane Eyre', 'author': 'Charlotte Brontë', 'genre': 'Gothic Fiction'},
            {'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien', 'genre': 'Fantasy'},
            {'title': 'The Brothers Karamazov', 'author': 'Fyodor Dostoevsky', 'genre': 'Philosophical Fiction'},
            {'title': 'Wuthering Heights', 'author': 'Emily Brontë', 'genre': 'Gothic Fiction'}]


class Book:
    def __init__(self, title: str, author: str, genre: str):
        self._title = title
        self._author = author
        self._genre = genre

    def display_info(self):
        print(f"Назва: {self._title}, Автор: {self._author}, Жанр: {self._genre}")

    def __str__(self):
        return f"'{self._title}' by {self._author}"

    def __repr__(self):
        return f"Book(title='{self._title}', author='{self._author}', genre='{self._genre}')"

    def __eq__(self, other):
        return (self._title, self._author, self._genre) == (other._title, other._author, other._genre)


books = [Book(b['title'], b['author'], b['genre']) for b in generate_data()]

[b.display_info() for b in books]

print(books[0])
print(repr(books[1]))

print(books[0] == books[1])
