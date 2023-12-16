import math

def plant_trees_on_road(K, T, road_points):
    trees = []

    total_distance = 0
    for i in range(K - 1):
        x1, y1 = road_points[i]
        x2, y2 = road_points[i + 1]
        segment_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        total_distance += segment_distance
        
    # print(total_distance)

    step = total_distance / (T-1)
    # print(step)

    cumulative_distance = 0
    current_point = road_points[0]
    trees.append(road_points[0])
    for i in range(K - 1):
        x1, y1 = current_point
        x2, y2 = road_points[i + 1]
        segment_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        # print(segment_distance)

        while cumulative_distance + segment_distance >= step:
            ratio = (step - cumulative_distance) / segment_distance
            tx = x1 + (x2 - x1) * ratio
            ty = y1 + (y2 - y1) * ratio
            trees.append((tx, ty))
            remaining_distance = segment_distance - (step - cumulative_distance)
            x1, y1 = tx, ty
            cumulative_distance = 0
            segment_distance = remaining_distance

        cumulative_distance += segment_distance
        current_point = (x2, y2)

    # trees.append(road_points[-1])

    return trees  # Используем обратный порядок вывода

# Входные данные
K = 5  # Количество точек на дороге
T = 6  # Количество деревьев
road_points = [(10.00, 10.00), (20.00, 20.00), (30.00, 10.00), (10.00, 0.00), (9.00, 9.00)]

# Обработка данных и вывод результатов
trees = plant_trees_on_road(K, T, road_points)
print("Road #1:")
for tree in trees:
    print(f"{tree[0]:.2f} {tree[1]:.2f}")
