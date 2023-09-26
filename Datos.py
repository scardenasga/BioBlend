import random

# Generar datos aleatorios dentro de los rangos proporcionados
num_muestras = 40  # Número de muestras

# Generar datos aleatorios para cada variable
masa = [random.uniform(0, 20) for _ in range(num_muestras)]
temperatura = [random.uniform(20, 40) for _ in range(num_muestras)]
ph = [random.uniform(6, 8) for _ in range(num_muestras)]
agua = [m / 2 for m in masa]

consumo_corriente = [random.uniform(1, 10) for _ in range(num_muestras)]

# Ruta donde se guardará el archivo de texto
ruta_archivo_txt = 'Datos/variables.csv'

# Escribir los datos en el archivo de texto
with open(ruta_archivo_txt, 'w') as file:
    # Escribir encabezados
    file.write("Masa (kg),Temperatura (°C),pH,Agua (ml),Consumo de Corriente (A)\n")
    
    # Escribir los datos
    for i in range(num_muestras):
        file.write(f"{masa[i]:.2f},{temperatura[i]:.2f},{ph[i]:.2f},{agua[i]:.2f},{consumo_corriente[i]:.2f}\n")

print('Archivo de texto creado con éxito:', ruta_archivo_txt)