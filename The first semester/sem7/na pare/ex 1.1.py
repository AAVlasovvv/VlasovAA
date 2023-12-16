class Vector():
    def __init__(self, x, y ,z):
        self.x = x
        self.y = y
        self.z = z
    
    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x+other.x, self.y+other.y, self.z+other.z )
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x + other, self.y + other, self.z + other)
        
    def __radd__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self + other
    
    def __repr__(self):
        return f'x={self.x} y={self.y} x={self.z}'
    
    def __str
    

v1 = Vector(1,2,3)
print(isinstance(v1, Vector))
print(v1.x - v1.y)
v2 = Vector(2,3,4)
print(v1.x*v2.x)
print(abs(v2))

v3 = v1 + 1 + v2
print(v3.x, v3.y, v3.z)

sv = str(v3)

print(sv)