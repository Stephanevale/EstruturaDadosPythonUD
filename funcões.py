class Triangulo:
    def __init__(self, lado1, lado2, lado3, base, altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura

    def Area(self):
        return (self.base * self.altura) / 2

T1 = Triangulo(3,4,4,5,9)
print(T1.lado1, T1.lado2, T1.lado3, T1.base, T1.altura)
print(T1.Area())

T2 = Triangulo(2,2,3,4,5)
print(T2.lado1, T2.lado2, T2.lado3, T2.base, T2.altura)
print(T2.Area())