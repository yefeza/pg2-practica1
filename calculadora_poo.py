import math


# Clase base que representa una calculadora simple (Abstracción)
class Calculadora:
    def __init__(self):
        self.__resultado = 0  # Atributo privado (Encapsulamiento)

    def sumar(self, a, b):
        self.__resultado = a + b
        return self.__resultado

    def restar(self, a, b):
        self.__resultado = a - b
        return self.__resultado

    def multiplicar(self, a, b):
        self.__resultado = a * b
        return self.__resultado

    def dividir(self, a, b):
        if b != 0:
            self.__resultado = a / b
            return self.__resultado
        else:
            return "Error: División por cero"

    def mostrar_resultado(self):
        return f"Resultado: {self.__resultado}"


# Clase que hereda de Calculadora y añade funciones científicas (Herencia)
class CalculadoraCientifica(Calculadora):
    def potencia(self, base, exponente):
        return math.pow(base, exponente)

    def raiz_cuadrada(self, numero):
        if numero >= 0:
            return math.sqrt(numero)
        else:
            return "Error: No se puede calcular la raíz de un número negativo"

    # Sobreescribimos el método mostrar_resultado (Polimorfismo)
    def mostrar_resultado(self):
        return f"Resultado científico: {super().mostrar_resultado()}"


# Ejemplo de uso
calc = CalculadoraCientifica()

print(calc.sumar(10, 5))  # 15
print(calc.restar(10, 5))  # 5
print(calc.multiplicar(10, 5))  # 50
print(calc.dividir(10, 5))  # 2.0
print(calc.potencia(2, 3))  # 8.0
print(calc.raiz_cuadrada(25))  # 5.0
print(calc.mostrar_resultado())  # "Resultado científico: Resultado: 2.0"
