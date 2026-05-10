class Empleado:
    """Representa a un empleado de la empresa."""

    def __init__(self, nombre, cedula, salario_base):
        self.nombre = nombre
        self.cedula = cedula
        self.salario_base = salario_base

    def calcular_salario(self):
        """Retorna el salario base. Las subclases pueden sobreescribir este método."""
        return self.salario_base

    def __str__(self):
        return (
            f"Empleado: {self.nombre} | "
            f"Cédula: {self.cedula} | "
            f"Salario: ${self.calcular_salario():,.0f}"
        )