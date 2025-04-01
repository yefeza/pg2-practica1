# Practica 1

## Implementacion Calculadora Estandar

Este módulo implementa una calculadora estándar que permite realizar operaciones
aritméticas básicas como suma, resta, multiplicación y división. El modo de
funcionamiento es el siguiente:

```python
from calculadora import Calculadora

calc = Calculadora()
print(calc.sumar(2, 3))       # Devuelve 5
print(calc.restar(5, 2))      # Devuelve 3
print(calc.multiplicar(2, 3)) # Devuelve 6
print(calc.dividir(6, 2))     # Devuelve 3.0
print(calc.dividir(6, 0))     # Devuelve "Error: Division por cero"
```
