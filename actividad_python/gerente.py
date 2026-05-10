from empleado import Empleado


class Gerente(Empleado):
    """Representa a un gerente. Hereda de Empleado y agrega un bono."""

    def __init__(self, nombre, cedula, salario_base, bono):
        super().__init__(nombre, cedula, salario_base)
        self.bono = bono

    def calcular_salario(self):
        """Polimorfismo: salario base + bono del gerente."""
        return self.salario_base + self.bono

    def __str__(self):
        return (
            f"Gerente: {self.nombre} | "
            f"Cédula: {self.cedula} | "
            f"Salario: ${self.calcular_salario():,.0f} "
            f"(incluye bono de ${self.bono:,.0f})"
        )