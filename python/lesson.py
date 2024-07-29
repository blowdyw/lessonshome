# def a(*args):
#     return   args < 60
#
#
#
# print(a(x))
#

# def sum(*args):
#     i = 0
#     for j in args:
#         i = i * j
#         return i
#         print(sum(6, 2))
#
#
#
# #
# # def sum(*args):
#     i = 1
#     for j in args:
#         i = i * j
#     return i
# print(sum(3, 2))
#
#
#
#
#
#
# def b(my_list):
#     result = []
#     i = 0
#     for i in my_list:
#         result.append(i)
#     return i
# if i < 60:
#     print(b(1))
#
# my_list = []

#
# def sum(my_list):
#     result = []
#     for element in my_list:
#         if element < 60:
#             result.append(element)
#     return result
#
#
#
# my_list = [1, 2,3,45, 23, 32, 12, 21,45, 45345, 456, 59]
# result = sum(my_list)
# print(result)



#
# def s(my_list):
#     result = my_list[0] + my_list[-1]
#     return result
#
#
#
#
#
# my_list = [1, 2,3,45, 23, 32, 12, 2,4, 5, 6, 9]
# result = s(my_list)
# print(result)
#
#
#
#







#
# def dic(my_info):
#
#
#
#
#
#
#
#
# my_info = { name : " Bektursun",
#             surname: "Asankojoev"}




# def f(n):
#     if n == 1:
#         return 1
#     return n**2 * f(n - 1)
#
# print(f(5))
#
#

#
#
# #
#
# def compare_numbers(a, b):
#     if a > b:
#         return "a chon b karaganda"
#     elif b > a:
#         return "b chon  a karaganda "
#     else:
#         return "a menen b ten"
#
# a = int(input("a:"))
# b = int(input("b::"))
# result = compare_numbers(a, b)
# print(result)





# def three(a, b, c):
#     if a > b and a > c:
#         print( "a чон баарынан")
#     elif b > a and b > c:
#         print("b чон баарынан")
#     elif c > a and c > b:
#         print(  "c чон баарынан")
#     elif b < a and b < c:
#         print("b баарынан кичине")
#     elif a < b and a < c:
#         print("a баарынан кичине")
#     elif c < b and c < a:
#         print("c баарынан кичине")
#
#     if a == b and a != c:
#         print("a менен b тен ")
#     elif b == a and b != c:
#         print("a менен c тен  ")
#     elif c == a and c != b:
#         print( "a менен c тен  ")
#     elif c == b and c != a:
#         print( "c менен b тен  ")
#     else:
#         print( "маселеде  баары тен же тен сан жок")
#
# a = int(input("a:"))
# b = int(input("b:"))
# c = int (input("c:"))
# three(a,b,c)






# def my_infon(name):
#     my_info= {"name" : name}
#     result = my_info
#     return result
# m=my_infon("BEKA")
# print(m)
#

#
#
#
# def my_info(name):
#     result = name
#     return result
#
# m=my_info(name="Bektursun")
# print(m)
#
#
#
#
# def my_info(name):
#     my_info(name)
#     return my_info(name)
#
# m=my_info(name="Bektursun")
# print(m)








#def com(a, b, c):
#
#     if a > b:
#         print(" a chon ")
#     elif b > a:
#         print(" b chon ")
#     else:
#         print(" a jana b ten")
#
#
#     if a > c:
#         print("a chon ")
#     elif c > a:
#         print("c chon ")
#     else:
#         print(" a jana c ten")
#
#
# a = int(input("a"))
# b = int(input("b"))
# c = int(input("c"))
# com(a, b, c)
#
# #
#
#
# def f (n):
#     print(n)
#     if n == 1 :
#         return 0
#     return f(n-1)
#
# print(f(100))
#
# #
# def f (n):
#     if n == 0:
#         return 1
#     i = 0
#     while i <= n:
#         print(i)
#         i = i + 1
#
# print(f(100))





# def f (n):
#     print(n)
#     if n == 99:
#         return 100
#     return f(n+1)
#
# print(f(1))
#
#


#
# a = 3
# b = 0
#
# try:
#     c = a / b
#     print(c)
# except ZeroDivisionError:
#     print("0 саны болунбойт")

#


#
# try:
#     a = int(input("a:"))
#     b = int(input("b:"))
#     while a <= b:
#         print(a)
#         a = a + 1
# except :
#     print("тамганы колдонго болбойт")
#     print("тамганы колдонго болбойт")
# b = int(input("b:"))
# while a <= b:
#     print(a)
#     a = a + 1

#
#
#
#
# a = int(input("a:"))
# b = int(input("b:"))
#
# for i in range(a, b):
#     print(i)
#





#
#
# def san(a, b):
#     if a < b:
#         print("a  саны b-санынан кичине")
#
#
#
#     else:
#         print("a  саны b-санынан кичине болуш керек")
#
# a = int(input("a:"))
# b = int(input("b:"))
# san(a, b)
#
#
# #



















#
#
#
# def f (n):
#     print(n)
#     try:
#         if n == 1:
#             print(1)
#     except RecursionError:
#         print("Рекурсияда ката")
#     return f(n-1)
#
# print(f(100))
#
#






#
# try:
#     a = int(input("a:"))
# except ValueError:
#     print("тамганы колдонго болбойт")
# try:
#     b = int(input("b:"))
# except ValueError:
#     print("тамга бербе")
# try:
#     while a <= b:
#         print(a)
#         a = a + 1
# except NameError:
#     print("берилиш туура эмес берилди")

#
# try:
#     a = int(input("a:"))
#     b = int(input("b:"))
#     while a <= b:
#         print(a)
#         a = a + 1
# except:
#     print("берилиш туура эмес берилди")
#
#
#


#
# try:
#
#     a = int(input("a:"))
#     b = int(input("b:"))()
#
#     for i in range(a, b+1):
#         print(i)
# except ValueError:
#     print("din")
# except TypeError:
#     print("der")
#


#
#
#
#
# def bsort(arr):
#     leng = len(arr)
#     for i in range(leng):
#         for j in range (0, leng-i-1):
#             if arr[j] > arr[j+1]:
#                 temp = arr[j]
#                 arr[j]  = arr[j + 1]
#                 arr[j + 1] = temp
#
#
# arr = [8, 9,  6, 7, 10, 3,  1, 2,  4, 5]
# bsort(arr)
# print(arr)
#
#
#
#

#
# def aek(row):
#     n = len(row)
#     for i in range(n-1):
#         m = i
#         for j in range(i +1, n):
#             if row[j] < row[m]:
#                 m = j
#         temp = row[i]
#         row[i] = row[m]
#         row[m] = temp
#
# a = [6, 7, 4, 3, 1, 9, 5, 2, 8]
# aek(a)
# print(a)




#
# def b(a):
#     ab = len(a)
#     if c == 2:
#         for j in range(1, ab, 3 ):
#             print(a[j])
#     elif c == 2:
#         for j in range(1, ab, 3):
#             print(a[j])
#     elif c == 11:
#
#
#
#
#
# a = [3,2,8,1,2,5,4,2,9,10,2,6]
# c = int(input("::"))
# b(a)
#
#
# def b(a):
#     for i in range(len(a)):
#         if a[i] == a[c]:
#             print(i)
#         else:
#             print(f"{c} сен сураган сан жок")
#
#
#
#
#
# a = [3, 2, 8, 1, 2, 5, 4, 2, 9, 10, 2, 6]
# c = int(input("::"))
# b(a)



#
#
# def b(a):
#     t = 0
#     for i in range(len(a)):
#         if a[i] == c:
#             print(f"сиз сураган {c} ал {i}-чу индексте")
#             t = 1
#     if t == 0:
#         print(f"сен сураган {c} жок")
#
# a = [3, 2, 8, 1, 2, 5, 4, 2, 9, 10, 2, 6]
# c = int(input("::"))
# b(a)





#
#
# a = [-3, 5, 0,-8, 1, 10]
# n = len(a)
#
#
# for i in range(1, n):
#     for j in range(i, 0, -1):
#         if a[j] < a[j-1]:
#             a[j], a[j-1] = a[j-1], a[j]
#         else:
#             break
#     print(a)
#








































































