"""Rotar los elementos de una lista hacia la derecha k posiciones."""


def rotate_right(arr: list, k: int) -> list:
    if k == 0 or not arr:
        return (arr)
    else:
        k %= len(arr)
    return (arr[-k:] + arr[:-k])
