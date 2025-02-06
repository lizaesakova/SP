import math
from math import gcd

class Rational:
    """
    Класс для представления рациональных чисел в виде дробей (числитель/знаменатель).
    """
  
  def __init__(self, n, m=1):
    """
    Инициализация рационального числа.

    n: Числитель или другое рациональное число.
    m: Знаменатель (не может быть равным нулю).
    """
    if m==0:
      raise ValueError("You can't divide by zero.")

    # Преобразуем float в Rational
    if isinstance(n, Rational) or isinstance(m, Rational):
        self._process_rational_input(n, m)
    else:
        self._process_float_input(n, m)
    self._simplify()


  def _process_rational_input(self, n, m):
    """
    если числитель или знаменатель уже является рациональным числом.

    n: Числитель или рациональное число.
    m: Знаменатель или рациональное число.
    """
    n_ration = isinstance(n, Rational)
    m_ration = isinstance(m, Rational)

    if n_ration and m_ration:
        self.numerator = n.numerator * m.denominator
        self.denominator = n.denominator * m.numerator
    elif n_ration:
        self.numerator = n.numerator
        self.denominator = n.denominator * m
    elif m_ration:
        self.numerator = n * m.denominator
        self.denominator = m.numerator
    
  def _process_float_input(self, n, m):
    """
    если числитель или знаменатель является числом с плавающей точкой.

    n: Числитель или число с плавающей точкой.
    m: Знаменатель или число с плавающей точкой.
    """
    n_numerator, n_denominator = None, None
    m_numerator, m_denominator = None, None

    if isinstance(n, float):
        n_numerator, n_denominator = self._float_to_rational(n)
    if isinstance(m, float):
        m_numerator, m_denominator = self._float_to_rational(m)

    if n_numerator is not None and m_numerator is not None:
        self.numerator = n_numerator * m_denominator
        self.denominator = m_numerator * n_denominator
    elif n_numerator is not None:
        self.numerator = n_numerator
        self.denominator = n_denominator * m
    elif m_numerator is not None:
        self.numerator = m_denominator * n
        self.denominator = m_numerator

    elif isinstance(num, int) and isinstance(denom, int):
        self.numerator = n
        self.denominator = m


  def float_to_rational(self, n):
    if n.is_integer():
        return int(n), 1
      
    sign = -1 if n < 0 else 1
    n = abs(n)

    str_n = str(n)
    if '.' in str_n:
        decimal_places = len(str_n.split('.')[1])
    else:
        decimal_places = 0

    numerator = round(n * (10 ** decimal_places))
    denominator = 10 ** decimal_places

    common_div = math.gcd(numerator, denominator)

    return sign * (numerator // common_div), denominator // common_div

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
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator


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
            raise TypeError("other must be an integer or Rational")


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
            raise TypeError("other must be an integer or Rational")


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
            raise TypeError("other must be an integer or Rational")

  def __div__(self, other):
    if isinstance(other, Rational):
      return Rational(self.numerator * other.denominator, self.denominator * other.numerator)
    elif isinstance(other, int):
      if other == 0:
        raise ValueError("You can't divide by zero.")
      else:
        return Rational(self.numerator, self.denominator * other)
    else:
      raise TypeError("other must be an integer or Rational")

  def __eq__(self, other):
    if isinstance(other, Rational):
      return (self.numerator * other.denominator) == (self.denominator * other.numerator)
    elif isinstance(other, int):
      return self.numerator == (other * self.denominator)
    else:
      raise ValueError("other must be an int or Rational")


  def __pow__(self, other: int | None):
        if not isinstance(other, int):
            raise TypeError("other operand must be an int")
        if other < 0:
            return Rational(self.denominator ** abs(other), self.numerator ** abs(other))
        elif other > 0:
            return Rational(self.numerator ** other, self.denominator ** other)
          
  def __round__(self, n=None):
      if n is None:
          return Rational(round(self.numerator / self.denominator))
      else:
          factor = 10 ** n
          round_numerator = round(self.numerator * factor / self.denominator)
          return Rational(round_numerator, factor)

  def __abs__(self):
    return Rational(abs(self.numerator), abs(self. denominator))

  def __ne__(self, value):
    return not self == other

  def __str__(self):
    return str(round(self.__numerator / self.__denominator, 10))

  def __repr__(self):
    return f"Rational({self.__numerator}, {self.__denominator})"

  def print_fraction(self):
    return f"Rational number: ({self.__numerator} / {self.__denominator})"

  def __int__(self):
      return self.numerator // self.denominator

  def __float(self):
    return self.numerator / self.denominator
  
  def __min__(self):
    return Rational(-self.numerator, self.denominator)
