import sys
from fractions import Fraction

def read_circle_file(file_path):
    with open(file_path, 'r') as file:
        x, y = map(Fraction, file.readline().split())
        R = Fraction(file.readline().strip())
    
    return x, y, R

def read_points_file(file_path):
    with open(file_path, 'r') as file:
        points = [tuple(map(Fraction, line.split())) for line in file]
    
    if not (1 <= len(points) <= 100):
        raise ValueError("Количество точек должно быть от 1 до 100.")
    
    for point in points:
        for coord in point:
            if not (-1e38 <= coord.numerator / coord.denominator <= 1e38):
                raise ValueError("Координаты точек должны быть в диапазоне от -10^38 до 10^38.")
    
    return points

def point_position(circle_x, circle_y, R, point_x, point_y):
    hypotenuse = (point_x - circle_x) ** 2 + (point_y - circle_y) ** 2
    
    if hypotenuse == R ** 2:
        return 0
    elif hypotenuse < R ** 2:
        return 1
    else:
        return 2

def main():
    if len(sys.argv) != 3:
        print("Пример использования: python script.py <circle_file> <points_file>")
        return

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    circle_x, circle_y, R = read_circle_file(circle_file)
    points = read_points_file(points_file)

    for point_x, point_y in points:
        result = point_position(circle_x, circle_y, R, point_x, point_y)
        print(result)

if __name__ == "__main__":
    main()
