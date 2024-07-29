##############design#######################


#
# class Car:
#
#     def __init__(self, model, marka, color, ful_up):
#         self.model = model
#         self.marka = marka
#         self.color = color
#         self.ful_up = ful_up
#
#
#     def start(self):
#         print(f"{self.model} {self.marka} is starting!")
#     def move(self):
#         print(f"{self.model} {self.marka}is moving!")
#     def stop(self):
#         print(f"{self.model} {self.marka} is stoping!")
#     def full_up(self):
#         print(f"{self.model} {self.marka} is petrol!\n")
#     def display(self):
#         print()
#
#
#
# mers = Car("MERS","w220", "write", "benzin")
# bmw = Car("BMW", "f90", "Black", "gas")
# bmw.start()
# bmw.move()
# bmw.stop()
# bmw.full_up()
#
#
# mers.start()
# mers.move()
# mers.stop()
# mers.full_up()



class Car:

    def __init__(self, model, marka, color, ful_up):
        self.__model = model
        self.__marka = marka
        self.__color = color
        self.ful_up = ful_up



    def get_color(self):
        return self.__color
    def get_model(self):
        return self.__model

    def set_color(self, new_color):
        self.__color = new_color

    def start(self):
        print(f"{self.__model} - {self.__marka} is starting!")
    def move(self):
        print(f"{self.__model} {self.__marka}is moving!")
    def stop(self):
        print(f"{self.__model} {self.__marka} is stoping!")
    def full_up(self):
        print(f"{self.__model} {self.__marka} is petrol!\n")
    def display(self):
        print(f"model : {self.__model}\n"
              f"marka : {self.__marka}\n"
              f"color : {self.__color}\n"
              )



mers = Car("MERS","w220", "write", "benzin")
bmw = Car("BMW", "f90", "Black", "gas")





mers.start()


print(mers.get_color())

mers.set_color("writttttttttt")

print(mers.get_model())

mers.display()




# class Car:
#     model = "BMW"
#     marka = "e60"
#     year = 2011
#     color = "Black"
#
#     def start(self):
#         print(f"{self.model} is starting!")
#     def move(self):
#         print(f"{self.model} is moving!")
#     def stop(self):
#         print(f"{self.model} is stoping!")
# bmw_e60 = Car()
# bmw_e60.start()
#
# bmw_e60.move()
# bmw_e60.stop()

#
#
#
#
# class Technique:
#     def __init__(self, model, marka, color, price):
#         self.__model = model
#         self.__marka = marka
#         self.__c = color
#         self.__p = price
#     def set_p(self, n_price):
#         self.__p = n_price
#     def get_model(self):
#         print(self.__model)
#
#     def start(self, type):
#         print(f"{self.__model} вкдючается!! за {type} секунд\n")
#     def change(self, type):
#         print(f"{self.__model} на зарядке его зарядка мощности {type}\n")
#     def year(self, type):
#         print(f"этому ноутбуку всего то {type} \n")
#     def prices(self, type):
#         print(f"цена ее было на момент выхода было {type} сейчас же {self.__p}\n  ")
#
#     def info(self):
#         print(f"model : {self.__model}\n"
#               f"marka : {self.__marka}\n"
#               f"color : {self.__c}\n"
#               f"price : {self.__p}\n"
#               )
#
# lenevo = Technique("lenovo","Ideapad 5i","silver","83000som")
# lenevo.get_model()
#
# lenevo.get_model = "Acer"
#
# lenevo.set_p("90000som")
#
# lenevo.start(20)
#
# lenevo.info()
#
# lenevo.year("год")
#
#
# lenevo.prices("93000som")
#







##################### OOP ################
#
# class Calculator:
#     def __init__(self, number1, operation, number2):
#
#         self.__a = number1
#         self.__oper = operation
#         self.__b = number2
#
#     def get_a(self):
#         return self.__a
#     def get_oper(self):
#         return self.__oper
#     def get_b(self):
#         return self.__b
#
#
#
#     def set_a(self, new_a):
#         self.__a = new_a
#     def set_oper(self, new_oper):
#         self.__oper = new_oper
#     def set_B(self, new_b):
#         self.__b = new_b
#
#
#
#
#     def plus(self):
#         result = self.get_a() + self.get_b()
#         print(f"кошулду : {result}")
#     def minus(self):
#         result = self.get_a() - self.get_b()
#         print(f"кемитилди :{result}")
#     def koboity(self):
#         result = self.get_a() * self.get_b()
#         print(f"кобойтулду :{result}")
#     def bolyy(self):
#         result = self.get_a() / self.get_b()
#         print(f"болунду:{result}")
#
#
#
#     def oper(self):
#         if self.get_oper() == "+":
#             self.plus()
#         elif self.get_oper() == "-":
#             self.minus()
#         elif self.get_oper() == "*":
#             self.koboity()
#         elif self.get_oper() == "/":
#             self.bolyy()
#         else:
#             print("сен операцияны туура эмес бердин")
#
# c = Calculator(10, "*", 200)
# c.oper()
#

#
#
# getter
# setter
# метод проголатывание
#
#
# class Employee:
#     emp = 0
#     def __init__(self, name, salary, opyto):
#         self.__name = name
#         self.__salary = salary
#         self.__opyt = opyto
#         Employee.emp = Employee.emp  + 1
#
#     def set_salary(self, new_salary):
#         self.__salary = new_salary
#     def set_opyt(self, new_opyt):
#         self.__opyt = new_opyt
#     def get_name(self):
#         return self.__name
#
#     def display_e(self):
#         print(f"Аты: {self.__name}\n"
#               f"Айлык: {self.__salary}")
#
#     def experience(self, s):
#         if self.__opyt < 1:
#             print(f"{self.__name}{s} стажы бир жылга жете элек \n")
#         elif self.__opyt <=2 and self.__opyt >= 1:
#             print(f"{self.__name}{s} стажы эки жыл\n")
#         elif self.__opyt <= 5 and self.__opyt >= 3:
#             print(f"{self.__name}{s} cтажы беш жыл\n")
#         else:
#             print(f"{self.__name}{s} стажы 5 жылдан ашкан\n")
#
# emp1 = Employee("Айбек", 19900, 10)
# emp2 = Employee("Азема", 9000, 5)
# emp3 = Employee("Бегимай",15500,6)
# emp4 = Employee("Айжан",11000,1)
#
# emp1.set_salary(34000) #Айбек
# emp4.set_opyt(2) #Айжан
#
# emp1.display_e()#Айбек
# emp1.experience("тин")#Айбек+тин
#
# print(emp2.get_name())#Азема
#
# emp2.display_e()#Азема
# emp2.experience("нын")#Азема+нын
#
# emp4.display_e()
# emp4.experience("дын")
#
# print(f"Сотрудниктин саны :{Employee.emp}










