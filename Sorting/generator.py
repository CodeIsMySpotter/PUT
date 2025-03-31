import numpy as np

SIZES = [
        100, 200, 300, 400, 500,
        600, 700, 800, 900, 1000,
        1100, 1200, 1300, 1400, 1500,
        1600, 1700, 1800, 1900, 2000,
        2100, 2200, 2300, 2400, 2500  
]


class Generator:
    def generate_increasing( n: int) -> np.ndarray:
        return np.arange(n)

    def generate_decreasing( n: int) -> np.ndarray:
        return np.arange(n, 0, -1)

    def generate_random(n: int) -> np.ndarray:
        return np.random.randint(0, 10000, n)

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
