import unittest
from complex import Complex
 
 
class TestComplexNumbers(unittest.TestCase):
 
    def test_normal(self):
        x = Complex(1, 3)
 
        self.assertEqual(str(x), "1.00 + 3.00i", "Complex number 1.00 + 3.00i doesn't print the correct value")
 
    def test_zero_real(self):
        x = Complex(0, 15)
 
        self.assertEqual(str(x), "15.00i", "Complex number 15.00i doesn't print the correct value")
 
    def test_negative_imaginary(self):
        x = Complex(1.539, -2.5)
 
        self.assertEqual(str(x), "1.54 - 2.50i", "Complex number 1.539 - 2.50i doesn't print the correct value")
 
    def test_negative_imaginary_with_zero_real(self):
        x = Complex(0, -999)
        actual = str(x)
        self.assertEqual(actual, "-999.00i", "Complex number -999.00i doesn't print the correct value")
 
    def test_both_negative(self):
        x = Complex(-10, -20)
 
        self.assertEqual(str(x), "-10.00 - 20.00i", "Complex number -10.00 - 20.00i doesn't print the correct value")

    def test_adding_positives(self):
        result = Complex(10, 20) + Complex(1,2)
 
        self.assertEqual(str(result), "11.00 + 22.00i", "Adding two positive complex numbers didn't print the correct value")

    def test_adding_negatives(self):
        result = Complex(-10, -20) + Complex(-1,-2)
 
        self.assertEqual(str(result), "-11.00 - 22.00i", "Adding two negative complex numbers didn't print the correct value")

    def test_adding_negative_to_positive(self):
        result = Complex(10, 20) + Complex(-1,-2)
 
        self.assertEqual(str(result), "9.00 + 18.00i", "Adding a negative complex to a positive complex number didn't print the correct value")

    def test_adding_negative_to_positive_reults_negative(self):
        x = Complex(1, 2)
        y = Complex(-2,-3)
        result = x + y
 
        self.assertEqual(str(result), "-1.00 - 1.00i", "Adding a negative complex to a positive complex number didn't print the correct value")

    def test_subract_positives(self):
        result = Complex(1,2) - Complex(2,3)
 
        self.assertEqual(str(result), "-1.00 - 1.00i", "Adding a negative complex to a positive complex number didn't print the correct value")

    def test_multiply_positives(self):
        result = Complex(1.0,2.0) * Complex(2.0,3.0)
 
        self.assertEqual(str(result), "2.00 + 6.00i", "Multiplying a negative complex to a positive complex number didn't print the correct value")
    
    def test_divide_positives(self):
        result = Complex(1,2) / Complex(2,3)
 
        self.assertEqual(str(result), "0.50 + 0.67i", "Dividing a negative complex to a positive complex number didn't print the correct value")

    def test_divide_with_zero_throws_ZeroDivisionError(self):
        self.assertRaises(ZeroDivisionError,Complex(1,2).divide ,Complex(0,3))
 
 
#if __name__ == '__main__':
#    unittest.main()