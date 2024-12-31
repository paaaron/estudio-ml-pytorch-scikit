import os

capitulos = 0  # Número de capítulos completados
ejercicios = 0  # Número de ejercicios resueltos
ejemplos = 0  # Número de ejemplos implementados

resumen = f"""
# Resumen de Estudio

- Capítulos completados: {capitulos}
- Ejercicios resueltos: {ejercicios}
- Ejemplos implementados: {ejemplos}
"""

with open("progreso/resumen-semanal.md", "a") as file:
    file.write(resumen)

print("Resumen semanal generado.")
