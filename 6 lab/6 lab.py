import math
class Complex():
    def __init__(self, a = 0, b = 0):
        try:
            self.a = a
            self.b = b
        except Exception:
            print('\n', 'ФУНКЦИЯ __init__ ИСПОЛЬЗУЕТСЯ НЕПРАВЛИЛЬНО! ПЕРЕОПРЕДЕЛИТЕ ЕЁ ИЛИ ИСПРАВЬТЕ ОШИБКУ!', '\n')
    def __add__(self, other):
        try:
            return Complex(self.a + other.a, self.b + other.b)
        except Exception:
            print('\n', 'ФУНКЦИЯ __add__ ИСПОЛЬЗУЕТСЯ НЕПРАВЛИЛЬНО! ПЕРЕОПРЕДЕЛИТЕ ЕЁ ИЛИ ИСПРАВЬТЕ ОШИБКУ!', '\n')
    def __sub__(self, other):
        try:
            return Complex(self.a - other.a, self.b - other.b)
        except Exception:
            print('\n', 'ФУНКЦИЯ __sub__ ИСПОЛЬЗУЕТСЯ НЕПРАВЛИЛЬНО! ПЕРЕОПРЕДЕЛИТЕ ЕЁ ИЛИ ИСПРАВЬТЕ ОШИБКУ!', '\n')
    def __mul__(self, other):
        try:
            return Complex(self.a * other.a - other.b * self.b, self.a * other.b + other.a * self.b)
        except Exception:
            print('\n', 'ФУНКЦИЯ __mul__ ИСПОЛЬЗУЕТСЯ НЕПРАВЛИЛЬНО! ПЕРЕОПРЕДЕЛИТЕ ЕЁ ИЛИ ИСПРАВЬТЕ ОШИБКУ!', '\n')
    def __truediv__(self, other):
        try:
            return Complex((self.a * other.a - other.b * self.b)/(other.a * other.a + other.b * other.b), (other.a * self.b - self.a * other.b)/(other.a * other.a + other.b * other.b))
        except Exception:
            print('\n', 'ФУНКЦИЯ __truediv__ ИСПОЛЬЗУЕТСЯ НЕПРАВЛИЛЬНО! ПЕРЕОПРЕДЕЛИТЕ ЕЁ ИЛИ ИСПРАВЬТЕ ОШИБКУ!', '\n')
    def __abs__(self):
        try:
            return math.sqrt(self.a * self.a + self.b * self.b)
        except Exception:
            print('\n', 'ФУНКЦИЯ __abs__ ИСПОЛЬЗУЕТСЯ НЕПРАВЛИЛЬНО! ПЕРЕОПРЕДЕЛИТЕ ЕЁ ИЛИ ИСПРАВЬТЕ ОШИБКУ!', '\n')
    def __str__(self):
        try:
            out = ''
            if self.a != 0:
                out += str(self.a)
            if self.b > 0:
                if out == '':
                    out += '{}i'.format(self.b)
                else:
                    out += ' + {}i'.format(self.b)
            elif self.b < 0:
                if out == '':
                    out += '{}i'.format(self.b)
                else:
                    out += ' - {}i'.format(-self.b)
            else:
                pass
            return out
        except Exception:
            print('\n', 'ФУНКЦИЯ __str__ ИСПОЛЬЗУЕТСЯ НЕПРАВЛИЛЬНО! ПЕРЕОПРЕДЕЛИТЕ ЕЁ ИЛИ ИСПРАВЬТЕ ОШИБКУ!', '\n')

class Vector():
    def __init__(self, x = 0, y = 0, z = 0):
        try:
            self.x = x
            self.y = y
            self.z = z
        except Exception:
            print('\n', 'ФУНКЦИЯ __init__ ИСПОЛЬЗУЕТСЯ НЕПРАВЛИЛЬНО! ПЕРЕОПРЕДЕЛИТЕ ЕЁ ИЛИ ИСПРАВЬТЕ ОШИБКУ!', '\n')

    @classmethod
    def strok(cls, input = '0,0,0'):
        try:
            return cls(int(input[0]), int(input[2]), int(input[4]))
        except Exception:
            print('\n', 'ФУНКЦИЯ __init__.strok ИСПОЛЬЗУЕТСЯ НЕПРАВЛИЛЬНО! ПЕРЕОПРЕДЕЛИТЕ ЕЁ ИЛИ ИСПРАВЬТЕ ОШИБКУ!', '\n')

    def __str__(self):
        try:
            return ('(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ')')
        except Exception:
            print('\n', 'ФУНКЦИЯ __str__ ИСПОЛЬЗУЕТСЯ НЕПРАВЛИЛЬНО! ПЕРЕОПРЕДЕЛИТЕ ЕЁ ИЛИ ИСПРАВЬТЕ ОШИБКУ!', '\n')

    def __add__(self, other):
        try:
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        except Exception:
            print('\n', 'ФУНКЦИЯ __add__ ИСПОЛЬЗУЕТСЯ НЕПРАВЛИЛЬНО! ПЕРЕОПРЕДЕЛИТЕ ЕЁ ИЛИ ИСПРАВЬТЕ ОШИБКУ!', '\n')

    def __mul__(self, other):
        try:
            return (self.x * other.x + self.y * other.y + self.z * other.z)
        except Exception:
            print('\n', 'ФУНКЦИЯ __mul__ ИСПОЛЬЗУЕТСЯ НЕПРАВЛИЛЬНО! ПЕРЕОПРЕДЕЛИТЕ ЕЁ ИЛИ ИСПРАВЬТЕ ОШИБКУ!', '\n')

    def __truediv__(self, other):
        try:
            return Vector(self.x / other, self.y / other, self.z / other)
        except Exception:
            print('\n', 'ФУНКЦИЯ __truediv__ ИСПОЛЬЗУЕТСЯ НЕПРАВЛИЛЬНО! ПЕРЕОПРЕДЕЛИТЕ ЕЁ ИЛИ ИСПРАВЬТЕ ОШИБКУ!', '\n')

    def __sub__(self, other):
        try:
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        except Exception:
            print('\n', 'ФУНКЦИЯ __sub__ ИСПОЛЬЗУЕТСЯ НЕПРАВЛИЛЬНО! ПЕРЕОПРЕДЕЛИТЕ ЕЁ ИЛИ ИСПРАВЬТЕ ОШИБКУ!', '\n')

    def __abs__(self):
        try:
            return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        except Exception:
            print('\n', 'ФУНКЦИЯ __abs__ ИСПОЛЬЗУЕТСЯ НЕПРАВЛИЛЬНО! ПЕРЕОПРЕДЕЛИТЕ ЕЁ ИЛИ ИСПРАВЬТЕ ОШИБКУ!', '\n')

    @staticmethod
    def most_distant(*args):
        try:
            answer = Vector()
            mx = float('-inf')
            for el in args:
                if abs(el) > mx:
                    mx = abs(el)
                    answer = el
            return (answer)
        except Exception:
            print('\n', 'ФУНКЦИЯ most_distant ИСПОЛЬЗУЕТСЯ НЕПРАВЛИЛЬНО! ПЕРЕОПРЕДЕЛИТЕ ЕЁ ИЛИ ИСПРАВЬТЕ ОШИБКУ!', '\n')

    @staticmethod
    def mass_centre(*args):
        try:
            return (sum(*args) / len(args))
        except Exception:
            print('\n', 'ФУНКЦИЯ mass_centre ИСПОЛЬЗУЕТСЯ НЕПРАВЛИЛЬНО! ПЕРЕОПРЕДЕЛИТЕ ЕЁ ИЛИ ИСПРАВЬТЕ ОШИБКУ!', '\n')

    @staticmethod
    def square_par(a, b):
        try:
            return (0.5 * (a * b))
        except Exception:
            print('\n', 'ФУНКЦИЯ square_par ИСПОЛЬЗУЕТСЯ НЕПРАВЛИЛЬНО! ПЕРЕОПРЕДЕЛИТЕ ЕЁ ИЛИ ИСПРАВЬТЕ ОШИБКУ!', '\n')

    @staticmethod
    def max_square(*args):
        try:
            answer = [Vector(0,0,0), Vector(0,0,0), Vector(0,0,0)]
            mx = float('-inf')
            for i in range(len(args)):
                for j in range(1, len(args)):
                    for el in args[j::]:
                        a = abs((el - args[i]) * (el - args[j]))
                        if a > mx:
                            mx = a
                            answer = [el, args[i], args[j]]
            return answer
        except Exception:
            print('\n', 'ФУНКЦИЯ max_square ИСПОЛЬЗУЕТСЯ НЕПРАВЛИЛЬНО! ПЕРЕОПРЕДЕЛИТЕ ЕЁ ИЛИ ИСПРАВЬТЕ ОШИБКУ!', '\n')

    @staticmethod
    def max_perimetr(*args):
        try:
            answer = [Vector(0,0,0), Vector(0,0,0), Vector(0,0,0)]
            mx = float('-inf')
            for i in range(len(args)):
                for j in range(len(args[i::])):
                    for el in args[j::]:
                        a = abs((el - args[i])) + abs((el - args[j])) + abs((args[i] - args[j]))
                        if a > mx:
                            mx = a
                            answer = [el, args[i], args[j]]
            return answer
        except Exception:
            print('\n', 'ФУНКЦИЯ max_perimetr ИСПОЛЬЗУЕТСЯ НЕПРАВЛИЛЬНО! ПЕРЕОПРЕДЕЛИТЕ ЕЁ ИЛИ ИСПРАВЬТЕ ОШИБКУ!', '\n')

if __name__ == '__main__':
    b = Vector.strok('4,5,6')
    print(b)
    a = Vector(1, 2, 3)
    print(a)
    c = Vector(1, 5, 3)
    d = Vector.strok('9,9,9')
    f = 4
    print(a + f)
    print("Максимальную площадь образуют:")
    for el in Vector.max_square(a, b, c, d):
        print(el)
    print("Максимальный периметр образуют:")
    for el in Vector.max_perimetr(a, b, c, d):
        print(el)
