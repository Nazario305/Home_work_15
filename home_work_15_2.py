
import math
class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError('Знаменник не може дорівнювати нулю')
        self.a = a
        self.b = b
        self.original_a = a
        self.original_b = b
        self._reduce()

    def _reduce(self):
        gcd = math.gcd(self.a, self.b)
        self.a //= gcd
        self.b //= gcd


    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_a = self.original_a * other.original_a
            new_b = self.original_b * other.original_b
            return Fraction(new_a, new_b)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_a = self.original_a * other.original_b + other.original_a * self.original_b
            new_b = self.original_b * other.original_b
            return Fraction(new_a, new_b)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_a = self.original_a * other.original_b - other.original_a * self.original_b
            new_b = self.original_b * other.original_b
            return Fraction(new_a, new_b)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.a == other.a and self.b == other.b
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b > other.a * self.b
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b < other.a * self.b
        return NotImplemented

    def __str__(self):
        return f"Fraction: {self.original_a}, {self.original_b}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')



