# Базовый класс Transport
class Transport:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self):
        return f"Транспорт {self.name} движется со скоростью {self.speed} км/ч"



class Car(Transport):
    def move(self):
        return f"Машина {self.name} едет со скоростью {self.speed} км/ч по дороге."

    def refuel(self):
        return f"Машина {self.name} заправляется топливом."



class Bicycle(Transport):
    def move(self):
        return f"Велосипед {self.name} едет со скоростью {self.speed} км/ч по велосипедной дорожке."

    def ring_bell(self):
        водитель = f"Велосипед {self.name}: Дзынь-дзынь!"
        return водитель

class Airplane(Transport):
    def move(self):
        return f"Самолёт {self.name} летит со скоростью {self.speed} км/ч в небе."

    def take_off(self):
        return f"Самолёт {self.name} успешно взлетел!"


Car = Car("Land Cruiser 540", 80)
Bicycle = Bicycle("Stels", 20)
Plane = Airplane("Boeing 737", 850)


transport_list = [Car, Bicycle, Plane]

for t in transport_list:
    print(t.move())

print(Car.refuel())
print(Bicycle.ring_bell())
print(Plane.take_off())
