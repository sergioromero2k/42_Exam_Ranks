## obtener_palindromos
---
Dada una lista de palabras, devuelve las que son palíndromos (ignorando mayúsculas), ordenadas alfabéticamente.
```py
def obtener_palindromos(words: list[str]) -> list[str]:
```

### Salida
```
obtener_palindromos([])                              # → []
obtener_palindromos(["casa", "perro", "sol"])        # → []
obtener_palindromos(["radar"])                       # → ["radar"]
obtener_palindromos(["Ana", "oso", "radar"])         # → ["Ana", "oso", "radar"]
obtener_palindromos(["Aba", "aba", "ABA"])           # → ["ABA", "Aba", "aba"]
obtener_palindromos(["a", "b", "c"])                 # → ["a", "b", "c"]
obtener_palindromos(["radar", "casa", "oso", "perro", "Ana", "sol"])  # → ["Ana", "oso", "radar"]