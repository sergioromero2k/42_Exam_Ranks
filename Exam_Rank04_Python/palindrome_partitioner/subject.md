## min_cuts_no_modules
---

Dado un string, devuelve el número mínimo de cortes para que cada parte sea un palíndromo. 
Sin usar módulos externos.

### Salida
```
""          → 0
"a"         → 0
"racecar"   → 0
"ab"        → 1   # "a"|"b"
"abc"       → 2   # "a"|"b"|"c"
"aab"       → 1   # "aa"|"b"
"aabcb"     → 1   # "aa"|"bcb"
"abacd"     → 2   # "aba"|"c"|"d"
"ababbbabbababa" → 3
```