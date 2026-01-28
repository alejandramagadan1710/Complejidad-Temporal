# Complejidad-Temporal
Comparación del tiempo de ejecución de Bubble Sort, Merge Sort y Quick Sort en Python.

La complejidad temporal es el número de operaciones que realiza un algoritmo para completar su tarea (considerando que cada operación dura el mismo tiempo). El algoritmo que realiza la tarea en el menor número de operaciones se considera el más eficiente en términos de complejidad temporal. Sin embargo, la complejidad espacial y temporal se ve afectada por factores como el sistema operativo y el hardware, pero no los incluiremos en discusión.
# Bubble Sort

El ordenamiento burbuja hace múltiples pasadas a lo largo de una lista. Compara los ítems adyacentes e intercambia los que no están en orden. Cada pasada a lo largo de la lista ubica el siguiente valor más grande en su lugar apropiado. En esencia, cada ítem “burbujea” hasta el lugar al que pertenece.

Su codigo en Python seria el siguiente.

```python
# Metodo Bubble Sort

def bubblesort(vector): # Definimos Bubble Sort y vector es la lista de numeros con la que voy a trabajar
    n = len(vector) # Se define el tamaño n para saber que cantidad de numeros vamos a comparar
    for i in range(n - 1): # Este for se utiliza para repetir el proceso de ordenar varias veces, se utiliza n - 1 porque cuando queda 1 elemento ya no se necesita mover
        for j in range(0, n - i - 1): # En este for , i indica cuantos elementos ya no tenemos que tocar y cada pasada se va recorriendo 1 
            if vector[j] > vector[j + 1]: # Comparamos si el elemento de la isquierda es mayor que el de la derecha entonces esta en el orden incorrecto
                vector[j], vector[j + 1] = vector[j + 1], vector[j] # El numero mayor se va moviendo hacia la derecha , por lo cual se van intercambiando
```

# Merge Sort

Ahora dirigimos nuestra atención a usar una estrategia de dividir y conquistar como una forma de mejorar el desempeño de los algoritmos de ordenamiento. El primer algoritmo que estudiaremos es el ordenamiento por mezcla. El ordenamiento por mezcla es un algoritmo recursivo que divide continuamente una lista por la mitad. Si la lista está vacía o tiene un solo ítem, se ordena por definición (el caso base). Si la lista tiene más de un ítem, dividimos la lista e invocamos recursivamente un ordenamiento por mezcla para ambas mitades. Una vez que las dos mitades están ordenadas, se realiza la operación fundamental, denominada mezcla. La mezcla es el proceso de tomar dos listas ordenadas más pequeñas y combinarlas en una sola lista nueva y ordenada.

```python
# Metodo Merge Sort

def mergesort(vector): # Definimos Merge Sort y vector es la lista de numeros a comparar
    if len(vector) > 1: # Si la lista tiene 1 elemento, ya esta ordenada
        medio = len(vector) // 2 # Se divide la lista en dos partes
        izq = vector[:medio] # Parte izquierda de la lista
        der = vector[medio:] # Parte derecha de la lista

        mergesort(izq) # Recursion en la parte izquierda
        mergesort(der) # Recursion en la parte derecha

        i = j = k = 0 # Contadores para izquierda, derecha y vector final

        while i < len(izq) and j < len(der): # Mientras ambas listas tengan elementos
            if izq[i] < der[j]: # Comparamos elementos
                vector[k] = izq[i]
                i += 1
            else:
                vector[k] = der[j]
                j += 1
            k += 1

        while i < len(izq): # Copia los elementos restantes de la izquierda
            vector[k] = izq[i]
            i += 1
            k += 1

        while j < len(der): # Copia los elementos restantes de la derecha
            vector[k] = der[j]
            j += 1
            k += 1
```
# Quick Sort

El ordenamiento rápido usa dividir y conquistar para obtener las mismas ventajas que el ordenamiento por mezcla, pero sin utilizar almacenamiento adicional. Sin embargo, es posible que la lista no se divida por la mitad. Cuando esto sucede, veremos que el desempeño disminuye.

Un ordenamiento rápido primero selecciona un valor, que se denomina el valor pivote. Aunque hay muchas formas diferentes de elegir el valor pivote, simplemente usaremos el primer ítem de la lista. El papel del valor pivote es ayudar a dividir la lista. La posición real a la que pertenece el valor pivote en la lista final ordenada, comúnmente denominado punto de división, se utilizará para dividir la lista para las llamadas posteriores a la función de ordenamiento rápido.

```python
# Metodo Quick Sort

def quicksort(vector): # Definimos Quick Sort y vector es la lista de numeros a comparar
    def quick(vec, inicio, fin): # Definimos la lista, el inicio y el fin
        if inicio >= fin: # Si inicio es mayor o igual al fin, ya esta ordenado
            return

        pivot = vec[inicio] # Elegimos el primer elemento como pivote
        menor = inicio + 1 # Avanza desde la izquierda
        mayor = fin # Retrocede desde la derecha

        while True:
            while menor <= mayor and vec[mayor] >= pivot:
                mayor -= 1
            while menor <= mayor and vec[menor] <= pivot:
                menor += 1
            if menor <= mayor:
                vec[menor], vec[mayor] = vec[mayor], vec[menor]
            else:
                break

        vec[inicio], vec[mayor] = vec[mayor], vec[inicio] # Coloca el pivote en su posicion correcta
        quick(vec, inicio, mayor - 1) # Lado izquierdo
        quick(vec, mayor + 1, fin) # Lado derecho

    quick(vector, 0, len(vector) - 1) # Llamada inicial
```
# Medicion de Tiempo

```python
# Metodo para medir el tiempo de ejecucion

def medir_tiempo(algoritmo, lista): # Definimos la medicion de tiempo y recibimos el algoritmo y la lista
    copia = lista.copy()  # Se hace una copia para no modificar la lista original
    inicio = time.perf_counter() # Guardamos el tiempo inicial
    algoritmo(copia) # Ejecutamos el algoritmo con la lista copiada
    fin = time.perf_counter() # Guardamos el tiempo final
    return fin - inicio # Retornamos el tiempo total de ejecucion
```
# Comparacion de Metodos

```python
# Comparacion de tiempos y tabla de resultados

tamanos = list(range(50, 1050, 50))  # Definimos los tamaños de nuestras listas

tiempos_bubble = []  # Listas para guardar los tiempos
tiempos_merge = []
tiempos_quick = []

for n in tamanos:  # Recorremos cada tamaño de la lista
    lista = sample(range(10000), n)  # Creamos una lista de numeros aleatorios

    tiempos_bubble.append(medir_tiempo(bubblesort, lista))  # Medimos los tiempos
    tiempos_merge.append(medir_tiempo(mergesort, lista))
    tiempos_quick.append(medir_tiempo(quicksort, lista))

# Tabla de comparacion

print("\nTamaño | Bubble Sort (s) | Merge Sort (s) | Quick Sort (s)")
print("----------------------------------------------------------")

for i in range(len(tamanos)):
    print(f"{tamanos[i]:6d} | {tiempos_bubble[i]:15.6f} | {tiempos_merge[i]:14.6f} | {tiempos_quick[i]:14.6f}")
```
# Grafica comparativa de los algoritmos de ordenamiento

```python
plt.plot(tamanos, tiempos_bubble, label="Bubble Sort")
plt.plot(tamanos, tiempos_merge, label="Merge Sort")
plt.plot(tamanos, tiempos_quick, label="Quick Sort")

plt.xlabel("Tamaño de la lista (N)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Comparación de algoritmos de ordenamiento")
plt.legend()
plt.grid(True)
plt.show()
```


