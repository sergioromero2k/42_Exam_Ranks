"""Tienes una fila de números y miras de k en k. En cada grupo apuntas el más grande, y luego avanzas un paso."""


def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    return [max(nums[i:i + k]) for i in range(len(nums) - k + 1)] if k > 0 else []
