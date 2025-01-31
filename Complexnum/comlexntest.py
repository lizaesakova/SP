import unittest
from rational import Rational
from complex_number import ComplexNumber
import math

class TestRational(unittest.TestCase):

    def test_init(self):
        r = Rational(3, 4)
        self.assertEqual(r.numerator, 3)
        self.assertEqual(r.denominator, 4)

        r = Rational(8, 16)
        self.assertEqual(r.numerator, 1)
        self.assertEqual(r.denominator, 2)

        with self.assertRaises(ValueError):
            Rational(42, 0)

    def test_float_to_rational(self):
        r = Rational(0.25)
        self.assertEqual(r.numerator, 1)
        self.assertEqual(r.denominator, 4)

        r = Rational(0.6)
        self.assertEqual(r.numerator, 3)
        self.assertEqual(r.denominator, 5)

    def test_strange_input(self):
        r = Rational(0.4, 1.2)  
        self.assertEqual(str(r), "1/3") 

        r1 = Rational(0.5)  
        self.assertEqual(str(r1), "1/2")

        r2 = Rational(3, 1.5) 
        self.assertEqual(str(r2), "2")

        r3 = Rational(2.5, 5) 
        self.assertEqual(str(r3), "1/2")

        r4 = Rational(Rational(1, 4), Rational(3, 8))
        self.assertEqual(str(r4), "2/3")

        r5 = Rational(3, Rational(7, 2)) 
        self.assertEqual(str(r5), "6/7")

        r6 = Rational(Rational(3, 4), 3)
        self.assertEqual(str(r6), "1/4")

    def test_add(self):
        r1 = Rational(2, 5)
        r2 = Rational(1, 4)
        result = r1 + r2
        self.assertEqual(result.numerator, 13)
        self.assertEqual(result.denominator, 20)

    def test_sub(self):
        r1 = Rational(3, 5)
        r2 = Rational(1, 2)
        result = r1 - r2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 10)

    def test_mul(self):
        r1 = Rational(2, 3)
        r2 = Rational(3, 4)
        result = r1 * r2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 2)

    def test_div(self):
        r1 = Rational(5, 6)
        r2 = Rational(2, 3)
        result = r1 / r2
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 4)

        with self.assertRaises(ZeroDivisionError):
            r1 / Fraction(0)

        result = r1 / 2
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 12)

        self.assertEqual(r1.__truediv__("string"), NotImplemented)


    def test_eq(self):
        r1 = Rational(3, 4)
        r2 = Rational(3, 4)
        self.assertTrue(r1 == r2)

        r3 = Rational(6, 8)
        self.assertTrue(r1 == r3)

        r4 = Rational(2, 5)
        self.assertFalse(r1 == r4)

        self.assertEqual(r1.__eq__("string"), NotImplemented)
      
    def test_pow(self):
        r = Rational(3, 2)
        result = r ** 3
        self.assertEqual(result.numerator, 27)
        self.assertEqual(result.denominator, 8)

        self.assertEqual(r.__pow__("string"), NotImplemented)

    def test_round(self):
        r = Rational(3, 2)
        self.assertEqual(round(r), Rational(3, 1))

        r = Rational(1, 3)
        self.assertEqual(round(r, 2), Rational(33, 100))

    def test_abs(self):
        f = Rational(-3, 2)
        self.assertEqual(abs(r), Rational(3, 2))

        f = Rational(1, -7)
        self.assertEqual(abs(r), Rational(1, 7))
      
    def test_ne(self):
        r1 = Rational(1, 3)
        r2 = Rational(1, 3)
        self.assertFalse(r1 != r2)

        r3 = Rational(2, 5)
        self.assertTrue(r1 != r3)

        self.assertEqual(r1.__ne__("string"), NotImplemented)
  
    def test_str(self):
        r = Rational(2, 3)
        self.assertEqual(str(r), "2/3")

        r = Rational(-3)
        self.assertEqual(str(r), "-3")
      
    def test_int(self):
        r = Rational(3, 2)
        self.assertEqual(int(r), 1)

    def test_float(self):
        r = Rational(3, 4)
        self.assertEqual(float(r), 0.75)

    def test_min(self):
        r = Rational(1, 2)
        self.assertEqual(-r, Rational(-1, 2))


class TestComplex(unittest.TestCase):

    def test_init(self):
        c = ComplexNumber(2, 3)
        self.assertEqual(c.real, 2)
        self.assertEqual(c.imag, 3)

        c = ComplexNumber(Fraction(3, 4), Fraction(5, 6))
        self.assertEqual(c.real, Fraction(3, 4))
        self.assertEqual(c.imag, Fraction(5, 6))

    def test_setters(self):
        c = ComplexNumber(2, 3)
        c.real = -5
        c.imag = -10
        self.assertEqual(c, ComplexNumber(-5, -10))

    def test_add(self):
        c1 = ComplexNumber(2, 3)
        c2 = ComplexNumber(4, 5)
        result = c1 + c2
        self.assertEqual(result.real, 6)
        self.assertEqual(result.imag, 8)

        result = c1 + 3
        self.assertEqual(result.real, 5)
        self.assertEqual(result.imag, 3)

    def test_iadd(self):
        c1 = ComplexNumber(2, 3)
        c1 += 1
        self.assertEqual(c1.real, 3)
        self.assertEqual(c1.imag, 3)

        c1 = ComplexNumber(2, 3)
        c1 += ComplexNumber(4, 5)
        self.assertEqual(c1.real, 6)
        self.assertEqual(c1.imag, 8)
      
        c1 = ComplexNumber(Rational(1, 3), Rational(2, 3))
        c1 += Fraction(1, 5)
        self.assertEqual(c1.real, Rational(8, 15))
        self.assertEqual(c1.imagine, Rational(10, 15))

        self.assertEqual(c1.__iadd__("string"), NotImplemented)

    def test_sub(self):
        c1 = ComplexNumber(2, 3)
        c2 = ComplexNumber(4, 5)
        result = c1 - c2
        self.assertEqual(result.real, -2)
        self.assertEqual(result.imag, -2)

        result = c1 - 3
        self.assertEqual(result.real, -1)
        self.assertEqual(result.imag, 3)

    def test_isub(self):
        c1 = ComplexNumber(2, 3)
        c1 -= 1
        self.assertEqual(c1.real, 1)
        self.assertEqual(c1.imag, 3)

        c1 = ComplexNumber(2, 3)
        c1 -= ComplexNumber(4, 5)
        self.assertEqual(c1.real, -2)
        self.assertEqual(c1.imag, -2)

        c1 = ComplexNumber(1, 2)
        c1 -= Rational(1, 2)
        self.assertEqual(c1.real, Rational(1, 2))
        self.assertEqual(c1.imagine, Rational(3, 2))

        self.assertEqual(c1.__isub__("string"), NotImplemented)
      
    def test_mul(self):
        c1 = ComplexNumber(2, 3)
        c2 = ComplexNumber(4, 5)
        result = c1 * c2
        self.assertEqual(result.real, -7)
        self.assertEqual(result.imag, 22)

        result = c1 * 2
        self.assertEqual(result.real, 4)
        self.assertEqual(result.imag, 6)
      
    def test_imul(self):
        c1 = ComplexNumber(1, 3)
        c1 *= 2
        self.assertEqual(c1.real, 2)
        self.assertEqual(c1.imagine, 6)

        c1 = ComplexNumber(1, 2)
        c1 *= ComplexNumber(3, 4)
        self.assertEqual(c1.real, -9)
        self.assertEqual(c1.imagine, 13)

        c1 = ComplexNumber(1, 2)
        c1 *= Rational(1, 2)
        self.assertEqual(c1.real, Rational(1, 2))
        self.assertEqual(c1.imagine, 1)

        self.assertEqual(c1.__imul__("string"), NotImplemented)
      
    def test_truediv(self):
        c1 = ComplexNumber(2, 3)
        c2 = ComplexNumber(4, 5)
        result = c1 / c2
        self.assertEqual(result.real, Rational(23, 41))
        self.assertEqual(result.imag, Rational(2, 41))

        result = c1 / 2
        self.assertEqual(result.real, Rational(1, 1))
        self.assertEqual(result.imag, Rational(3, 2))

        with self.assertRaises(ZeroDivisionError):
            c1 / 0
          
    def test_itruediv(self):
        c1 = ComplexNumber(1, 2)
        c2 = ComplexNumber(3, 4)
        c1 /= c2
        self.assertEqual(c1.real, Rational(11, 25))
        self.assertEqual(c1.imagine, Rational(2, 25))

        c1 = ComplexNumber(1, 2)
        c1 /= 2
        self.assertEqual(c1.real, Rational(1, 2))
        self.assertEqual(c1.imagine, 1)

        with self.assertRaises(ZeroDivisionError):
            c1 /= 0

        self.assertEqual(c1.__itruediv__("string"), NotImplemented)
      
    def test_eq(self):
        c1 = ComplexNumber(2, 3)
        c2 = ComplexNumber(2, 3)
        self.assertTrue(c1 == c2)

        c3 = ComplexNumber(2, 4)
        self.assertFalse(c1 == c3)
      
    def test_ne(self):
        c1 = ComplexNumber(1, 2)
        c2 = ComplexNumber(1, 2)
        self.assertFalse(c1 != c2)

        c3 = ComplexNumber(1, 3)
        self.assertTrue(c1 != c3)

        self.assertEqual(c1.__ne__("string"), NotImplemented)
      
    def test_min(self):
        c1 = ComplexNumber(5, 4)
        self.assertEqual(c1.__min__(), ComplexNumber(-5, -4))
      
    def test_pow(self):
        c = ComplexNumber(1, 1)
        result = c ** 3
        self.assertEqual(result.real, -2)
        self.assertEqual(result.imag, 2)
      
    def test_arg(self):
        c = ComplexNumber(1, 1)
        self.assertEqual(c.arg(), math.pi / 4)
      
    def test_abs(self):
        c = ComplexNumber(3, 4)
        self.assertEqual(abs(c), 5)

    def test_str(self):
        c = ComplexNumber(2, 3)
        self.assertEqual(str(c), "2 + 3i")

        c = ComplexNumber(2, -3)
        self.assertEqual(str(c), "2 - 3i")

        c = ComplexNumber(2, 0)
        self.assertEqual(str(c), "2")

    def test_repr(self):
        c = ComplexNumber(3, 4)
        self.assertEqual(repr(c), "Complex(real=3, imagine=4)")

        c = ComplexNumber(Rational(1, 2), Rational(3, 4))
        self.assertEqual(repr(c), "Complex(real=1/2, imagine=3/4)")

    def test_type_error_add(self):
        c = ComplexNumber(1, 42)
        with self.assertRaises(TypeError):
            c + "string"
          
    def test_type_error_iadd(self):
        c = ComplexNumber(1, 42)
        with self.assertRaises(TypeError):
            c += "string"
          
    def test_type_error_sub(self):
        c = ComplexNumber(1, 42)
        with self.assertRaises(TypeError):
            c - "string"

    def test_type_error_isub(self):
        c = ComplexNumber(1, 42)
        with self.assertRaises(TypeError):
            c -= "string"

    def test_type_error_mul(self):
        c = ComplexNumber(1, 42)
        with self.assertRaises(TypeError):
            c * "string"
          
    def test_type_error_imul(self):
        c = ComplexNumber(1, 42)
        with self.assertRaises(TypeError):
            c *= "string"
          
    def test_type_error_truediv(self):
        c = ComplexNumber(1, 42)
        with self.assertRaises(TypeError):
            c / "string"
          
    def test_type_error_itruediv(self):
        c = ComplexNumber(1, 42)
        with self.assertRaises(TypeError):
            c /= "string" 
          
    def test_type_error_pow(self):
        c = ComplexNumber(1, 42)
        with self.assertRaises(TypeError):
            c ** "string"

    def test_not_implemented_add(self):
        c = ComplexNumber(1, 42)
        self.assertEqual(c.__add__("string"), NotImplemented)

    def test_not_implemented_sub(self):
        c = ComplexNumber(1, 42)
        self.assertEqual(c.__sub__("string"), NotImplemented)

    def test_not_implemented_mul(self):
        c = ComplexNumber(1, 42)
        self.assertEqual(c.__mul__("string"), NotImplemented)

    def test_not_implemented_truediv(self):
        c = ComplexNumber(1, 42)
        self.assertEqual(c.__truediv__("string"), NotImplemented)

    def test_not_implemented_pow(self):
        c = ComplexNumber(1, 42)
        self.assertEqual(c.__pow__("string"), NotImplemented)

    def test_not_implemented_eq(self):
        c = ComplexNumber(1, 42)
        self.assertEqual(c.__eq__("string"), NotImplemented)

    def test_not_implemented_ne(self):
        c = ComplexNumber(1, 42)
        self.assertEqual(c.__ne__("string"), NotImplemented)

    def test_type_error_abs(self):
        c = ComplexNumber(1, 42)
        with self.assertRaises(TypeError):
            abs(c, "extra_arg")

    def test_type_error_min(self):
        c = ComplexNumber(1, 42)
        with self.assertRaises(TypeError):
            -c("extra_arg")

    def test_type_error_arg(self):
        c = ComplexNumber(1, 42)
        with self.assertRaises(TypeError):
            c.arg("extra_arg")

    def test_truediv_zero_division(self):
        c1 = ComplexNumber(42, 3)
        c2 = ComplexNumber(0, 0)
        with self.assertRaises(ZeroDivisionError):
            c1 / c2
