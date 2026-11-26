import os

# CORRECCION (vulnerabilidad): la contraseña ya no esta escrita en el codigo,
# se lee desde una variable de entorno.
DB_PASSWORD = os.getenv("DB_PASSWORD")


def calcular_promedio(valores):
    """Regresa el promedio de una lista de numeros (0 si la lista esta vacia)."""
    # CORRECCION (code smell): verificacion simple de lista vacia y uso de sum()
    if not valores:
        return 0
    return sum(valores) / len(valores)

# CORRECCION (code smell): se elimino la funcion sin uso funcion_inutil()
