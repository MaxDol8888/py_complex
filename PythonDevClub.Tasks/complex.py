import math
class Complex(object):

    real = 0.0
    imaginary = 0.0

    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary
        

    def __str__(self,):
        tempStringSource = []
        if self.real is not 0:
            tempStringSource.append("%.2f" % round(self.real, 2))

        if self.imaginary > 0 :
            if self.real is not 0:
                self.imaginary = math.fabs(self.imaginary)
                tempStringSource.append(" + ")

        if self.imaginary < 0:
            if self.real is not 0:
                oldImaginary = self.imaginary
                self.imaginary = math.fabs(self.imaginary)
                tempStringSource.append(" - ")

        if self.imaginary is not 0:
            tempStringSource.append("%.2fi" % round(self.imaginary, 2))

        result = "".join(tempStringSource)
        
        return result

    def add(self, comp):
        """ (m + ni) + (p + qi) = (m + p) + (n + q)i """

        result = Complex(self.real + comp.real,self.imaginary + comp.imaginary)
        return result
    
    def __add__(self, other):
        return self.add(other)
    
    def subtract(self,comp):
        """ (m + ni) - (p + qi) = (m - p) + (n - q)i """
        result = Complex(self.real - comp.real, self.imaginary - comp.imaginary)
        return result
    
    def __sub__(self, other):
        return self.subtract(other)

    def multiply(self, other):
        """ (m + ni) * (p + qi) = (m * p) + (n * q)i """
        return Complex(self.real * other.real,self.imaginary * other.imaginary)

    def __mul__(self, other):
        return self.multiply(other)

    def divide(self,other):
        """ (m + ni) / (p + qi) = (m / p) + (n / q)i """
        return Complex(self.real / other.real,self.imaginary / other.imaginary)

    def __truediv__(self, other):
        return self.divide(other)