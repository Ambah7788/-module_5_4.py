class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1:
            return f"Этаж {new_floor} не существует. Пожалуйста, выберите этаж от 1 до {self.number_of_floors}."
        elif new_floor > self.number_of_floors:
            return f"Этаж {new_floor} не существует. Пожалуйста, выберите этаж от 1 до {self.number_of_floors}."
        else:
            return f"Вы находитесь на этаже {new_floor} в доме '{self.name}'."

my_house = House("Солнечный дом", 5)

result = my_house.go_to(3)
print(result)

result_invalid = my_house.go_to(6)
print(result_invalid)


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        """Возвращает количество этажей в здании."""
        return self.number_of_floors

    def __str__(self):
        """Возвращает строковое представление объекта House."""
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

house = House("Сосновый бор", 3)
print(len(house))
print(house)


class Building:
    def __init__(self, floors):
        if floors < 0:
            raise ValueError("Количиство этажей не может быть отрицательным.")
        self.floors = floors


        def __eq__(self, other):
            if isinstance(other, Building):
                return self.floors == other.floors
            return NotImplemented


        def __lt__(self, other):
            if isinstance(other,Building):
                return self.floors < other.floors
            return NotImplemented



        def __le__(self, other):
            if isinstance(other,Building):
                return self.floors <= other.floors
            return NotImplemented



        def __gt__(self, other):
            if isinstance(other,Building):
                return self.floors > other.floors
            return NotImplemented




        def __ge__(self, other):
            if isinstance(other,Building):
                return self.floors >= other.floors
            return NotImplemented



        def __ne__(self, other):
            if isinstance(other, Building):
                return other.floors != other.floors
            return NotImplemented



        def __add__(self, value):
            if not isinstance(value, int) or value < 0:
                raise ValueError("Значение должно быть неотрицательным целым числом.")
        self.floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __repr__(self):
        return f"Building(floors={self.floors})"


class House:
    houses_history = []  # Атрибут класса для хранения истории зданий

    def __new__(cls, *args, **kwargs):
        instance = super(House, cls).__new__(cls)

        if args:
            house_name = args[0]  # Название дома из args
            cls.houses_history.append(house_name)

        return instance

    def __init__(self, *args, **kwargs):
        self.first = args[0] if args else None  # Название дома
        self.second = kwargs.get('second', None)  # Второй аргумент
        self.third = kwargs.get('third', None)  # Третий аргумент

    def __del__(self):
        print(f"{self.first} снесён, но он останется в истории")


if __name__ == "__main__":
    house1 = House("Дом на берегу", second=25, third=3.14)
    house2 = House("Коттедж в лесу", second=30, third=2.71)

    print("История построенных домов:", House.houses_history)

    del house1
    del house2

    print("История построенных домов после удаления:", House.houses_history)