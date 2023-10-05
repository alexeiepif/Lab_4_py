def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    b = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
    c = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
    s = 0.5 * (a + b + c)
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


x1, y1 = 1, 2
x2, y2 = 3, 7
x3, y3 = 5, 3
x4, y4 = 3, 0

abc_area = calculate_triangle_area(x1, y1, x2, y2, x3, y3)
acd_area = calculate_triangle_area(x1, y1, x3, y3, x4, y4)

# вычисление суммарной площади двух треугольников
total_area = abc_area + acd_area

# вывод результата
print("Площадь четырехугольника: ", round(total_area, 10))
