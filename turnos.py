"""
Generador de turnos para una Farmacia
"""

def numeros_perfumeria():
    """Generación de turnos para el área de Perfumería"""
    for num in range(1, 100000):
        yield f"P - {num}"


def numeros_farmacia():
    """Generación de turnos para el área de Farmacia"""
    for num in range(1, 100000):
        yield f"F - {num}"


def numeros_cosmetica():
    """Generación de turnos para el área de Cosmética"""
    for num in range(1, 100000):
        yield f"C - {num}"


p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()

def decorador(area):
    """Impresión de Turno o Ticket"""
    print("\n" + "*" * 23)
    print("Su número es: ")
    if area == "P":
        print(next(p))
    elif area == "F":
        print(next(f))
    elif area == "C":
        print(next(c))
    print("Aguarde y será atendido")
    print("*" * 23 + "\n")
