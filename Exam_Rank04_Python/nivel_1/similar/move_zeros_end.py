"""Mover todos los ceros al final de una lista, manteniendo el orden de los demás números."""


def move_zeros_end(nums: list[int]) -> list[int]:
    zeros_counter: int = 0
    new_lst: list[int] = []

    for num in nums:
        if num == 0:
            zeros_counter += 1
        else:
            new_lst.append(num)

    new_lst += [0] * zeros_counter
    return new_lst
