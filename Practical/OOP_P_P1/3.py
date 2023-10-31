# Створіть клас Book з атрибутами title (назва
# книги), author (автор) та genre (жанр). Додайте метод
# display_info, який виведе інформацію про книгу у
# вигляді "Назва: {title}, Автор: {author}, Жанр: {genre}".

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


books = [Book(b['title'], b['author'], b['genre']) for b in generate_data()]

[b.display_info() for b in books]
