
import os

<<<<<<< HEAD
# VULNERABILIDAD: credenciales expuestas
DB_PASSWORD = "Secret123!"

def calcular_promedio(valores):
    # CODE SMELL: falta de manejo de lista vacía
=======
# Vulnerabilidad: contraseña escrita directamente en el código
DB_PASSWORD = "SuperSecretPassword123!"

# Función para calcular el promedio
def calcular_promedio(valores):
>>>>>>> d1127ae497dd999e2b0472140996387d24a878a7
    if len(valores) == 0:
        return 0

    suma = 0
    for v in valores:
        suma += v

    return suma / len(valores)

<<<<<<< HEAD
# CODE SMELL: código no utilizado
=======
# Código no utilizado
>>>>>>> d1127ae497dd999e2b0472140996387d24a878a7
def funcion_inutil():
    pass
