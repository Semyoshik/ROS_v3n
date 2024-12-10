import random
import numpy as np

def generate_world(num_buildings=5, min_distance=1.0, x_range=(0, 9), y_range=(0, 9)):
    """Генерирует случайные расположения и цвета зданий."""

    buildings = []
    for i in range(num_buildings):
        while True:
            x = random.uniform(*x_range)
            y = random.uniform(*y_range)
            valid_location = True
            for b in buildings:
                distance = np.linalg.norm(np.array([x, y]) - np.array([b['x'], b['y']]))
                if distance < min_distance:
                    valid_location = False
                    break
            if valid_location:
                break

        color = random.choice(['красный', 'зеленый', 'желтый', 'синий'])
        buildings.append({'x': x, 'y': y, 'color': color})
    return buildings

# Пример использования:
buildings = generate_world()
print(buildings)
