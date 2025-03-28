import struct

def float64_to_bits(value):
    import math

    # 1. Ekstrakcja znaku
    sign = 0 if value >= 0 else 1
    value = abs(value)

    # 2. Znalezienie wykładnika i mantysy
    if value == 0:
        exp = 0
        mant = 0
    else:
        exp = int(math.log2(value))  # Znajdź wykładnik
        mant = value / (2 ** exp)  # Unormowana mantysa (1.XXXX * 2^exp)
        
        exp += 1023  # Bias dla IEEE 754 (bias = 2^(k-1) - 1, tutaj 1023)
        
        if exp <= 0:
            exp = 0  # Liczba zdenormalizowana
        elif exp >= 2047:
            exp = 2047  # Inf lub NaN

    # 3. Konwersja mantysy na 52-bitową wartość
    mant_bits = int((mant - 1) * (2**52)) if exp > 0 else int(mant * (2**52))

    # 4. Konwersja do bitów
    sign_bit = f"{sign:01b}"
    exp_bits = f"{exp:011b}"
    mant_bits = f"{mant_bits:052b}"

    return sign_bit + exp_bits + mant_bits

# 🔹 Przykład konwersji
decimal_number = 3.141592653589793
bit_representation = float64_to_bits(decimal_number)
print("64-bit IEEE 754:", bit_representation)




num = 3.141592653589793
bits = ''.join(f"{b:08b}" for b in struct.pack(">d", num))
print("64-bit IEEE 754:", bits)
