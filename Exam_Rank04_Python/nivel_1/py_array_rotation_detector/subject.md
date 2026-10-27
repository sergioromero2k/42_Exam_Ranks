## array_rotation_detector 
---

Escribe una función en Python que tome dos listas (matrices) como parámetros y determine si la segunda lista es una rotación de la primera (hacia la izquierda o hacia la derecha).

Una rotación significa que los elementos se desplazan de forma circular. Por ejemplo, desplazar [1, 2, 3] a la derecha una posición da como resultado [3, 1, 2].

La función debe devolver True si arr2 es una rotación de arr1, y False en caso contrario.
Si las matrices tienen longitudes diferentes, no pueden ser rotaciones entre sí.
Dos matrices vacías se consideran rotaciones entre sí.

**Funciones permitidas:** collections.deque.rotate(). Utiliza solo las funciones permitidas para evitar un cero el día del examen.
**Firma:** `def array_rotation_detector(arr1: list, arr2: list) -> bool:`

### Salida
```py
array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3])   # Salida: True
array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4])   # Salida: True
array_rotation_detector([1, 2, 3], [3, 2, 1])               # Salida: False
array_rotation_detector([1, 2], [1, 2, 3])                  # Salida: False
array_rotation_detector([], [])                             # Salida: True
```