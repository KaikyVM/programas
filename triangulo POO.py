from ast import main


class triangulo:
 
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def areatriangulo(self):
        if self.lado1 > self.lado2 and self.lado1 >self.lado3:
            self.base = self.lado1

        elif self.lado2 > self.lado1 and self.lado2 >self.lado3:
            self.base = self.lado2
        
        elif self.lado3 > self.lado1 and self.lado3 >self.lado2:
            self.base = self.lado3

        altura = ((self.lado1 + self.lado2 + self.lado3) / 2)
        area = (self.base * altura) / 2
        print(f"o valor da area do triangulo é igual {area:.2f}" )

    
    def perimetrotriangulo(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        print(f"o valor do perimetro do triangulo é igual {perimetro:.2f}" )

    def entradausuario(self):
        self.lado1 = float((input("digite o valor do lado 1 triangulo: ")))
        self.lado2 = float((input("digite o valor do lado 2 triangulo: ")))
        self.lado3 = float((input("digite o valor do lado 3 triangulo: ")))

triangulo_instancia = triangulo(0, 0, 0)

triangulo_instancia.entradausuario()
triangulo_instancia.perimetrotriangulo()
triangulo_instancia.areatriangulo()

