import csv
import os

ARCHIVO = "empleados.csv"


def guardar_empleado(empleado):
    """Agrega un empleado al archivo CSV."""
    es_nuevo = not os.path.exists(ARCHIVO)

    with open(ARCHIVO, mode="a", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        if es_nuevo:
            escritor.writerow(["tipo", "nombre", "cedula", "salario_base", "bono"])
        tipo = type(empleado).__name__
        bono = getattr(empleado, "bono", 0)
        escritor.writerow([tipo, empleado.nombre, empleado.cedula,
                           empleado.salario_base, bono])


def leer_empleados():
    """Lee y retorna todos los empleados desde el archivo CSV."""
    if not os.path.exists(ARCHIVO):
        print("No hay empleados registrados aún.")
        return

    with open(ARCHIVO, mode="r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            print(
                f"[{fila['tipo']}] {fila['nombre']} | "
                f"Cédula: {fila['cedula']} | "
                f"Salario base: ${float(fila['salario_base']):,.0f}"
            )