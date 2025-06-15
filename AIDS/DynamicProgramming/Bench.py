import time
import matplotlib.pyplot as plt
from algs import *
import random
from mpl_toolkits.mplot3d import Axes3D 
import numpy as np

def generate_knapsack_data(n, max_weight, max_value):
    items = [(random.randint(1, max_weight), random.randint(1, max_value)) for _ in range(n)]
    return items

########################################################################################################################################################
########################################################################################################################################################


def test_time_vs_n(
    greedy_fn,
    brute_fn,
    dynamic_fn,
    n_range=range(2, 10, 2),
    max_weight=15,
    max_value=100,
    fixed_capacity=50,
    save_path='time_vs_n.png'
):
    greedy_times = []
    brute_times = []
    dynamic_times = []
    ns = list(n_range)

    for n in ns:
        items = generate_knapsack_data(n, max_weight, max_value)
        capacity = fixed_capacity

        start = time.perf_counter()
        greedy_fn(items, capacity)
        greedy_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        brute_fn(items, capacity)
        brute_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        dynamic_fn(items, capacity)
        dynamic_times.append(time.perf_counter() - start)

    plt.figure(figsize=(10, 6))
    plt.plot(ns, greedy_times, label='Greedy', marker='o')
    plt.plot(ns, brute_times, label='Brute Force', marker='o')
    plt.plot(ns, dynamic_times, label='Dynamic Programming', marker='o')
    plt.xlabel('Liczba przedmiotów n')
    plt.ylabel('Czas wykonania [s]')
    plt.title(f'Czas działania algorytmów plecakowych w zależności od liczby przedmiotów (pojemność = {fixed_capacity})')
    plt.legend()
    plt.grid(True)
    plt.savefig(save_path)


########################################################################################################################################################
########################################################################################################################################################

def test_time_vs_n_log(
    greedy_fn,
    brute_fn,
    dynamic_fn,
    n_range=range(2, 32, 2),
    max_weight=15,
    max_value=100,
    fixed_capacity=50,
    save_path='time_vs_n_log.png'
):
    greedy_times = []
    brute_times = []
    dynamic_times = []
    ns = list(n_range)

    for n in ns:
        items = generate_knapsack_data(n, max_weight, max_value)
        capacity = fixed_capacity

        start = time.perf_counter()
        greedy_fn(items, capacity)
        greedy_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        brute_fn(items, capacity)
        brute_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        dynamic_fn(items, capacity)
        dynamic_times.append(time.perf_counter() - start)

    plt.figure(figsize=(10, 6))
    plt.plot(ns, greedy_times, label='Greedy', marker='o')
    plt.plot(ns, brute_times, label='Brute Force', marker='o')
    plt.plot(ns, dynamic_times, label='Dynamic Programming', marker='o')
    plt.yscale('log')
    plt.xlabel('Liczba przedmiotów n')
    plt.ylabel('Czas wykonania [s] (skala log)')
    plt.title(f'Czas działania algorytmów plecakowych (logarytmiczna skala, pojemność = {fixed_capacity})')
    plt.legend()
    plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.savefig(save_path)




########################################################################################################################################################
########################################################################################################################################################


def test_time_vs_capacity(
    greedy_fn,
    brute_fn,
    dynamic_fn,
    b_range=range(10, 100, 10),
    n_items=20,
    max_weight=15,
    max_value=100,
    save_path='time_vs_capacity.png'
):
    greedy_times = []
    brute_times = []
    dynamic_times = []
    capacities = list(b_range)

    items = generate_knapsack_data(n_items, max_weight, max_value)

    for b in capacities:
        start = time.perf_counter()
        greedy_fn(items, b)
        greedy_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        brute_fn(items, b)
        brute_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        dynamic_fn(items, b)
        dynamic_times.append(time.perf_counter() - start)

    plt.figure(figsize=(10, 6))
    plt.plot(capacities, greedy_times, label='Greedy', marker='o')
    plt.plot(capacities, brute_times, label='Brute Force', marker='o')
    plt.plot(capacities, dynamic_times, label='Dynamic Programming', marker='o')
    plt.xlabel('Pojemność plecaka b')
    plt.ylabel('Czas wykonania [s]')
    plt.title(f'Czas działania algorytmów plecakowych w zależności od pojemności (n = {n_items})')
    plt.legend()
    plt.grid(True)
    plt.savefig(save_path)


########################################################################################################################################################
########################################################################################################################################################



def test_time_vs_n_and_capacity(
    greedy_fn,
    brute_fn,
    dynamic_fn,
    n_values=range(5, 31, 5),
    capacity_values=range(10, 101, 10),
    max_weight=15,
    max_value=100
):
    # Przygotuj siatkę wyników
    n_list = list(n_values)
    b_list = list(capacity_values)

    greedy_times = np.zeros((len(n_list), len(b_list)))
    brute_times = np.zeros_like(greedy_times)
    dynamic_times = np.zeros_like(greedy_times)

    for i, n in enumerate(n_list):
        for j, b in enumerate(b_list):
            items = generate_knapsack_data(n, max_weight, max_value)

            start = time.perf_counter()
            greedy_fn(items, b)
            greedy_times[i, j] = time.perf_counter() - start

            start = time.perf_counter()
            brute_fn(items, b)
            brute_times[i, j] = time.perf_counter() - start

            start = time.perf_counter()
            dynamic_fn(items, b)
            dynamic_times[i, j] = time.perf_counter() - start

    # Rysuj wykresy 3D
    X, Y = np.meshgrid(b_list, n_list)

    fig = plt.figure(figsize=(18, 5))

    def plot_surface(ax, Z, title):
        surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k')
        ax.set_xlabel('Pojemność plecaka b')
        ax.set_ylabel('Liczba przedmiotów n')
        ax.set_zlabel('Czas [s]')
        ax.set_title(title)
        fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

    ax1 = fig.add_subplot(131, projection='3d')
    plot_surface(ax1, greedy_times, 'Greedy')

    ax2 = fig.add_subplot(132, projection='3d')
    plot_surface(ax2, brute_times, 'Brute Force')

    ax3 = fig.add_subplot(133, projection='3d')
    plot_surface(ax3, dynamic_times, 'Dynamic Programming')

    plt.tight_layout()
    plt.savefig("wykres_czas_vs_n_b.png", dpi=300)

########################################################################################################################################################
########################################################################################################################################################+


nrange = range(2, 30, 2)  # Zakres n do testowania

test_time_vs_n(
    greedy_fn=greedy_knapsack,
    brute_fn=brute_force_knapsack,
    dynamic_fn=dynamic_knapsack,
    n_range=nrange,
    fixed_capacity=50,
    save_path='czas_vs_n.png'
)

test_time_vs_n_log(
    greedy_fn=greedy_knapsack,
    brute_fn=brute_force_knapsack,
    dynamic_fn=dynamic_knapsack,
    n_range=nrange,
    fixed_capacity=50,
    save_path='czas_vs_n_log.png'
)

test_time_vs_capacity(
    greedy_fn=greedy_knapsack,
    brute_fn=brute_force_knapsack,
    dynamic_fn=dynamic_knapsack,
    n_items=20,
    b_range=range(10, 100, 10),
    save_path='czas_vs_pojemnosc.png'
)

test_time_vs_n_and_capacity(
    greedy_fn=greedy_knapsack,
    brute_fn=brute_force_knapsack,
    dynamic_fn=dynamic_knapsack,
    n_values=range(5, 21, 5),
    capacity_values=range(10, 51, 10)
)
