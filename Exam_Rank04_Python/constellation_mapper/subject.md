## constellation_mapper 
---

Escribe una función **constellation_mapper(coordinates, size)** que reciba una lista de tuplas (row, col) y un entero size. Devuelve una grilla de size x size donde cada posición es "." excepto las coordenadas válidas que se marcan con "*". Cada fila se devuelve como string.

### Salida
```
constellation_mapper([(0, 0)], 3)
# → [["*.."], ["..."], ["..."]]

constellation_mapper([(0, 0), (1, 2), (2, 1)], 3)
# → [["*.."], ["..*"], [".*."]]

constellation_mapper([(-1, 0), (0, 0), (3, 3), (1, 5)], 3)
# → [["*.."], ["..."], ["..."]]  # los fuera de rango se ignoran

constellation_mapper([], 2)
# → [[".."], [".."]]

constellation_mapper([(0, 0)], 1)
# → [["*"]]

constellation_mapper([], 1)
# → [["."]]
```