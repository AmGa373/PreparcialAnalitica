#El Jardin Botanico de Medellín necesita contratar una solución de análitica de datos, 
#para almacenar procesar y definir el estado actual de los arboles sembrados 
#a lo largo de la avenida 80, esto con el fin de informar que arboles se deben talar 
#y cuales transplantar.

import random
import pandas as pd

def generar_simulacion(numero_simulaciones):

    nombres_semilla = ["pino", "mamoncillo", "sauce", "cedro", "ceiba"]
    estados_semilla = ["optimo", "malo", "mejoria"]
    alturas_semilla = [30,15,5,3,12]
    direcciones_semilla = ["av 80 #44a-30", "av 80 #30-25", "av 80 #100-24", "av 80 #48a-02", "av 80 #16a-20"]
    botanicos_semilla = ["Jose Sosa", "Andres Insignares", "Camila Orozco", "Catalina Suarez", "Carlos Santana"]

    simulaciones = []
    for _ in range(numero_simulaciones):

        simulacion = {
            "id":random.randint(0,200),
            "botanico_encargado":random.choice(botanicos_semilla),
            "direccion":random.choice(direcciones_semilla),
            "altura":random.choice(alturas_semilla),
            "estado":random.choice(estados_semilla),
            "nombre":random.choice(nombres_semilla)
        }

        probabilidad_error = random.random()

        if probabilidad_error < 0.2:
            simulacion["id"] = None
        elif probabilidad_error < 0.4:
            simulacion["id"] = random.choice([-10,-1,0])
            simulacion["direccion"] = random.choice(["av 7 bogota", None])
        elif probabilidad_error < 0.6:
            simulacion["estado"] = "chocolate"
            simulacion["nombre"] = simulacion["nombre"].upper()
        elif probabilidad_error < 0.8:
            simulacion["botanico_encargado"] = random.choice([None, -1, "sin"])

        simulaciones.append(simulacion)

    print(simulaciones)

    tabla = pd.DataFrame(simulaciones)
    print(tabla)