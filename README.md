# Practica 1

En esta práctica se implementa una calculadora en Python que permite realizar
operaciones aritméticas básicas como suma, resta, multiplicación y división.

Del mismo modo, se implementa una calculadora de factorial que aplica principios
de herencia y polimorfismo.

## Preparación del entorno y ejecución

1. Clonar el repositorio:

```bash
git clone https://github.com/yefeza/pg2-practica1.git
cd pg2-practica1
```

2. Crear un entorno virtual:

```bash
python -m venv env
```

3. Activar el entorno virtual:

- En Windows:

```bash
.\env\Scripts\activate
```

- En Linux o Mac:

```bash
source env/bin/activate
```

4. Ejecutar el script:

```bash
python main.py
```

5. Desactivar el entorno virtual:

```bash
deactivate
```

## Implementacion Calculadora Estandar

Este módulo implementa una calculadora estándar que permite realizar operaciones
aritméticas básicas como suma, resta, multiplicación y división. El modo de
funcionamiento es el siguiente:

```python
from calculadora_poo import Calculadora

calculadora_1 = Calculadora()

print(calculadora_1.sumar(2, 5))
print(calculadora_1.restar(10, 9))
print(calculadora_1.multiplicar(5, 9))
print(calculadora_1.dividir(150, 6))
```

## Implementacion Calculadora Factorial

Este módulo implementa una calculadora factorial que hereda de la clase
Calculadora. Permite calcular el factorial de un número entero positivo. El modo
de funcionamiento es el siguiente:

```python
from calculadora_poo import CalculadoraFactorial
calculadora_factorial = CalculadoraFactorial(numero=5)
print(calculadora_factorial.calcular())
```
