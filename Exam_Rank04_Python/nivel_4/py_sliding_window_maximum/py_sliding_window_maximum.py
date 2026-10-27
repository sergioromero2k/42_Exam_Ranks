from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0:
        return []

    dq = deque()  # guarda índices, el frente siempre es el máximo
    result = []

    for i, n in enumerate(nums):
        # Eliminar índices fuera de la ventana
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        # Eliminar índices de elementos menores al actual
        while dq and nums[dq[-1]] < n:
            dq.pop()
        dq.append(i)
        # Empezar a añadir resultados cuando la ventana está completa
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


def max_sliding_window2(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0:
        return []

    result = []
    for i in range(len(nums) - k + 1):
        curr_window = nums[i:i+k]
        result.append(max(curr_window))

    return result
