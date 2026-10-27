## py_palindrome_partitioner 
---

Dada una cadena s, encuentra el número mínimo de cortes necesarios para particionarla de manera que cada subcadena resultante sea un palíndromo.

- Devuelve el número mínimo de cortes (un entero)
- Una cadena de longitud 1 requiere 0 cortes
- Una cadena vacía requiere 0 cortes

**Funciones permitidas:** Ninguna. Utiliza solo las funciones permitidas para evitar un cero el día del examen.
**Firma:** `def palindrome_partitioner(s: str) -> int:`

### Salida
```py
palindrome_partitioner("aab") # Salida -> 1
palindrome_partitioner("aba") # Salida -> 0
palindrome_partitioner("abc") # Salida -> 2
```