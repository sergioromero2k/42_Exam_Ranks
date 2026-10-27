## constellation_mapper 
---

Escribe una función que proyecte una constelación de estrellas en una cuadrícula y devuelva la representación visual como una lista de cadenas.

La función debe:
- Tomar una lista de coordenadas de estrellas como tuplas (fila, columna) y el tamaño de la cuadrícula como entero
- Devolver una lista de cadenas que represente la cuadrícula
- Las estrellas se representan con '*' y los espacios vacíos con '.'
- Las coordenadas de la cuadrícula comienzan en (0, 0) en la esquina superior izquierda
- Ignorar las coordenadas fuera de los límites de la cuadrícula
- Manejar coordenadas duplicadas (cada estrella aparece solo una vez).

**Funciones permitidas:** Ninguna. Utiliza solo las funciones permitidas para evitar un cero el día del examen.
**Firma:** `def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:`
### Salida
```py
constellation_mapper([(0, 0), (1, 1), (2, 2)], 3)                   # Salida -> ['*..', '.*.', '..*']
constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3)   # Salida -> ['.*.', '***', '.*.']
constellation_mapper([], 2)                                         # Salida -> ['..', '..']
constellation_mapper([(0, 0), (0, 0), (1, 1)], 2)                   # Salida -> ['*.', '.*']
constellation_mapper([(0, 0), (5, 5)], 3)                           # Salida -> ['*..', '...', '...']
constellation_mapper([(1, 0), (1, 1), (1, 2)], 3)                   # Salida -> ['...', '***', '...']
```