class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return True
        else:
            return False


    def __lt__(self, other):
        if self.a*other.b < other.a*self.b:
            return True

        else:
            return False

    def __gt__(self, other):

        if self.a*other.b > other.a*self.b:
            return True

        else:
            return False

    def fraction_mod(self, frac):
        if frac.a > frac.b:
            for i in range(frac.b, 2):
                if frac.a%i == 0:
                    return Fraction(frac.a/i, frac.b/i)

        else:
            for i in range(frac.a, 2):
                if frac.b%i == 0:
                    return Fraction(frac.a/i, frac.b/i)


    def __add__(self, other):
        nominator = self.a * other.b + other.a * self.b
        denominator = self.b * other.b
        summ = Fraction(nominator, denominator)
        summ = self.fraction_mod(summ)
        return summ

    def __sub__(self, other):
        nominator = self.a * other.b - other.a * self.b
        denominator = self.b * other.b
        summ = Fraction(nominator, denominator)
        summ = self.fraction_mod(summ)
        return summ

if __name__ == '__main__':
    a = Fraction(1,2)
    b = Fraction(2,1)

    print(a<b)
    print(a==b)
    print(a+b)
    print(a-b)