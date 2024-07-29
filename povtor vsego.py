# class Human:
#     def __init__(self, name, nationality, hobby, age ):
#         self.__name = name
#         self.__na = nationality
#         self.__hobby = hobby
#         self.__age = age
#
#
#     def sleep(self):
#         print(f"{self.__name} спит")
#
#     def nsleep(self):
#         print(f"{self.__name} проснулся")
#
#     def breakfast(self):
#         print(f"{self.__name} завтракает")
#
#     def have_fun(self, s):
#         print(f"{self.__name} пошел веселится  в {s}" )
#
#     def dream(self, s):
#         print(f"{self.__name} хочет {s}\n")
#
#
# class Teacher(Human):
#     def __init__(self, name, nationality, hobby, age, job, rank):
#         super().__init__(name, nationality, hobby, age)
#         self.__job = job
#         self.__rank = rank
#
#
#     def worktime(self, a, s):
#         print(f"У {self.name}{a} работа начинается в {s}")
#
#     def lesson(self, s):
#         print(f"{self.name} ведет урок в {s}")
#
#     def nworktime(self, s):
#         print(F"И заканчивается в {s}")
#
#
# class Student(Human):
#     def __init__(self, name, nationality, hobby, age,  job, courses):
#         super().__init__(name, nationality, hobby, age,)
#         self.__job = job
#         self.__cour = courses
#
#
#     def college(self, s):
#         print(f"{self.name} учиться в {s}")
#
#     def work(self, s):
#         print(f"{self.name} работает {s} ")
#
#
# aibek = Human("Айбек","Ыссык-кол", "плавать", 19)
# azema = Teacher("Азема","Бишкек","Рисовать", 23, "Учитель", "Завуч")
# nurtilek = Student("Нуртилек","Баткен", "Футбол", 16, "-", "-")
#
#
# aibek.sleep()
# aibek.nsleep()
# aibek.dream("Катамаран")
#
# azema.lesson("Университете")
# azema.dream("стат Ректором")
#
# nurtilek.have_fun("Аква парк")
# nurtilek.college("Техникуме"





#
# def add(a : int, b : int):
#     return a * b
#
#
#
# def add(a : str, b : str):
#     return  f"{a}  {b}"
#
# def add(a : float, b : float):
#     return round(a * b, 3)
# if __name__ == '__main__':
#     add(1, 1)

#
#
# class Animal:
#     def make_voice(self):
#         print(f"Animal is voice")
#
#
#
#
# class Cat(Animal):
#     def make_voice(self):
#         print("Meaw-meaw")
#
#
#
# class Dog(Animal):
#     def make_voice(self):
#         print("Gaf-gaf")
#
#
# def voice(animal: Animal):
#     animal.make_voice()
#
# if __name__ == "__main__":
#     voice(Dog())
#     voice(Cat())

#
# from abc import ABC, abstractmethod
# import math
#
# class Shape(ABC):#Фигура
#     @ abstractmethod
#     def calculator_area(self):
#         pass
#
# class Roctangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def calculator_area(self):
#         return self.length * self.width
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculator_area(self):
#         return math.pi * self.radius ** 2
#
#
# ractangle = Roctangle(4, 5)
# circle = Circle(3)
# print("Плошадь прямоуголника",ractangle.calculator_area())
# print("Площад круга:", circle.calculator_area())







from abc import ABC, abstractmethod

class Vahicle(ABC):
    def __init__(self, marka, color, weight):
        self.marka = marka
        self.color = color
        self.weight = weight
    def drive(self):
        pass


class Car(Vahicle):
    def __init__(self, marka, color, weight,  model):
        super().__init__(marka, color, weight)
        self.model = model
    def drive(self):
        return f"{self.marka} is driving"


class Bicycle(Vahicle):
    def __init__(self, marka, color, weight):
        super().__init__(marka, color, weight)
    def drive(self):
        return f"{self.marka} is moving"


class Boat(Vahicle):
    def __init__(self, marka, color, weight, size ):
        super().__init__(marka, color, weight,)
        self.size = size
    def drive(self):
        return f"{self.marka} is sailing"


car = Car("Mers", "write",1500, "w220")
bycycle = Bicycle("road bike", "blue",9)
boat = Boat("Raft", "write",90, "120х95х50")


print(car.drive())
print(bycycle.drive())
print(boat.drive())









