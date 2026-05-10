from empleado import Empleado
from gerente import Gerente
from archivo import guardar_empleado, leer_empleados


def main():
    """Función principal del programa."""
    # Crear empleados
    emp1 = Empleado("Ana Gutierrez", "10234567", 2_500_000)
    emp2 = Empleado("Antonio Pérez", "10987654", 2_200_000)
    ger1 = Gerente("David Ramírez", "20112233", 4_000_000, 1_500_000)
    emp3 = Empleado("María López", "10032569", 2_300_000)
    emp4 = Empleado("Juan Rodriguez", "107654569", 2_500_000)
    ger2 = Gerente("Gustavo Díaz", "12547893", 6_000_000, 2_500_000)

    empleados = [emp1, emp2, emp3, emp4, ger1, ger2]

    # Polimorfismo: el mismo método funciona diferente según el tipo
    print("=== Nómina del mes ===")
    for persona in empleados:
        print(persona)  # Llama a __str__ de cada clase

    # Guardar en archivo
    print("\n=== Guardando en archivo ===")
    for persona in empleados:
        guardar_empleado(persona)
        print(f"  Guardado: {persona.nombre}")

    # Leer desde archivo
    print("\n=== Empleados registrados ===")
    leer_empleados()


if __name__ == "__main__":
    main()