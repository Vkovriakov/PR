class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    @property
    def model(self):
        return f"Модель: {self.__model}"

    @property
    def horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    @property
    def color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.model)
        print(self.horsepower)
        print(self.color)
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)

vehicle1 = Sedan('Vitalii', 'Chevrolet Cobalt', 'blue', 105)

vehicle1.print_info()

vehicle1.set_color('Yellow')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Valentin'

vehicle1.print_info()