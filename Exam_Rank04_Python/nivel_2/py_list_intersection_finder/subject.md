## py_list_intersection_finder 
---

Escribe una función que encuentre la intersección de varias listas ordenadas. Devuelve una nueva lista que contenga los elementos que aparecen en TODAS las listas de entrada, en orden ordenado.

La función debe:
- Devolver los elementos que aparecen en TODAS las listas
- El resultado debe estar ordenado en orden ascendente
- Eliminar duplicados del resultado
- Manejar adecuadamente las entradas vacías o listas vacías
- Si alguna lista está vacía, la intersección está vacía

**Funciones permitidas:** Ninguna. Utiliza solo las funciones permitidas para evitar un cero el día del examen.
**Firma:** `def list_intersection_finder(lists: list[list[int]]) -> list[int]:`

### Salida
```py
list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]])             # Salida -> [2, 3]
list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]])      # Salida -> [4]
list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]])    # Salida -> [1, 2, 3]
list_intersection_finder([[1, 2, 3], [4, 5, 6]])                        # Salida -> []
list_intersection_finder([])                                            # Salida -> []
list_intersection_finder([[1, 2, 3], []])                               # Salida -> []
list_intersection_finder([[5]])                                         # Salida -> [5]
```