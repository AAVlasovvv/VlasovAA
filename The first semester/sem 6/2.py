from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        weight = float(weight_.get())
        height = float(height_.get())
        BMI.set('{0:.3f}'.format(float(weight/(height**2/10000))))
        if float(BMI.get()) < 16:
            BMIresult.set(Pronounced_body_weight_deficiency)
        elif 16 <= float(BMI.get()) < 18.5:
            BMIresult.set(Insufficient_deficiency_body_weight)
        elif 18.5 <= float(BMI.get()) < 25:
            BMIresult.set(Standard)
        elif 25 <= float(BMI.get()) < 30:
            BMIresult.set(Overweight_pre_obesity)
        elif 30 <= float(BMI.get()) < 35:
            BMIresult.set(Obesity1)
        elif 35 <= float(BMI.get()) < 40:
            BMIresult.set(Obesity2)
        else:
            BMIresult.set(Obesity3)
            
    except ValueError:
        print(1)
        pass


Pronounced_body_weight_deficiency = 'Pronounced body weight deficiency'
Insufficient_deficiency_body_weight = 'Insufficient (deficiency) body weight'
Standard = 'Standard'
Overweight_pre_obesity = 'Overweight (pre-obesity)'
Obesity1 = 'Obesity of the 1st degree'
Obesity2 = 'Obesity of the 2nd degree'
Obesity3 = 'Obesity of the 3rd degree'





# Создадим основное окно приложенияweight
root = Tk()
root.title("BMI")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


weight_ = StringVar()
weight__entry = ttk.Entry(mainframe, width=7, textvariable=weight_)
weight__entry.grid(column=1, row=2, sticky=(W, E))

height_ = StringVar()
height__entry = ttk.Entry(mainframe, width=7, textvariable=height_)
height__entry.grid(column=2, row=2, sticky=(W, E))

BMI = StringVar()
ttk.Label(mainframe, textvariable=BMI).grid(column=3, row=2, sticky=(W, E))

BMIresult = StringVar()
ttk.Label(mainframe, textvariable=BMIresult).grid(column=3, row=3, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=1, row=3, sticky=W)

# косметические подписи, обратите внимание на расположение
ttk.Label(mainframe, text="Your weight (kg):").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Your height (cm)").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, text="BMI").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Interpretation of BMI indicators:").grid(column=2, row=3, sticky=W)
# этот цикл позволяет "разбросать" элементы подальше друг от друга
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# сразу помещает курсор ввода в поле feet_entry
# feet_entry.focus()
# делает так, чтобы при нажатии на Enter (эквивалент команды Return) тоже выполнялось calculate
root.bind("<Return>", calculate)

# циклим наше окно
root.mainloop()