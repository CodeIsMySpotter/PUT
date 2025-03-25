import math

def decimal_string_to_exponent(decimal_str: str) -> int:
    if '.' in decimal_str:
        parts = decimal_str.split('.')
        int_part = int(parts[0]) if parts[0] else 0  # Część całkowita
        frac_part_str = parts[1] if len(parts) > 1 else "0"
    else:
        int_part = int(decimal_str)
        frac_part_str = "0"
    
    if int_part > 0:
        return int_part.bit_length() - 1  # floor(log2(int_part))
    
    # Jeśli integer_part == 0, analizujemy część ułamkową
    frac_part = int(frac_part_str)  # Liczba po przecinku jako int
    frac_bits = len(frac_part_str) * 3.32192809489  # log2(10) ~ 3.32 -> oszacowanie ilości bitów
    
    # Konwertujemy część ułamkową na binarną i szukamy pierwszej '1'
    for i in range(int(math.ceil(frac_bits))):
        frac_part *= 2
        if frac_part >= 10**len(frac_part_str):  # Jeśli przekroczy 1.0
            return -(i + 1)  # Eksponent odpowiada pierwszej jedynce
    
    return float('-inf')  # Jeśli liczba to dokładnie 0

# Przykłady
print(bin(decimal_string_to_exponent("256") + 127))           # 8  (2⁸ = 256)
print(bin(decimal_string_to_exponent("0.125") + 127))         # -3 (2⁻³ = 0.125)
print(bin(decimal_string_to_exponent("1.5") + 127))           # 0  (największa potęga 2 w 1.5 to 2⁰)
print(bin(decimal_string_to_exponent("0.0009765625") + 127))  # -10 (2⁻¹⁰ = 0.0009765625)
