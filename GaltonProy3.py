# Se utiliza la librería matplotlib para poder realizar un histograma
import random
import matplotlib.pyplot as plt

# se establecen las 2 variables
num_canicas = 3000
num_niveles = 12

# Se crea una función en donde se vaya incrementando cada número de canicas y cada uno de los niveles + 1
def simular_galton(num_canicas, num_niveles):
    contenedores = [0] * (num_niveles + 1)
    for i in range(num_canicas):
        pos = 0
        for j in range(num_niveles):
            if random.random() < 0.5: #se utiliza la prob .05 para que se ponga al centro, de lo contrario se centra a la IZQ o derecha
                pos += 1
        contenedores[pos] += 1
    return contenedores

# se establece una función para graficar para que se puedan contar los bins y weights y se pueda representar el histograma
def graficar_histograma(contenedores):
    plt.hist(range(len(contenedores)), bins=len(contenedores), weights=contenedores)
    plt.xlabel('Contenedor')
    plt.ylabel('Cantidad de canicas')
    plt.title('Histograma de la simulación de la máquina de Galton')
    plt.show()

contenedores = simular_galton(num_canicas, num_niveles)
graficar_histograma(contenedores)