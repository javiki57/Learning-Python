#!/usr/bin/env python3

class Vehiculo:

    def __init__(self, matricula, modelo):
        self.matricula = matricula
        self.modelo = modelo
        self.disponible = True

    def alquilar(self):
        if self.disponible:
            self.disponible = False
        else:
            print(f"El vehículo con matrícula {self.matricula} no está disponible")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
        else:
            print(f"El vehículo con matrícula {self.matricula} ya estaba disponible")


    def __str__(self):
        return f"Vehículo(matrícula={self.matricula}, modelo={self.modelo}, disponible={self.disponible})"

class Flota:

    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def alquilar_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.alquilar()

    def devolver_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.devolver()


    def __str__(self):
    
        return "\n".join(str(vehiculo) for vehiculo in self.vehiculos)

if __name__ == "__main__":

    flota = Flota()

    flota.agregar_vehiculo(Vehiculo("DEJ6812", "Toyota Corolla"))
    flota.agregar_vehiculo(Vehiculo("KTL1837", "Honda Civic"))

    print(f"\n[+] Flota inicial:\n")
    print(flota)

    print(f"\n[+] Flota después de alquilar DEJ6812:\n")
    flota.alquilar_vehiculo("DEJ6812")
    print(flota)
    
    print(f"\n[+] Flota después de devolver DEJ6812:\n")
    flota.devolver_vehiculo("DEJ6812")
    print(flota)
    
