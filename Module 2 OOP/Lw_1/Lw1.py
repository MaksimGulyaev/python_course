# TODO Написать 3 класса с документацией и аннотацией типов
class Tree:
    """
    Документация на класс Tree.
    Класс описывает модель дерева.
    """
    def __init__(self, age: int, fruits: int):
        """
        Инициализация экземпляра класса.

        :param age: Возраст дерева.
        :param fruits: Количество фруктов

        Пример:
        >>> apple_tree = Tree(15, 20)    # Инициализация экземпляра класса
        """
        self.age = age
        if age <= 0:
            raise ValueError("Возраст дерева не может быть отрицательным числом")

        self.fruits = fruits
        if not isinstance(fruits, int):
            raise TypeError("Количество фруктов должно быть типа int")


    def calc_age(self) -> int:
        """Метод увеличивает возраст дерева."""
        ...
    def pick_fruits(self, pick_act: int) -> int:
        """
        Метод суммирует собранные фрукты.
        :param pick_act: Количество уже собранных фруктов

        Пример:
        >>> apple_tree = Tree(30, 18)
        >>> apple_tree.pick_fruits(22)
        """
        ...


class Woodpecker:
    """
    Документация на класс Woodpecker.
    Класс описывает модель дятла.
    """
    def __init__(self, age: int, beaks_per_minute: int,):
        """
        Инициализация экземпляра класса

        :param beaks_per_minute: Количество ударов клювом в минуту
        :param age: Возраст дятла

        Пример:
        >>> Coock = Woodpecker(3, 18)    # Инициализация экземпляра класса
        """
        self.beaks_per_minute = beaks_per_minute
        if beaks_per_minute < 0:
            raise ValueError("Количество ударов клювом в минуту не может быть отрицательным числом")

        self.age = age
        if age <= 0:
            raise ValueError("Возраст дятля не может быть отрицательным числом")

    def modify_beaks_per_minute(self, delta: int) -> int:
        """
        Метод изменяет количество ударов в минуту.
        :param delta: Значение, на которое необходимо изменить количество ударов клювом в минуту
        """
        ...
    def up_age(self) -> int:
        """
        Метод увеличивает возраст дятла
        """
        ...

class Mug:
    """
    Документация на класс Mug.
    Класс описывает модель кружки.
    """
    def __init__(self, mug_form: str, mug_volume: int):
        """
        Инициализация экземпляра класса

        :param mug_form: Форма кружки
        :param mug_volume: Объём кружки

        Пример:
        >>> mug1 = Mug("Стеклянный высокий бокал", 300)   #инициализация экземпляра класса
        """
        self.mug_form = mug_form
        if not isinstance(mug_form, str):
            raise TypeError("Форма кружки должна быть типа str")

        self.mug_volume = mug_volume
        if mug_volume <= 0:
            raise ValueError("Объём кружки не может быть отрицательным числом")

    def rename_form(self) -> str:
        """Метод изменяет форму кружки"""
        ...
    def mod_vol(self) -> int:
        """Метод изменяет объём кружки"""
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
    pass