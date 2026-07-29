def obtener_palindromos(words: list[str]) -> list[str]:
    if not words:
        return []
    return sorted(w for w in words if w.lower() == w.lower()[::-1])