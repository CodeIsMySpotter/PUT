import numpy as np

SIZES = [
        250, 500, 750, 1000,
        1250, 1500, 1750, 2000
        
]


class Generator:
    def generate_increasing( n: int) -> np.ndarray:
        return np.arange(n)

    def generate_decreasing( n: int) -> np.ndarray:
        return np.arange(n, 0, -1)

    def generate_random(n: int) -> np.ndarray:
        return np.random.randint(0, 32767, n)

    def generate_A_random(n: int) -> np.ndarray:
        half = n // 2
        first_half = np.arange(half)
        second_half = np.arange(half, 0, -1)
        return np.concatenate((first_half, second_half))

    def generate_V_random(n: int) -> np.ndarray:
        half = n // 2
        first_half = np.arange(half, 0, -1)
        second_half = np.arange(half)
        return np.concatenate((first_half, second_half))
