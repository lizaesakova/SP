import math

class Rational:
  """принимаем два необязательных аргумента (n)числитель и (m)знаментель
  используем аннотацию типов, указываем, что оба числа могут быть целыми
  или None
  проверяем на целочисленность, а после устанавливаем значения
  """

  def __init__(self, n: int | None, m: int | None):
    if not isinstance(n, int):
      raise ValueError("numerator must be an int")
    if not isinstance(m, int):
      raise ValueError("denomitor must be an int")

    self.__numerator = n

    if m==0:
      raise ValueError("You can't divide by zero.")

    self.__denominator = m

  """получаем значение числителя через свойство numerator"""
  #геттер для числителя
  @property
  def numerator(self):
    return self.__numerator

  """принимаем значение и проверяем целое оно или нет"""
  #Сеттер для числителя
  @numerator.setter
  def numerator(self, value: int | None):
    if not isinstance(value, int):
      raise ValueError("numerator must be an integer")
    self.__numerator = value

  #геттер для знаменателя
  @property
  def denominator(self):
    return self.__denominator

  #сеттер для знаменателя
  @denominator.setter
  def denominator(self, value: int | None):

    if not isinstance(value, int):
      raise ValueError("denominator must be an integer")

    if value != 0:
      self.__denominator = value

    else:
      raise ValueError("Division by zero")

  def simplify(self):
        from math import gcd
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

  """сложение"""

  def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(
                self.numerator * other.denominator + self.denominator * other.numerator,
                self.denominator * other.denominator)
        elif isinstance(other, int):
            return Rational(
                self.numerator + other * self.denominator,
                self.denominator)
        else:
            raise TypeError("other operand must be an integer or Rational")

  def __iadd__(self, other):
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator + self.denominator * other.numerator
            self.denominator = self.denominator * other.denominator
        elif isinstance(other, int):
            self.numerator += other * self.denominator
        else:
            raise TypeError("other operand must be an integer or Rational")
        self.simplify()
        return self

  """вычитание"""
  def __sub__(self, other):
        if isinstance(other, Rational):
            return Rational(
                self.numerator * other.denominator - self.denominator * other.numerator,
                self.denominator * other.denominator)
        elif isinstance(other, int):
            return Rational(
                self.numerator - other * self.denominator,
                self.denominator)
        else:
            raise TypeError("other operand must be an integer or Rational")

    def __isub__(self, other):
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator - self.denominator * other.numerator
            self.denominator = self.denominator * other.denominator
        elif isinstance(other, int):
            self.numerator -= other * self.denominator
        else:
            raise TypeError("other operand must be an integer or Rational")
        self.simplify()
        return self

  """Метод для умножения"""

  def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(
                self.numerator * other.numerator,
                self.denominator * other.denominator
            )
        elif isinstance(other, int):
            return Rational(
                self.numerator * other,
                self.denominator
            )
        else:
            raise TypeError("other operand must be an integer or Rational")

  def __imul__(self, other):
        if isinstance(other, Rational):
            self.numerator *= other.numerator
            self.denominator *= other.denominator
        elif isinstance(other, int):
            self.numerator *= other
        else:
            raise TypeError("other operand must be an integer or Rational")
        self.simplify()
        return self

  """Метод для деления"""
  def __div__(self, other):
    if isinstance(other, Rational):
      return Rational(self.numerator * other.denominator, self.denominator * other.numerator)
    elif isinstance(other, int):
      return Rational(self.numerator, self.denominator * other)
    else:
      raise TypeError("other operand must be an integer or Rational")

  def __idiv__(self, other):
    if isinstance(other, Rational):
      self.numerator = self.numerator * other.denominator
      self.denominator = self.denominator * other.numerator
    elif isinstance(other, int):
      self.denominator = self.denominator * other
    else:
      raise TypeError("other operand must be an integer or Rational")
    self.simplify()
    return self

  """метод определения равенства (==)"""
  def __eq__(self, value):
    if isinstance(other, Rational):
      return (self.numerator * other.denominator) == (self.denominator * other.numerator)
    elif isinstance(other, int):
      return self.numerator == (other * self.denominator)
    else:
      raise ValueError("other operand must be an int or Rational")

  """возведение в степень"""

  def __pow__(self, other: int | None):
        if not isinstance(other, int):
            raise TypeError("other operand must be an int")

        if other < 0:
            return Rational(self.denominator ** abs(other), self.numerator ** abs(other))
        elif other > 0:
            return Rational(self.numerator ** other, self.denominator ** other)
        else:
            return Rational(1, 1)

  def __abs__(self):
    return Rational(abs(self.numerator), abs(self. denominator))

  """метод определения неравенства (!=)"""
  def __ne__(self, value):
    return not self == other


  def __str__(self):
    return str(round(self.__numerator / self.__denominator, 10))

  def __repr__(self):
    return f"Rational({self.__numerator}, {self.__denominator})"

  def print_fraction(self):
    return f"Rational number: ({self.__numerator} / {self.__denominator})"
