#Tusk1
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed

# Створимо об'єкт класу Car
my_car = Car(make="Toyota", model="Camry", year=2022)

# Виконаємо метод accelerate п'ять разів
for _ in range(5):
    my_car.accelerate()
    print(f"Поточна швидкість: {my_car.get_speed()} км/год")

# Виконаємо метод brake п'ять разів
for _ in range(5):
    my_car.brake()
    print(f"Поточна швидкість: {my_car.get_speed()} км/год")
#Tusk2
class Buffer:
    def __init__(self):
        self.sequence = []

    def add(self, *a):
        self.sequence.extend(a)
        while len(self.sequence) >= 5:
            print(f"Сума п'ятірки: {sum(self.sequence[:5])}")
            self.sequence = self.sequence[5:]

    def get_current_part(self):
        return self.sequence

# Приклад використання:
buffer = Buffer()
buffer.add(1, 2, 3)
buffer.add(4, 5, 6, 7, 8)
buffer.add(9)
print("Поточна частина послідовності:", buffer.get_current_part())
