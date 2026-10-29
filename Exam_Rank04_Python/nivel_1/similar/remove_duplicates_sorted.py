"""Eliminar los elementos repetidos de una lista ordenada."""


def remove_duplicates_sorted(nums: list[int]) -> list[int]:
    new_lst: list[int] = []

    for num in nums:
        if not new_lst or num != new_lst[-1]:
            new_lst.append(num)
    return new_lst
