import itertools
import numpy as np

def calculate_triangle_area(a, b, c):
    """
    Функция для вычисления площади треугольника по координатам вершин.
    Использует формулу Герона.
    """
    ab = np.linalg.norm(np.subtract(a, b))
    bc = np.linalg.norm(np.subtract(b, c))
    ac = np.linalg.norm(np.subtract(a, c))

    semiperimeter = (ab + bc + ac) / 2
    area = np.sqrt(semiperimeter * (semiperimeter - ab) * (semiperimeter - bc) * (semiperimeter - ac))
    return area

def max_triangle_area(points):
    """
    Функция для вычисления максимальной площади треугольника, которую можно получить
    из комбинаций троек заданных точек.
    """
    max_area = 0
    max_triangle = None
    for combination in itertools.combinations(points, 3):
        triangle = list(combination)
        area = calculate_triangle_area(triangle[0], triangle[1], triangle[2])
        if area > max_area:
            max_area = area
            max_triangle = triangle
    return max_area, max_triangle

points = [np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1]), np.array([1, 1, 1])]
print(max_triangle_area(points))
