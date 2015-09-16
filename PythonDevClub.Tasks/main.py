from complex import Complex
import unittest
from tests import TestComplexNumbers

print(Complex(1, 2))
print(Complex(0, 2))
print(Complex(1, -2))
print(Complex(0, -2))
print(Complex(-1, -2))

print(Complex(1,2).add(Complex(1,2)))
print(Complex(1,-2).add(Complex(1,-2)))

suite = unittest.TestLoader().loadTestsFromTestCase(TestComplexNumbers)
unittest.TextTestRunner(verbosity=2).run(suite)