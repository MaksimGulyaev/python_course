if __name__ == "__main__":
    class Car:
        """Базовый класс Автомобиль.
        Содержит в себе информацию о бренде и модели автомобиля."""

        def __init__(self, brand: str, model: str):
            """Инициализация экземпляра класса.
            :param brand: Автомобильный бренд.
            :param model: Модель автомобиля."""
            self.brand = brand
            self.model = model

        def __str__(self):
            return f"Автомобиль {self.brand}. Модель {self.model}"

        def __repr__(self):
            return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r})"

        def recognition(self):
            """Метод выводит текстовое обозначение отношения к автомобилям."""
            print("Мне нравятся машины")

        def BrandName(self):
            """Метод выводит название бренда с использованием функции print"""
            print(f"{self.brand}")


    class Pickup(Car):
        """Дочерний класс Пикап.
        Помимо информации о бренде и модели автомобиля содержит в себе
        значение объёма багажника (я, честно, не придумал более весомое различие)."""

        def __init__(self, brand: str, model: str, vol_bool: int):
            super().__init__(brand, model)
            self.vol_bool = vol_bool

            super().recognition(self)
            """Метод, унаследованный из основного класса.
            Его содержание не изменяется в дочерних классах."""

        def __str__(self):
            return f"Автомобиль {self.brand}. Модель {self.model}. Объём багажника {self.vol_bool}"

        def __repr__(self):
            return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, Объём багажника={self.vol_bool!r})"

        def BrandName(self):
            """Метод, перегруженный из базового класса.
            Это было введено для обозначения различий между экземплярами разных дочерних классов.
            Различные типы кузова имеют разные двигатели и выхлопные системы,
            поэтому издают разные звуки."""
            print(f"{self.brand} {self.model} is bububu")


    class Sport_Coupe(Car):
        """Дочерний класс Спорт-купе.
        Помимо информации о бренде и модели автомобиля содержит в себе информацию
        о мощности в лошадиных силах."""

        def __init__(self, brand: str, model: str, horsepower: int):
            super().__init__(brand, model)
            self.horsepower = horsepower

        @property
        def horsepower(self):
            return self._horsepower

        @horsepower.setter
        def horsepower(self, value):
            """В этом методе мы пишем проверки атрибута horsepower.
            Вводимое значение должно быть целым и неотрицательным.
            К тому же, значение атрибута не должно изменяться."""
            if not isinstance(value, int):
                raise ValueError("Кол-во лошадиных сил должно быть целым числом")
            if value < 0:
                raise ValueError("Кол-во лошадиных сил не может быть меньше 0")
            self._horsepower = value

            super().recognition(self)
            """Метод, унаследованный из основного класса.
            Его содержание не изменяется в дочерних классах."""

        def __str__(self):
            return f"Автомобиль {self.brand}. Модель {self.model}. Мощность {self.horsepower}."

        def __repr__(self):
            return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, horsepower={self.horsepower!r})"

        def BrandName(self):
            """Метод, перегруженный из базового класса.
            Это было введено для обозначения различий между экземплярами разных дочерних классов.
            Различные типы кузова имеют разные двигатели и выхлопные системы,
            поэтому издают разные звуки."""
            print(f"{self.brand} {self.model} is sututu")
    pass












