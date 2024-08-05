
# 💭 - TP Nº8 

### 🃏 - Ejercicio 1
Este código implementa una búsqueda lineal para encontrar un elemento en una lista. En este método, se recorre la lista desde el primer hasta el último elemento, comparando cada uno con el elemento buscado. Si se encuentra una coincidencia, se devuelve el índice del elemento. Si se llega al final de la lista sin encontrar el elemento, se retorna -1. A diferencia de la búsqueda binaria, la búsqueda lineal no requiere que la lista esté ordenada.

### 🃏 - Ejercicio 2
Este código utiliza un algoritmo de búsqueda binaria, encontrar un elemento en una lista ordenada. Primero, la lista se ordena para asegurar el correcto funcionamiento del algoritmo. Luego, se utilizan dos punteros (izq y der) para definir los límites de la búsqueda y un puntero central (medio) que divide la lista en dos partes. En cada iteración, se compara el elemento buscado con el elemento en la posición medio. Si coinciden, se devuelve el índice. Si el elemento buscado es mayor, se ajusta el límite izquierdo (izq) para descartar la mitad izquierda de la lista. Si es menor, se ajusta el límite derecho (der) para descartar la mitad derecha. 