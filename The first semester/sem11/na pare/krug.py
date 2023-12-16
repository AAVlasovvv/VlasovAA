from math import pi

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("positive radius expected")
        self.radius = radius

    def area(self):
        assert self.radius >= 0, "positive radius expected"
        return pi * self.radius ** 2
    
    def correct_radius(self, correction_coefficient):
        self.radius *= correction_coefficient
        
tire = Circle(42)
tire.area()
tire.correct_radius(-1.02)
tire.area()