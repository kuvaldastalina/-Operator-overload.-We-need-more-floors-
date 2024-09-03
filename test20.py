class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f"В доме {self.name} не сеществует этажа под № {new_floor}")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __ed__(self, other):
        return self.name == other.name and self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors < other.number_of_floors or self.number_of_floors == other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors > other.number_of_floors or self.number_of_floors == other.number_of_floors

    def __ne__(self, other):
        return self.name != other.name and self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        return self.number_of_floors





x = House('"ЖК Эльбрус"', 30)
y = House('"Домик в деревне"', 2)
x.go_to(12)
y.go_to(7)

x = House('ЖК Эльбрус', 10)
y = House('ЖК Акация', 20)


# __str__
print(x)
print(y)

# __len__
print(len(x))
print(len(y))

print(x == y)
print(x < y)
print(x <= y)
print(x > y)
print(x >= y)
print(x != y)

x += 10  # __iadd__
print(x)

x = y + x  # __radd__
print(x)