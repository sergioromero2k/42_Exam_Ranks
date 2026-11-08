"""
Te dan dos listas y tienes que decir si la segunda es la primera girada, 
es decir, los mismos números en el mismo orden pero empezando en otro sitio, como si dieran la vuelta en círculo.
"""


def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False
    if not arr1:
        return True
    for i in range(len(arr1)):
        if arr1[i:] + arr1[:i] == arr2:
            return True
    return False
