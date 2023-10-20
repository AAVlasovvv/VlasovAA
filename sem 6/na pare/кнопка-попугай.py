from tkinter import *
root = Tk()
root.geometry("500x250")

# функция нажатия на кнопку создает новый
def callback():
   Label(root, text="Hello World!", font=('Montserrat 20 bold')).pack(pady=4) #обратите внимание, что обращаемся к root как к глобальной переменной
'''
ВАЖНО!
Вы передаете функцию в виджет как объект -- поэтому она пишется здесь без скобок.
Если напишете со скобками, то она вызовется один раз и передаст как команду результат вызова (в нашем случае -- ничего).
Протестируйте это.
'''
btn = Button(root, text="Press Enter", command = callback)
btn.pack(ipadx=50) #ipadx задает размер кнопки по x
# делает так, чтобы при нажатии на Enter (эквивалент команды Return) тоже выполнялось callback
root.bind('<Return>', callback)
root.mainloop()