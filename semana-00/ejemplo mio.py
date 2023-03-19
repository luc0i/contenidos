import os

path1 = "Programación avanzada\contenidos\semana-00\ejemplo_mio.py"

dirname1 = os.path.dirname(path1)
basename1 = os.path.basename(path1)
print(f'path: {path1}')
print(f'dirname: {dirname1}')
print(f'basename: {basename1}')


ruta_juego_1 = "C:\Users\rturn\OneDrive - Universidad Católica de Chile\Documentos\Universidad (actual)\Programación avanzada\contenidos\semana-00\data\gato"
ruta_juego_1_1 = os.path.join("semana00", "data", "gato", "juego_1.txt")

print(ruta_juego_1_1)
archivo = open(ruta_juego_1_1, "rt")
archivo.readlines()
