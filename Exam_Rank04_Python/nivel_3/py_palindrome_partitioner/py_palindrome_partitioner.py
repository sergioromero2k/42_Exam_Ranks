"""
Tienes que cortar una palabra en trozos de forma que cada trozo sea un palíndromo (que se lee igual al derecho y al revés), 
    usando el menor número de cortes posible.
La función devuelve cuántos cortes hacen falta."""


def palindrome_partitioner(s: str) -> int:
    if s == s[::-1]:
        return 0
    return min(1 + palindrome_partitioner(s[i:]) for i in range(1, len(s)) if s[:i] == s[:i][::-1])
