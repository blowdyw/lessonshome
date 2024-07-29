
import  tkinter as tk

oper = " "

def bara():
    global oper
    result = str(eval(oper))
    enter_d.set(result)


def click_btn(number):
    global oper
    oper = oper + str(number)
    enter_d.set(oper)

def clear_btn():
    global oper
    enter_d.set("")
    oper = ""



root = tk.Tk()


root.geometry("300x300")
root.title("calculator")
btn1 = tk.Button(root, width=5, height=2, text="1" ,command=lambda :click_btn(1))
btn2 = tk.Button(root, width=5, height=2, text="2", command=lambda :click_btn(2))
btn3 = tk.Button(root, width=5, height=2, text="3" ,command=lambda :click_btn(3))
btn4 = tk.Button(root, width=5, height=2, text="4" ,command=lambda :click_btn(4))
btn5 = tk.Button(root, width=5, height=2, text="5" ,command=lambda :click_btn(5))
btn6 = tk.Button(root, width=5, height=2, text="6" ,command=lambda :click_btn(6))

btn7 = tk.Button(root, width=5, height=2, text="7" ,command=lambda :click_btn(7))
btn8 = tk.Button(root, width=5, height=2, text="8" ,command=lambda :click_btn(8))
btn9 = tk.Button(root, width=5, height=2, text="9" ,command=lambda :click_btn(9))
btn0 = tk.Button(root, width=5, height=2, text="0" ,command=lambda :click_btn(0))
btnc = tk.Button(root, width=5, height=2, text="c",command=clear_btn)
btntochka = tk.Button(root, width=5, height=2, text="." ,command=lambda :click_btn("."))
btnbara = tk.Button(root, width=5, height=2, text="=", command=bara)
btnkoshuu = tk.Button(root, width=5, height=2, text="+",command=lambda :click_btn("+"))
btnkemityy = tk.Button(root, width=5, height=2, text="-",command=lambda :click_btn("-"))
btnkoboityy = tk.Button(root, width=5, height=2, text="*",command=lambda :click_btn("*"))
btnbolyy = tk.Button(root, width=5, height=2, text="/", command=lambda:click_btn("/"))
btnpro = tk.Button(root, width=5, height=2, text="%", command=lambda:click_btn("%"))
btnx = tk.Button(root, width=5, height=2, text="x²",command=lambda:click_btn("²"))
btnx1 = tk.Button(root, width=5, height=2, text="x³" ,command=lambda:click_btn("³"))
enter_d = tk.DoubleVar()
enter = tk.Entry(root, width=20, font=40, textvariable=enter_d)




btn1.place(x=15, y = 50)
btn2.place(x=65, y = 50)
btn3.place(x=115, y = 50)
btn4.place(x=15, y = 100)
btn5.place(x=65, y = 100)
btn6.place(x=115, y = 100)
btn7.place(x=15, y = 150)
btn8.place(x=65, y = 150)
btn9.place(x=115, y = 150)
btn0.place(x=65, y = 200)
btnc.place(x=15, y = 200)
btntochka.place(x=115, y = 200)
btnbara.place(x=230, y = 200)
btnkoshuu.place(x=180, y = 150)
btnkemityy.place(x=180, y = 100)
btnkoboityy.place(x=180, y = 50)
btnbolyy.place(x=230, y = 50)
btnpro.place(x=180, y = 200)
btnx.place(x=230, y = 100)
btnx1.place(x=230, y = 150)



enter.place(x=15, y= 11)

root.mainloop()







































































































