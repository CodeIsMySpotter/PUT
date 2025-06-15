import time
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from statistics import mean
from euler import *
from hamilton import *
import os
# ------------------------------
# Pomocnicze funkcje
# ------------------------------

def measure_time(func, *args):
    start = time.perf_counter()
    func(*args)
    return time.perf_counter() - start

def generate_hamiltonian_undirected_matrix(n, saturation_percent):
    max_possible_edges = (n * (n - 1)) // 2
    target_edge_count = int(max_possible_edges * (saturation_percent / 100))

    # Zaczynamy od cyklu Hamiltona
    matrix = [[0] * n for _ in range(n)]
    edges = set()

    for i in range(n):
        u = i
        v = (i + 1) % n
        matrix[u][v] = 1
        matrix[v][u] = 1
        edges.add((min(u, v), max(u, v)))

    current_edge_count = len(edges)

    # Dodajemy losowe krawędzie aż osiągniemy nasycenie
    while current_edge_count < target_edge_count:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v:
            a, b = min(u, v), max(u, v)
            if (a, b) not in edges:
                matrix[a][b] = 1
                matrix[b][a] = 1
                edges.add((a, b))
                current_edge_count += 1

    return matrix

def generate_hamiltonian_directed_successors_list(n, saturation_percent):
    max_possible_edges = n * (n - 1)
    target_edge_count = int(max_possible_edges * (saturation_percent / 100))

    successors = [[] for _ in range(n)]
    edges = set()

    # Tworzymy cykl Hamiltona
    for i in range(n):
        u = i
        v = (i + 1) % n
        successors[u].append(v)
        edges.add((u, v))

    current_edge_count = len(edges)

    # Dodajemy losowe krawędzie
    while current_edge_count < target_edge_count:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v and (u, v) not in edges:
            successors[u].append(v)
            edges.add((u, v))
            current_edge_count += 1

    return successors

def generate_undirected_matrix(n, saturation_percent):
    # Tworzymy pustą macierz n x n
    matrix = [[0] * n for _ in range(n)]

    # Generowanie grafu z nasyceniem b%
    for i in range(1, n):  # od 2 do n (Pascalowe 1-indexed => Python 0-indexed)
        for j in range(i):
            if random.randint(0, 99) < saturation_percent:
                matrix[i][j] = 1
                matrix[j][i] = 1  # nieskierowany

    # Modyfikacja grafu, aby zapewnić parzystość wszystkich wierzchołków
    for v in range(n - 1):  # od 0 do n-2 (Pascal: 1 do n-1)
        degree = sum(matrix[v])  # licz stopień (suma jedynek w wierszu)
        if degree % 2 != 0:
            # Znajdź losowy wierzchołek i > v (tak jak i:=Random(n-wierzcholek)+wierzcholek+1)
            candidates = [i for i in range(v + 1, n)]
            if not candidates:
                continue
            i = random.choice(candidates)
            if matrix[i][v] == 1:
                matrix[i][v] = matrix[v][i] = 0
            else:
                matrix[i][v] = matrix[v][i] = 1

    return matrix


def generate_directed_successors_list(n, saturation):
    from random import randint
    successors = {i: [] for i in range(n)}
    max_edges = n * (n - 1)
    target_edges = int(max_edges * saturation)
    edges = set()

    while len(edges) < target_edges:
        u = randint(0, n - 1)
        v = randint(0, n - 1)
        if u != v and (u, v) not in edges:
            successors[u].append(v)
            edges.add((u, v))
    return successors

def plot_time_vs_n(saturation=0.5, n_values=None, repeats=3, save_path="t_vs_n.png"):
    if n_values is None:
        n_values = [10, 20, 30, 40, 50]

    t_euler_undir = []
    t_hamil_undir = []
    t_euler_dir = []
    t_hamil_dir = []

    for n in n_values:

        print(f'[I :: {n}]')
        # NIESKIEROWANY – macierz
        matrix = generate_undirected_matrix(n, saturation)
        t1 = np.mean([measure_time(eulerian_cycle_matrix, matrix) for _ in range(repeats)])
        matrix = generate_hamiltonian_undirected_matrix(n, saturation)
        t2 = np.mean([measure_time(hamiltonian_cycle_matrix, matrix) for _ in range(repeats)])
        t_euler_undir.append(t1)
        t_hamil_undir.append(t2)

        # SKIEROWANY – lista następników
        adjlist = generate_directed_successors_list(n, saturation)
        t3 = np.mean([measure_time(eulerian_cycle_adjlist, adjlist) for _ in range(repeats)])
        adjlist = generate_hamiltonian_directed_successors_list(n, saturation)
        t4 = np.mean([measure_time(hamiltonian_cycle_adjlist, adjlist) for _ in range(repeats)])
        t_euler_dir.append(t3)
        t_hamil_dir.append(t4)
    
    print("[END]")

    # Wykres nieskierowany
    plt.figure()
    plt.plot(n_values, t_euler_undir, label="Euler (macierz)", marker='o')
    plt.plot(n_values, t_hamil_undir, label="Hamilton (macierz)", marker='s')
    plt.title("t = f(n) – graf nieskierowany, s = 50%")
    plt.xlabel("n (liczba wierzchołków)")
    plt.ylabel("t (czas w sekundach)")
    plt.grid(True)
    plt.legend()
    plt.savefig("t_vs_n_undirected.png")

    # Wykres skierowany
    plt.figure()
    plt.plot(n_values, t_euler_dir, label="Euler (lista)", marker='o')
    plt.plot(n_values, t_hamil_dir, label="Hamilton (lista)", marker='s')
    plt.title("t = f(n) – graf skierowany, s = 50%")
    plt.xlabel("n (liczba wierzchołków)")
    plt.ylabel("t (czas w sekundach)")
    plt.grid(True)
    plt.legend()
    plt.savefig("t_vs_n_directed.png")

    print("Zapisano dwa wykresy: t_vs_n_undirected.png i t_vs_n_directed.png")


def main():

    n_vals = [x for x in range(10, 100, 5)]
    density_vals = [x for x in range(10, 100, 10)]

    plot_time_vs_n(0.5, n_vals, repeats=2)


main()
