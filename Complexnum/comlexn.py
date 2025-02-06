import math
from rational import Rational

class ComplexNumber:
    """
    Класс для представления комплексных чисел в виде real + imag*i.

    """
    def __init__(self, real: int | Rational | float, imag: int | Rational | float=0):
        """
        Инициализация комплексного числа.
        real: Действительная часть комплексного числа.
        imag: Мнимая часть комплексного числа.
        """
        self.__real = real
        self.__imag = imag

    @property
    def real(self) -> Rational:
        return self.__real

    @real.setter
    def real(self, value: Rational):
        if not isinstance(value, Rational):
            raise ValueError("Real part must be a rational number.")
        self.__real = value

    @property
    def imag(self) -> Rational:
        return self.__imag

    @imag.setter
    def imag(self, value: Rational):
        if not isinstance(value, Rational):
            raise ValueError("Imaginary part must be a rational number.")
        self.__imag = value

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        if isinstance(other, Rational | int | float):
            return Complex(self.real + Rational(other), self.imag)
        else:
            raise TypeError("operand must be a rational or a number.")

    def __iadd__(self, other):
        if isinstance(other, ComplexNumber):
            self.real += other.real
            self.imag += other.imag
        elif isinstance(other, (Rational, int, float)):
            self.real += Rational(other)
            self.imag += Rational(other)
        else:
            raise TypeError("operand must be a rational or a number.")
        return self

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imag - other.imag)
        elif isinstance(other, (Rational, int, float)):
            return ComplexNumber(self.real - Rational(other), self.imag)
        else:
            raise TypeError("operand must be a rational or a number.")
    
    def __isub__(self, other):
        if isinstance(other, ComplexNumber):
            self.real -= other.real
            self.imag -= other.imag
        elif isinstance(other, (Rational, int, float)):
            self.real -= Rational(other)  # Преобразуем в Rational
        else:
            raise TypeError("operand must be a rational or a number.")
        return self

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            return ComplexNumber(real_part, imag_part)
        elif isinstance(other, (Rational, int, float)):
            return ComplexNumber(self.real * Rational(other), self.imag * Rational(other))
        else:
            raise TypeError("operand must be a rational or a number.")

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            if other.real == 0 and other.imag == 0:
                raise ZeroDivisionError("cannot divide by zero.")
            denominator = other.real ** 2 + other.imag ** 2
            real_part = (self.real * other.real + self.imag * other.imag) / denominator
            imag_part = (self.imag * other.real - self.real * other.imag) / denominator
            return ComplexNumber(real_part, imag_part)
        elif isinstance(other, (Rational, int, float)):
            if other == 0:
                raise ZeroDivisionError("cannot divide by zero.")
            return ComplexNumber(self.real / Rational(other), self.imag / Rational(other))
        else:
            raise TypeError("operand must be a rational or a number.")
        
    def __itruediv__(self, other):
        if isinstance(other, ComplexNumber):
            if other.real == 0 and other.imag == 0:
                raise ZeroDivisionError("cannot divide by zero.")
            denominator = other.real ** 2 + other.imag ** 2
            self.real = (self.real * other.real + self.imag * other.imag) / denominator
            self.imag = (self.imag * other.real - self.real * other.imag) / denominator
        elif isinstance(other, (Rational, int, float)):
            if other == 0:
                raise ZeroDivisionError("cannot divide by zero.")
            self.real /= Rational(other)
            self.imag /= Rational(other)
        else:
            raise TypeError("operand must be a rational or a number.")
        return self
        
    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            return self.real == other.real and self.imag == other.imag
        if isinstance(other, Rational | int | float):
            return self.real == other and self.imag == 0
        else:
            raise TypeError("operand must be a rational or a number.")

    def __ne__(self, other):
        return not self == other

    def __min__(self):
        return ComplexNumber(-self.real, -self.imag)

    def pow(self, n: int):
        if n < 0:
            raise ValueError("exponent must be a non-negative integer.")
        result = ComplexNumber(Rational(1, 1), Rational(0, 1)) 
        for _ in range(n):
            result *= self
        return result

    def arg(self):
        return math.atan2(self.imag.__float(), self.real.__float())

    def abs(self):
        return math.sqrt(self.real.__float() ** 2 + self.imag.__float() ** 2)

    def __str__(self):
        sign = '+' if self.imag.numerator >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imag)}i"

    def __repr__(self):
        return f"ComplexNumber(real={self.real}, imag={self.imag})"
