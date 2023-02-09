# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 19:41:40 2021

@author: Daniel
"""

"""
REMISIÓN DE PACIENTES 
Elaborado por: Daniel Mauricio Valdes Cabrera
Curso: Informática Médica

"""
import numpy as np
#1: Permitir el ingreso de pacientes
nombre = input("Nombre del paciente: ").lower()
ubicacion = int(input("Área asignada: "))

"""Cedula","Nombre","Apellido","Edad","Sexo","Domicilio","Ciudad","Telefono",
                       "No. Historial Clínico","Fumante","Procedencia","Fechas de Ingreso",
                       "No. piso","No. cama","Causas de Ingreso"""

#2: Asignar (urgencias, cirugía, hospitalización)
#3: Urgencia debe tener 2 camas, cirugía dos salas (4 personas) y hospitalización 23 salas (46 personas) con 2 camas cada una
#urgencias = np.array([])
#cirugia = np.array([])
#hospitalizacion = np.array([])

base_datos = {}
p1 = 0
p2 = 0
p3 = 0
#for i in range(0,3):
nombres = []
ubicaciones = []
if ubicacion == 1:
    nombres.append(nombre)
    ubicaciones.append(ubicacion)
    base_datos = {'nombres':nombres,'ubicacion':ubicaciones}
    p1 = p1 + 1
    
elif ubicacion == 2:
    nombres.append(nombre)
    ubicaciones.append(ubicacion)
    base_datos = {'nombres':nombres,'ubicacion':ubicaciones}
    p2 = p2 + 1
    
elif ubicacion == 3:
    nombres.append(nombre)
    ubicaciones.append(ubicacion)
    base_datos = {'nombres':nombres,'ubicacion':ubicaciones}
    p3 = p3 + 1
else:
    print("Esa opción no es correcta. Intente nuevamente.")
        
print(base_datos['nombres'],base_datos['ubicacion'])
print(base_datos.values())




#4: Cada sección tiene un doctor asignado

#5: Debe verificar cupo 