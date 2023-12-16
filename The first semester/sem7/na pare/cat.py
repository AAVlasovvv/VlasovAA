class Cat():
  def __init__(self, breed, color, age):
     self.breed = breed
     self.color = color
     self.age = age

  def meow(self):
     print('Мяу!')
     
first_cat = Cat('Абиссинская', 'Рыжая', 4)

first_cat.meow()
a = first_cat.breed #без круглых скобок! это поле
print(a)