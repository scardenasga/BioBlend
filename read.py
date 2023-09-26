import csv

def leer_datos_desde_csv(ruta_archivo):
    masa = []
    temperatura = []
    ph = []
    agua = []
    consumo_corriente = []

    # Leer el archivo CSV y almacenar los datos en las listas
    with open(ruta_archivo, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            masa.append(float(row['Masa (kg)']))
            temperatura.append(float(row['Temperatura (°C)']))
            ph.append(float(row['pH']))
            agua.append(float(row['Agua (ml)']))
            consumo_corriente.append(float(row['Consumo de Corriente (A)']))

    return masa, temperatura, ph, agua, consumo_corriente
