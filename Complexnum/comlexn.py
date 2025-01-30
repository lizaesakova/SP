import math
from rational import Rational

class ComplexNumber:


    def __init__(self, real: Rational | None, imag: Rational | None):
        if not isinstance(real, Rational):
            raise ValueError("real part must be a rational number.")
        if not isinstance(imag, Rational):
            raise ValueError("imaginary part must be a rational number.")
        self.__real = real
        self.__imag = imag

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value: Rational | None):
        if not isinstance(value, Rational):
            raise ValueError("real part must be a rational number.")
        self.__real = value

    @property
    def imag(self):
        return self.__imag

    @imag.setter
    def imag(self, value: Rational | None):
        if not isinstance(value, Rational):
            raise ValueError("imaginary part must be a rational number.")
        self.__imag = value

    def __add__(self, other):
        if not isinstance(other, ComplexNumber):
            raise TypeError("operand must be a complexnumber.")
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __iadd__(self, other):
        if not isinstance(other, ComplexNumber):
            raise TypeError("operand must be a complexnumber.")
        self.real += other.real
        self.imag += other.imag
        return self

    def __sub__(self, other):
        if not isinstance(other, ComplexNumber):
            raise TypeError("operand must be a complexnumber.")
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __isub__(self, other):
        if not isinstance(other, ComplexNumber):
            raise TypeError("operand must be a complexnumber.")
        self.real -= other.real
        self.imag -= other.imag
        return self

    def __mul__(self, other):
        if not isinstance(other, ComplexNumber):
            raise TypeError("operand must be a complexnumber.")
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __truediv__(self, other):
        if not isinstance(other, ComplexNumber):
            raise TypeError("operand must be a complexnumber.")
        if other.real == 0 and other.imag == 0:
            raise ZeroDivisionError("cannot divide by zero.")

        denominator = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real_part, imag_part)

    def __itruediv__(self, other):
       if not isinstance(other, ComplexNumber):
            raise TypeError("operand must be a complexnumber.")
       if other.real == 0 and other.imag == 0:
            raise ZeroDivisionError("cannot divide by zero.")


       self.real = (self.real * other.real + self.imag * other.imag) / (other.real ** 2 + other.imag ** 2)
       self.imag = (self.imag * other.real - self.real * other.imag) / (other.real ** 2 + other.imag ** 2)

       return self

    def __eq__(self, other):
        if not isinstance(other, ComplexNumber):
            raise TypeError("operand must be a complexnumber")
        return self.real == other.real and self.imag == other.imag

    def __ne__(self, other):
        return not self == other

    def __neg__(self):
        return ComplexNumber(-self.real, -self.imag)

    def pow(self, n: int):
        if n < 0:
            raise ValueError("exponent must be a non-negative integer.")
        result = ComplexNumber(Rational(1, 1), Rational(0, 1))  # 1 + 0i
        for _ in range(n):
            result *= self
        return result

    def arg(self):
        return math.atan2(self.imag.to_float(), self.real.to_float())

    def abs(self):
        return math.sqrt(self.real.to_float() ** 2 + self.imag.to_float() ** 2)

    def __str__(self):
        sign = '+' if self.imag.numerator >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imag)}i"

    def __repr__(self):
        return f"ComplexNumber(real={self.real}, imag={self.imag})"

