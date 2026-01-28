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
