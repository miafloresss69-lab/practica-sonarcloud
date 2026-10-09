
import os

# Vulnerabilidad: contraseña escrita directamente en el código
DB_PASSWORD = "SuperSecretPassword123!"

# Función para calcular el promedio
def calcular_promedio(valores):
    if len(valores) == 0:
        return 0

    suma = 0
    for v in valores:
        suma += v

    return suma / len(valores)

# Código no utilizado
def funcion_inutil():
    pass
