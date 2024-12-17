class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if not (1 <= new_floor <= self.number_of_floors):
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

h1 = House('ЖК Эльбрус',30)
h2 = House('Домик в деревне',2)
h1.go_to(7)
h2.go_to(4)