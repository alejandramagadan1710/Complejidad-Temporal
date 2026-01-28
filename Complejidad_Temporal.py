import time # Agregar librerias Time  para la comparacion de tiempo de ejecucion de cada metodo
import matplotlib.pyplot as plt  # Agregar Libreria Matplotlib para graficar los metodos de ordenamiento
from random import sample # Agregar libreria random para seleccionar numeros aleatorios 


# Metodo Bubble Sort

def bubblesort(vector): # Definimos Bubble Sort y vector es la lista de numeros con la que voy a trabajar
    n = len(vector) # Se define el tamaño n para saber que cantidad de numeros vamos a comparar
    for i in range(n - 1): # Este for se utiliza para repetir el proceso de ordenar varias veces, se utiliza n - 1 porque cuando queda 1 elemento ya no se necesita mover
        for j in range(0, n - i - 1): # En este for , i indica cuantos elementos ya no tenemos que tocar y cada pasada se va recorriendo 1 
            if vector[j] > vector[j + 1]: # Comparamos si el elemento de la isquierda es mayor que el de la derecha entonces esta en el orden incorrecto
                vector[j], vector[j + 1] = vector[j + 1], vector[j] # El numero mayor se va moviendo hacia la derecha , por lo cual se van intercambiando


# Metodo Merge Sort

def mergesort(vector): # Definimos Merge Sort y vector es la lista de numeros a comparar
    if len(vector) > 1: # Si la lista tiene 1 elemento , ya esta ordenada , si no es asi se sigue con el procedimiento
        medio = len(vector) // 2 # Se nos da el tamaño total de la lista (vector) y se divide en 2
        izq = vector[:medio] # Parte izquierda de la lista
        der = vector[medio:] # Parte derecha de la lista

        mergesort(izq) # Recursion en la parte izquierda hasta llegar a 1 elemento
        mergesort(der) # Recursion en la parte derecha hasta llegar a 1 elemento

        i = j = k = 0 # Se crean 3 contadores, i para la parte izq , j para der y k para nuestro vector

        while i < len(izq) and j < len(der):  # Mientras las dos listas tengan elementos
            if izq[i] < der[j]: # Si el elemnto de la isq es menor , se guarda en vector 
                vector[k] = izq[i] # Y avanzamos en i 
                i += 1
            else:    # Si el de la derecha es menor 
                vector[k] = der[j] # Se guarda ese y avanzamos en j
                j += 1
            k += 1 # Siempre se avanza la posicion del vector final

        while i < len(izq):  # Copea los elementos que quedaron a la izquierda
            vector[k] = izq[i]
            i += 1
            k += 1

        while j < len(der): # Copea los elementos que quedaron a la derecha
            vector[k] = der[j]
            j += 1
            k += 1

# Quick Sort

def quicksort(vector): # Definimos Quick Sort y vector es la lista de numeros a comparar
    def quick(vec, inicio, fin): # Definimos nuestra lista (vec), el inicon y el fin 
        if inicio >= fin: # Si inicio es mayor o igual a el final entonces se retorna y ya esta ordenado
            return

        pivot = vec[inicio] # Elegimos un pivote , este sera el primer numero de nuestro rango
        menor = inicio + 1 # El numero menor avanza desde la izquierda
        mayor = fin # El numero mayor retrocede desde el final

        while True:
            while menor <= mayor and vec[mayor] >= pivot: # Mientras el numero sea mayor o igual al pivote 
                mayor -= 1 # Retrocedemos
            while menor <= mayor and vec[menor] <= pivot: # Mientras el numero sea menor o igual al pivote
                menor += 1 # Avanzamos
            if menor <= mayor: # Si un numero es menor al pivote de la derecha o mayor al numero de la izquierda
                vec[menor], vec[mayor] = vec[mayor], vec[menor] # Los intercambiamos
            else:
                break

        vec[inicio], vec[mayor] = vec[mayor], vec[inicio] # El pivote se coloca en su posicion correcta
        quick(vec, inicio, mayor - 1) # Todo lo que es menor o igual al pivote se coloca de lado izquierdo
        quick(vec, mayor + 1, fin) # Todo lo que es mayor al pivote se coloca a la derecha de este mismo

    quick(vector, 0, len(vector) - 1) # Comienza desde el vector 0 hasta el final de nuestra lista


# Medicion de tiempos

def medir_tiempo(algoritmo, lista): # Denimos nuestra medicion de tiempo y colocamos el algoritmo que vamos a medir y la lista
    copia = lista.copy()  # para no modificar la original
    inicio = time.perf_counter() # Guardamos el tiempo exacto
    algoritmo(copia) # Se ejecuta el algoritmo de la lista copeada
    fin = time.perf_counter() # Paramos el tiempo exacto
    return fin - inicio # Restamos el tiempo final - tiempo inicial


# Comparacion de tiempos 

tamanos = list(range(50, 1050, 50)) # Definimos los tamaños de nuestras listas

tiempos_bubble = [] # Listas para guardar los tiempos
tiempos_merge = []
tiempos_quick = []

for n in tamanos: # Recorremos cada tamaño de la lista
    lista = sample(range(10000), n) # Creamos nuestra lista de numero aleatorios

    tiempos_bubble.append(medir_tiempo(bubblesort, lista)) # Medimos los tiempos de cada algoritmo
    tiempos_merge.append(medir_tiempo(mergesort, lista))
    tiempos_quick.append(medir_tiempo(quicksort, lista))

# Tabla de comparacion

print("\nTamaño | Bubble Sort (s) | Merge Sort (s) | Quick Sort (s)")
print("----------------------------------------------------------")

for i in range(len(tamanos)):
    print(f"{tamanos[i]:6d} | {tiempos_bubble[i]:15.6f} | {tiempos_merge[i]:14.6f} | {tiempos_quick[i]:14.6f}")


# Grafica comparativa 

plt.plot(tamanos, tiempos_bubble, label="Bubble Sort")
plt.plot(tamanos, tiempos_merge, label="Merge Sort")
plt.plot(tamanos, tiempos_quick, label="Quick Sort")

plt.xlabel("Tamaño de la lista (N)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Comparación de algoritmos de ordenamiento")
plt.legend()
plt.grid(True)
plt.show()
