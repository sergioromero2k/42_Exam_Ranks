## merge_sorted_lists
---
Dadas varias listas de enteros (ya ordenadas), devuelve una única lista con todos los elementos ordenados.

```py
def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
```

### Salida
merge_sorted_lists([[1, 3, 5], [2, 4, 6]])        # → [1, 2, 3, 4, 5, 6]
merge_sorted_lists([[-3, 0, 5], [-1, 2, 4]])      # → [-3, -1, 0, 2, 4, 5]
merge_sorted_lists([[1], [2], [3]])                # → [1, 2, 3]
merge_sorted_lists([[1, 2, 3]])                    # → [1, 2, 3]
merge_sorted_lists([[], [1, 2], []])              # → [1, 2]
merge_sorted_lists([])                             # → []
merge_sorted_lists([[5, 5], [5, 5]])              # → [5, 5, 5, 5]
merge_sorted_lists([[1, -3, 5], [2, 4, 6], [-4, -5, 6]])  # → [-5, -4, -3, 1, 2, 4, 5, 6, 6]