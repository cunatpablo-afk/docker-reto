
alumnos = [
    {"nombre": "Ana", "nota": 8.5},
    {"nombre": "Luis", "nota": 4.0},
    {"nombre": "Marta", "nota": 7.0},
    {"nombre": "Pablo", "nota": 3.5},
    {"nombre": "Sara", "nota": 9.0},
]


def calcular_media(alumnos):
    """
    Calcula la media de las notas de una lista de alumnos.

    Parámetros:
        alumnos (list): Lista de diccionarios con nombre y nota.

    Devuelve:
        float: Media de las notas redondeada a 2 decimales.
        Si la lista está vacía, devuelve 0.
    """
    if len(alumnos) == 0:
        return 0

    suma_notas = 0

    for alumno in alumnos:
        suma_notas += alumno["nota"]

    media = suma_notas / len(alumnos)

    return round(media, 2)


# Inicializar contadores
total_alumnos = 0
aprobados = 0
suspendidos = 0

# Recorrer alumnos
for alumno in alumnos:
    nombre = alumno["nombre"].upper()
    nota = alumno["nota"]

    total_alumnos += 1

    if nota >= 5:
        estado = "Aprobado"
        aprobados += 1
    else:
        estado = "Suspendido"
        suspendidos += 1

    print(f"{nombre} - Nota: {nota} - {estado}")

# Mostrar resumen

print(f"Total de alumnos: {total_alumnos}")
print(f"Aprobados: {aprobados}")
print(f"Suspendidos: {suspendidos}")
print(f"Media del grupo: {calcular_media(alumnos):.2f}")
