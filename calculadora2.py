import math


# Clase base que representa una calculadora simple (Abstracción)
class Calculadora:
    def __init__(self, a, b):
        self.__resultado = 0
        self.a = a
        self.b = b
        self.operacion = ""

    def sumar(self):
        self.operacion = "Suma"
        self.__resultado = self.a + self.b
        return self._mostrar_operacion()

    def restar(self):
        self.operacion = "Resta"
        self.__resultado = self.a - self.b
        return self._mostrar_operacion()

    def multiplicar(self):
        self.operacion = "Multiplicar"
        self.__resultado = self.a * self.b
        return self._mostrar_operacion()

    def dividir(self):
        self.operacion = "Dividir"
        if self.b != 0:
            self.__resultado = self.a / self.b
            return self._mostrar_operacion()
        else:
            return "Error: División por cero"

    def _mostrar_operacion(self):
        return f"{self.operacion}: {self.a} y {self.b} = {self.__resultado}"


calculadora_1 = Calculadora(15, 5)

print(calculadora_1.sumar())

calculadora_2 = Calculadora(20, 5)

print(calculadora_2.restar())
calculadora_3 = Calculadora(20, 5)

print(calculadora_3.multiplicar())
calculadora_4 = Calculadora(20, 5)

print(calculadora_4.dividir())
