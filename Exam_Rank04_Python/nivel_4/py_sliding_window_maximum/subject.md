## py_sliding_window_maximum
---
Escribe una función que encuentre el elemento máximo en cada ventana deslizante de tamaño k en un arreglo. Devuelve una lista de los máximos para cada posición de ventana.

La función debe:
- Deslizar una ventana de tamaño k a través del arreglo
- Encontrar el elemento máximo en cada posición de la ventana
- Devolver una lista de valores máximos
- Manejar casos límite (arreglo vacío, k <= 0, k > longitud del arreglo)
- Devolver una lista vacía para entradas no válidas

**Funciones permitidas:** Ninguna. Utiliza solo las funciones permitidas para evitar un cero el día del examen.
**Firma:** `def sliding_window_maximum(nums: list[int], k: int) -> list[int]:`

### Salida
```
sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3)   # Salida -> [3, 3, 5, 5, 6, 7]
sliding_window_maximum([1, 2, 3, 4, 5], 2)              # Salida -> [2, 3, 4, 5]
sliding_window_maximum([5, 4, 3, 2, 1], 1)              # Salida -> [5, 4, 3, 2, 1]
sliding_window_maximum([1, 2, 3], 3)                    # Salida -> [3]
sliding_window_maximum([1, 2, 3], 4)                    # Salida -> []
sliding_window_maximum([], 2)                           # Salida -> []
sliding_window_maximum([1, 2, 3], 0)                    # Salida -> []
```