 
# Proyecto: Informe de notas con Python y Docker

## Integrantes
- Jana Cervera
- Pablo Cuñat
  

## Descripción
Programa desarrollado en Python que recorre una lista de alumnos y muestra sus nombres, notas y estado (aprobado o suspendido).

También calcula:
- Número total de alumnos.
- Número de aprobados.
- Número de suspendidos.
- Media de las notas del grupo.

## Archivos del proyecto
- `notas.py`: código del programa en Python.
- `Dockerfile`: instrucciones para construir la imagen Docker.
- `README.md`: documentación del proyecto.

## Construir la imagen Docker

Desde la carpeta del proyecto, ejecutar:

```bash
docker build -t notas-alumnos .
```

## Ejecutar el contenedor

```bash
docker run --rm notas-alumnos
```

## Actualizar el programa

Si se modifica `notas.py`, es necesario reconstruir la imagen y ejecutar de nuevo:

```bash
docker build -t notas-alumnos .
docker run --rm notas-alumnos
```

## Resultado esperado

El programa muestra el informe de notas y finaliza automáticamente.

```text
Total de alumnos: 5
Aprobados: 3
Suspendidos: 2
Media del grupo: 6.40
```
