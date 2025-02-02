class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages
    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Кол-во страниц должно быть целым числом")
        if value < 0:
            raise ValueError("Кол-во страниц не может быть меньше 0")
        self._pages = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Страниц {self.pages}"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        self.duration = duration
        super().__init__(name, author)

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float):
            raise ValueError("Длительность должна быть числом.")
        if value < 0:
            raise ValueError("Длительность не может быть отрицательной.")
        self._duration = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"

