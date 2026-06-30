## resolve_dependencies
---
Dado un diccionario de paquetes donde cada clave es un paquete y su valor es la lista de sus dependencias, devuelve el orden de instalación válido (las dependencias primero). Reglas:

* Si un paquete tiene una dependencia que no existe, se descarta junto a todos los que dependan de él
* Si hay ciclos, devuelve []
* En caso de empate, orden alfabético
* Si el input es vacío, devuelve []

### Salida
```
# Cadena lineal
{"A": ["B"], "B": ["C"], "C": []}
# → ["C", "B", "A"]

# Nodo independiente
{"independent": []}
# → ["independent"]

# Empate alfabético
{"Z": [], "M": [], "A": []}
# → ["A", "M", "Z"]

# Árbol con ramas
{"App": ["LibraryX", "LibraryY"], "LibraryX": ["Core"], "LibraryY": ["Core"], "Core": []}
# → ["Core", "LibraryX", "LibraryY", "App"]

# Dependencia fantasma
{"ValidPackage": [], "BrokenPackage": ["GhostDependency"], "DependentOnBroken": ["BrokenPackage"]}
# → ["ValidPackage"]

# Ciclo directo
{"chicken": ["egg"], "egg": ["chicken"]}
# → []

# Ciclo parcial (aunque A es válido, hay ciclo → [])
{"X": ["A", "Y"], "Y": ["X"], "A": []}
# → []

# Ciclo largo
{"A": ["B"], "B": ["C"], "C": ["D"], "D": ["A"]}
# → []

# Vacío
{}
# → []
```