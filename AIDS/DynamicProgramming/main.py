from itertools import combinations

def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().strip().split('\n')
        n, capacity = map(int, lines[0].split())
        items = [tuple(map(int, line.split())) for line in lines[1:]]
    return items, capacity

def greedy_knapsack(items, capacity):
    indexed_items = [(i, w, v, v / w) for i, (w, v) in enumerate(items)]
    indexed_items.sort(key=lambda x: x[3], reverse=True)

    total_value, total_weight = 0, 0
    chosen = []

    for i, w, v, _ in indexed_items:
        if total_weight + w <= capacity:
            chosen.append(i)
            total_weight += w
            total_value += v

    return chosen, total_weight, total_value

def brute_force_knapsack(items, capacity):
    n = len(items)
    best_value = 0
    best_weight = 0
    best_combo = []

    for r in range(1, n + 1):
        for combo in combinations(range(n), r):
            total_weight = sum(items[i][0] for i in combo)
            total_value = sum(items[i][1] for i in combo)
            if total_weight <= capacity and total_value > best_value:
                best_value = total_value
                best_weight = total_weight
                best_combo = list(combo)

    return best_combo, best_weight, best_value

def dynamic_knapsack(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w, v = items[i - 1]
        for c in range(capacity + 1):
            if w <= c:
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - w] + v)
            else:
                dp[i][c] = dp[i - 1][c]


    for row in dp:
        print(row)
    print()

    chosen = []
    c = capacity
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i - 1][c]:
            chosen.append(i - 1)
            c -= items[i - 1][0]

    total_weight = sum(items[i][0] for i in chosen)
    total_value = sum(items[i][1] for i in chosen)

    return chosen[::-1], total_weight, total_value

def compare_algorithms(file_path):
    items, capacity = read_input(file_path)
    print("Dane z pliku:", file_path)
    print("Pojemność plecaka:", capacity)
    print("Liczba przedmiotów:", len(items))
    print("")

    for name, algorithm in [
        ("AD (Dynamiczny)", dynamic_knapsack),
        ("AZ (Zachłanny)", greedy_knapsack),
        ("AB (Brute-force)", brute_force_knapsack)
    ]:
        chosen, total_w, total_v = algorithm(items, capacity)
        print(f"  {name}")
        print(f"  Wybrane indeksy: {chosen}")
        print(f"  Sumaryczny rozmiar: {total_w}")
        print(f"  Całkowita wartość: {total_v}\n")

if __name__ == "__main__":
    compare_algorithms("dane.txt")
