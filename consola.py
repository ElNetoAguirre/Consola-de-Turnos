"""
Consola de generación de turnos para una Farmacia
"""

import turnos


def preguntar():
    """Bienvenida y pregunta la categoría"""
    print("Bienvenido a Farmacias 'El Neto'")
    while True:
        print("[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmética")
        try:
            mi_area = input("Elija su area: ").upper()
            ["P", "F", "C"].index(mi_area)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            break
    turnos.decorador(mi_area)


def inicio():
    """Inicio"""
    while True:
        preguntar()
        try:
            otro_turno = input("Quieres generar otro turno? [S] - Si, [N] - No: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita a Farmacias 'El Neto'")
                break


inicio()
