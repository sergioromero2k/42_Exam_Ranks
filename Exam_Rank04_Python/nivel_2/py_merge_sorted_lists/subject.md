## py_merge_sorted_lists 
---

Escribe una función que fusione múltiples listas ordenadas en una sola lista ordenada de forma eficiente.

La función debe:
- Tomar como entrada una lista de listas de enteros ordenadas
- Devolver una única lista fusionada en orden ascendente
- Conservar todos los elementos duplicados en el resultado final
- Manejar listas vacías y entradas vacías de forma adecuada
- Mantener una eficiencia óptima para entradas grandes

**Funciones / módulos prohibidos:** sorted(), .sort(), heapq.merge(). Utiliza solo las funciones permitidas para evitar un cero el día del examen.
**Firma:** `def merge_sorted_lists(lists: list[list[int]]) -> list[int]:`
### Salida
```py
merge_sorted_lists([[1, 3, 5], [2, 4, 6]])                  # Salida -> [1, 2, 3, 4, 5, 6]
merge_sorted_lists([[1, 5, 9], [2, 3, 8], [4, 6, 7]])       # Salida -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
merge_sorted_lists([[5], [1, 3], [2, 4]])                   # Salida -> [1, 2, 3, 4, 5]
merge_sorted_lists([[1, 1, 2], [2, 3, 3]])                  # Salida -> [1, 1, 2, 2, 3, 3]
merge_sorted_lists([[], [1, 2, 3]])                         # Salida -> [1, 2, 3]
merge_sorted_lists([[]])                                    # Salida -> []
merge_sorted_lists([[-5, -1, 0], [-3, 2, 4]])               # Salida -> [-5, -3, -1, 0, 2, 4]
merge_sorted_lists([[10], [10], [10]])                      # Salida -> [10, 10, 10]
```