"""
Estandares y buenas practicas en Python, PEP8
Autor: Brayan Edgar Blanco Camacho
Registro: 219182965
"""
import math

class Empleado:
    """
    Una clase simple para representar un empleado.
    """

    def __init__(self, nombre, apellido, salario):
        """
        Inicializa a un empleado.

        Parameters:
            nombre (str): Solo el nombre o nombres del empleado.
            apellido (str): Solo el apellido o apellidos del empleado.
            salario (int or float): El salario del empleado.
        """
        
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario

    def nombre_completo(self):
        """
        Devuelve el nombre completo del empleado.

        Returns:
            str: Concatenacion de nombre(s) y apellido(s).
        """
        return f"{self.nombre} {self.apellido}"

    def aplicar_aumento(self, porcentaje):
        """
        Aplica un aumento porcentual al salario del empleado.

        Parameters:
            porcentaje (int or float): porcentaje que se incrementara al salario del empleado.

        Raises:
            ValueError: Si el porcentaje es negativo.
        
        Returns:
            float: El nuevo salario con el porcentaje incrementado.
        """
        if porcentaje < 0:
            raise ValueError("El porcentaje debe ser un valor positivo.")
        
        self.salario += self.salario * (porcentaje / 100)
        return self.salario
    
    def redondear_salario(self):
        """
        Devuelve un redondeo del salario.

        Returns:
            int: El salario redondeado hacia el valor mas cercano mayor o igual al salario actual.
        """
        return math.ceil(self.salario)

    def __str__(self):
        """
        Devuelve una representación en cadena del empleado.

        Returns:
            str: Devuelve una cadena con los datos del empleado. 
        """
        return f"Empleado: {self.nombre_completo()}, Salario: {self.salario:.2f}"
    

if __name__ == "__main__":
    print("*Ingresando datos del Nuevo Empleado:*")
    nombre = input("Ingrese solo el nombre: ")
    apellido = input("Ingrese solo el apellido: ")
    salario = float(input("Ingrese el salario que se asignara: "))
    empleado_1 = Empleado(nombre, apellido, salario)
    empleado_1.aplicar_aumento(50.5)
    print(empleado_1)
    print(f"Salario redondeado: {empleado_1.redondear_salario()}")



    
