# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class Triangle:
    def __init__(self, ax, ay, bx, by, cx, cy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        self.ab = math.sqrt((bx - ax)**2 + (by - ay)**2)
        self.ac = math.sqrt((cx - ax)**2 + (cy - ay)**2)
        self.bc = math.sqrt((cx - bx)**2 + (cy - by)**2)

    def perimetr(self):
        return self.ab + self.ac + self.bc

    def square(self):
        self.square = abs((self.bx - self.ax) * (self.cy - self.ay) - (self.cx - self.ax) * (self.by - self.ay)) / 2
        return self.square

    #Высота из точки A к стороне bc
    def height_a(self):
        self.height_a = self.square * 2 / self.bc
        return self.height_a

    #Высота из точки B к стороне ac
    def height_b(self):
        self.height_b = self.square * 2 / self.ac
        return self.height_b

    #Высота из точки C к стороне ab
    def height_c(self):
        self.height_c = self.square * 2 / self.ab
        return self.height_c

my_triangle = Triangle(0, 0, 3, 0, 0, 4)

print('Периметр треугольника равен ', my_triangle.perimetr())
print('Площадь треугольника равна ', my_triangle.square())
print('Высота из точки A к стороне bc равна ', my_triangle.height_a(), '\n'
      'Высота из точки B к стороне ac равна ', my_triangle.height_b(), '\n'
      'Высота из точки C к стороне ab равна ', my_triangle.height_c(), '\n')


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezoid:
    def __init__(self, ax, ay, bx, by, cx, cy, dx, dy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        self.dx = dx
        self.dy = dy
        self.ab = float(math.sqrt((bx - ax)**2 + (by - ay)**2))
        self.ad = float(math.sqrt((dx - ax)**2 + (dy - ay)**2))
        self.bc = float(math.sqrt((cx - bx)**2 + (cy - by)**2))
        self.cd = float(math.sqrt((dx - cx) ** 2 + (dy - cy) ** 2))

    def check(self):
        if self.ab == self.cd:
            return 'Трапеция равнобедренная'
        else:
            return 'Трапеция не является равнобедренной'

    def perimetr(self):
        return self.ab + self.bc + self.cd + self.ad

    def square(self):
        return ((self.ad + self.bc) / 2) * math.sqrt(self.ab ** 2 - (self.ad - self.bc) ** 2)

my_trapezoid = Trapezoid(1, 1, 2, 4, 6, 4, 7, 1)

print('Сторона AB равна ', my_trapezoid.ab, '\n'
      'Сторона BC равна ', my_trapezoid.bc, '\n'
      'Сторона CD равна ', my_trapezoid.cd, '\n'
      'Сторона AD равна ', my_trapezoid.ad)
print(my_trapezoid.check())
print('Периметр трапеции равен ', my_trapezoid.perimetr())
print('Площадь трапеции равна ', my_trapezoid.square())
