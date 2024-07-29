
#
# class Animals:
#
#     def __init__(self, name, breed, weight, color):
#         self.name = name
#         self.breed = breed
#         self.weight = weight
#         self.color = color
#
#
#
#
#     def sleep(self):
#         print(f"{self.breed} {self.name} sleep !")
#     def nsleep(self):
#         print(f"{self.breed} {self.name}  woke up from sleep!")
#     def start(self, s,type):
#         print(f"{self.breed} {self.name}  {s} after {type} ")
#     def eat(self, type):
#         print(f"{self.breed} {self.name} eating  {type}\n\n\n\n")
#
#
#
# bear = Animals("bear","polar", "450kg", "write")
# tiger = Animals("tiger", "bengal", "260kg", "dark brown")
# tiger.sleep()
# tiger.nsleep()
# tiger.start("runs","monkey")
# tiger.eat("monkey")
#
#
#
#
#
# bear.sleep()
# bear.nsleep()
# bear.start("floats","warlus")
# bear.eat("warlus")




#
#
# class Humans:
#
#     def __init__(self, name, profession_or_hobby, weight, nationality):
#         self.name = name
#         self.p = profession_or_hobby
#         self.weight = weight
#         self.w = nationality
#
#
#
#
#     def sleep(self):
#         print(f" {self.name} спит!\n ")
#     def nsleep(self, s, type):
#         print(f" {self.name}  проснулься в {s} чтобы {type}!\n ")
#     def start(self,s,  type):
#         print(f" {s} {self.name}   поехал в  {type} \n")
#     def wo(self, type):
#         print(f" {self.name} поехал на {type}\n")
#     def dos(self, type, s):
#         print(f"Он вернулься домой в {type} и пошел{s} спать\n")
#
#
#
# Mike = Humans(" Майк","боддибилдинг", "105кг", "Американец")
# Aibek = Humans("Айбек", "плавать", "60кг", "Ыссык-кол")
#
#
#
# Mike.nsleep("8","сделать утреннию зарядку")
# Mike.start("потом ","спорт зал")
# Mike.wo("волмарт")
# Mike.dos("22:00", "")
#

class Animal:
    def __init__(self, color , weight, food):
        self.c = color
        self.w = weight
        self.f = food

    def move(self):
        print(f"{self.name} is moving!!!")
    def eat(self):
        print(f"Animal is eating!!!")
    def drink(self):
        print(f"Animal is drinking")





class Dog(Animal):
    def __init__(self, color, weight, food, name, age):
        super().__init__(color, weight, food)
        self.name = name
        self.age = age

    def voice(self):
        print("Gav-Gav")


Tuzik = Dog("black",19,"meat", "Tuzik", 2)
Tuzik.move()


class Cat(Animal):
    def __init__(self, color, weight, food, name, age):
        super().__init__(color, weight, food)
        self.name = name
        self.age = age


    def voice(self):
        print(f"Meaw-meaw")


    def tree(self):
        print(f"{self.name} climbed tree ")


Murka = Cat("write",2,"mouse","Murka", 1)

Murka.move()
Murka.voice()




