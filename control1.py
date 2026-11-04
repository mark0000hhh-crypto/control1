# class animal: -----------------------------------------------> первое и второе задание вместе
#     def __init__(self, name , age):
#         self.name = name 
#         self.age = age

#     def make_sound(self):
#         print(f"{self.name} издает звук")

# class dog(animal):
#     def make_sound(self):
#         print(f"{self.name} гавкает")

# class cat(animal):
#     def make_sound(self):
#         print(f"{self.name} мяукает")

# puppy = dog("barbos", 12)
# kitten = cat("murzila", 2)


# puppy.make_sound()
# kitten.make_sound()

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name 
        self._age = age

    @abstractmethod
    def make_sound(self):
        pass

    def get_age(self):
        return self._age


    def __str__(self):
        return f"Имя: {self.name}, возраст: {self._age}"

    def __len__(self):
        return len(self.name)

    @staticmethod
    def is_adult(age):
        return age >= 1


class Dog(Animal):
    def make_sound(self):
        print("Гав!")


class Cat(Animal):
    def make_sound(self):
        print("Мяу!")



dog_v = Dog("Шарик", 3)
print(dog_v)                          
print(f"Длина имени: {len(dog_v)}")   
print(f"Взрослый? {Animal.is_adult(dog_v.get_age())}") 