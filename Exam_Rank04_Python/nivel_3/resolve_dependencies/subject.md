## py_package_dependency_resolver 
---

Escribe una función que determine un orden de instalación de paquetes válido resolviendo dependencias. Usa ordenamiento topológico para garantizar que las dependencias se instalen antes de los paquetes que las requieren.

La función debe:
- Tomar un diccionario donde las claves son nombres de paquetes y los valores son listas de dependencias
- Devolver los paquetes en orden de instalación (dependencias primero)
- Devolver una lista vacía si no existe un orden válido (dependencias circulares)
- Manejar entradas vacías y cadenas de dependencias aisladas
- Ignorar referencias a paquetes que no están en el diccionario de entrada

**Funciones permitidas:** `graphlib.TopologicalSorter.` Utiliza solo las funciones permitidas para evitar un cero el día del examen.
**Firma:** `def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:`

### Salida
```py
package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []})        # Salida -> ["driver", "database", "app"]
package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]})                             # Salida -> ["A", "B", "C"]
package_dependency_resolver({})                                                                 # Salida -> []
package_dependency_resolver({"X": ["Y"], "Y": ["X"]})                                           # Salida -> []
package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]})    # Salida -> ["api", "web", "backend", "frontend"]
```