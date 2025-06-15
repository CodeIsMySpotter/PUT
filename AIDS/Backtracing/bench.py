import time
import matplotlib.pyplot as plt
from directed_graph import *
from indirected_graph import *
from euler import *
from hamilton import *
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


import time
import matplotlib.pyplot as plt

def benchmark_cycle_algorithms(
    n_values,
    saturation,
    generate_undirected_graph,
    generate_directed_graph,
    eulerian_cycle_func_undirected,
    eulerian_cycle_func_directed,
    hamiltonian_cycle_func_undirected,
    hamiltonian_cycle_func_directed,
    plot_path="benchmark_plot.png"
):
    euler_times_undirected = []
    hamilton_times_undirected = []
    euler_times_directed = []
    hamilton_times_directed = []

    for n in n_values:
        # Graf nieskierowany
        graph_undirected = generate_undirected_graph(n, saturation)

        start = time.perf_counter()
        eulerian_cycle_func_undirected(graph_undirected)
        euler_times_undirected.append(time.perf_counter() - start)

        start = time.perf_counter()
        hamiltonian_cycle_func_undirected(graph_undirected)
        hamilton_times_undirected.append(time.perf_counter() - start)

        # Graf skierowany
        graph_directed = generate_directed_graph(n, saturation)

        start = time.perf_counter()
        eulerian_cycle_func_directed(edges_to_successors(graph_directed))
        euler_times_directed.append(time.perf_counter() - start)

        start = time.perf_counter()
        hamiltonian_cycle_func_directed(edges_to_successors(graph_directed))
        hamilton_times_directed.append(time.perf_counter() - start)

    # Tworzenie wykresu z subplotami
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Wykres 1: Nieskierowany
    axes[0].plot(n_values, euler_times_undirected, label="Euler (nieskierowany)", marker='o')
    axes[0].plot(n_values, hamilton_times_undirected, label="Hamilton (nieskierowany)", marker='s')
    axes[0].set_title("Graf nieskierowany — czas vs liczba wierzchołków")
    axes[0].set_xlabel("Liczba wierzchołków (n)")
    axes[0].set_ylabel("Czas obliczeń (s)")
    axes[0].legend()
    axes[0].grid(True)

    # Wykres 2: Skierowany
    axes[1].plot(n_values, euler_times_directed, label="Euler (skierowany)", marker='o')
    axes[1].plot(n_values, hamilton_times_directed, label="Hamilton (skierowany)", marker='s')
    axes[1].set_title("Graf skierowany — czas vs liczba wierzchołków")
    axes[1].set_xlabel("Liczba wierzchołków (n)")
    axes[1].set_ylabel("Czas obliczeń (s)")
    axes[1].legend()
    axes[1].grid(True)

    plt.tight_layout()
    plt.savefig(plot_path, dpi=300)
    plt.show()

def test_time_vs_n_for_two_algorithms(
    euler_directed,
    euler_undirected,
    hamilton_directed,
    hamilton_undirected,
    generate_directed_graph,
    generate_undirected_graph,
    n_values=range(10, 101, 10),
    saturation=0.5
):
    alg1_times_directed = []
    alg1_times_undirected = []
    alg2_times_directed = []
    alg2_times_undirected = []

    for n in n_values:
        g_directed = generate_directed_graph(n, saturation)
        g_undirected = generate_undirected_graph(n, saturation)

        start = time.perf_counter()
        euler_directed(edges_to_successors(g_directed))
        alg1_times_directed.append(time.perf_counter() - start)

        start = time.perf_counter()
        euler_undirected(g_undirected)
        alg1_times_undirected.append(time.perf_counter() - start)

        start = time.perf_counter()
        hamilton_directed(edges_to_successors(g_directed))
        alg2_times_directed.append(time.perf_counter() - start)

        start = time.perf_counter()
        hamilton_undirected(g_undirected)
        alg2_times_undirected.append(time.perf_counter() - start)

    plt.figure(figsize=(14, 6))

    plt.subplot(1, 2, 1)
    plt.plot(n_values, alg1_times_directed, label="Skierowany")
    plt.plot(n_values, alg1_times_undirected, label="Nieskierowany")
    plt.title("Algorytm 1 (Euler): czas obliczeń t = f(n)")
    plt.xlabel("Liczba wierzchołków n")
    plt.ylabel("Czas [s]")
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(n_values, alg2_times_directed, label="Skierowany")
    plt.plot(n_values, alg2_times_undirected, label="Nieskierowany")
    plt.title("Algorytm 2 (Hamilton): czas obliczeń t = f(n)")
    plt.xlabel("Liczba wierzchołków n")
    plt.ylabel("Czas [s]")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("czas_vs_n_algorytmy.png", dpi=300)
    plt.show()

def benchmark_vs_saturation(
    saturation_values,
    n_fixed,
    generate_undirected_graph,
    generate_directed_graph,
    eulerian_cycle_func_undirected,
    eulerian_cycle_func_directed,
    hamiltonian_cycle_func_undirected,
    hamiltonian_cycle_func_directed,
    plot_path="czas_vs_saturation.png"
):
    euler_times_undirected = []
    hamilton_times_undirected = []
    euler_times_directed = []
    hamilton_times_directed = []

    for saturation in saturation_values:
        print(saturation)
        # Graf nieskierowany
        graph_undirected = generate_undirected_graph(n_fixed, saturation)

        start = time.perf_counter()
        eulerian_cycle_func_undirected(graph_undirected)
        euler_times_undirected.append(time.perf_counter() - start)

        start = time.perf_counter()
        hamiltonian_cycle_func_undirected(graph_undirected)
        hamilton_times_undirected.append(time.perf_counter() - start)

        # Graf skierowany
        graph_directed = generate_directed_graph(n_fixed, saturation)

        start = time.perf_counter()
        eulerian_cycle_func_directed(edges_to_successors(graph_directed))
        euler_times_directed.append(time.perf_counter() - start)

        start = time.perf_counter()
        hamiltonian_cycle_func_directed(edges_to_successors(graph_directed))
        hamilton_times_directed.append(time.perf_counter() - start)

    # Tworzenie wykresu z subplotami
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Wykres 1: Nieskierowany
    axes[0].plot(saturation_values, euler_times_undirected, label="Euler (nieskierowany)", marker='o')
    axes[0].plot(saturation_values, hamilton_times_undirected, label="Hamilton (nieskierowany)", marker='s')
    axes[0].set_title(f"Graf nieskierowany — czas vs nasycenie (n={n_fixed})")
    axes[0].set_xlabel("Nasycenie (s)")
    axes[0].set_ylabel("Czas obliczeń (s)")
    axes[0].legend()
    axes[0].grid(True)

    # Wykres 2: Skierowany
    axes[1].plot(saturation_values, euler_times_directed, label="Euler (skierowany)", marker='o')
    axes[1].plot(saturation_values, hamilton_times_directed, label="Hamilton (skierowany)", marker='s')
    axes[1].set_title(f"Graf skierowany — czas vs nasycenie (n={n_fixed})")
    axes[1].set_xlabel("Nasycenie (s)")
    axes[1].set_ylabel("Czas obliczeń (s)")
    axes[1].legend()
    axes[1].grid(True)

    plt.tight_layout()
    plt.savefig(plot_path, dpi=300)
    plt.show()

def benchmark_vs_saturation_by_algorithm(
    saturation_values,
    n_fixed,
    generate_undirected_graph,
    generate_directed_graph,
    eulerian_cycle_func_undirected,
    eulerian_cycle_func_directed,
    hamiltonian_cycle_func_undirected,
    hamiltonian_cycle_func_directed,
    plot_path="czas_vs_s_by_algorithm.png"
):
    euler_times_undirected = []
    euler_times_directed = []
    hamilton_times_undirected = []
    hamilton_times_directed = []

    for saturation in saturation_values:
        # Graf nieskierowany
        graph_undirected = generate_undirected_graph(n_fixed, saturation)

        start = time.perf_counter()
        eulerian_cycle_func_undirected(graph_undirected)
        euler_times_undirected.append(time.perf_counter() - start)

        start = time.perf_counter()
        hamiltonian_cycle_func_undirected(graph_undirected)
        hamilton_times_undirected.append(time.perf_counter() - start)

        # Graf skierowany
        graph_directed = generate_directed_graph(n_fixed, saturation)

        start = time.perf_counter()
        eulerian_cycle_func_directed(edges_to_successors(graph_directed))
        euler_times_directed.append(time.perf_counter() - start)

        start = time.perf_counter()
        hamiltonian_cycle_func_directed(edges_to_successors(graph_directed))
        hamilton_times_directed.append(time.perf_counter() - start)

    # Tworzenie wykresów
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Wykres Euler
    axes[0].plot(saturation_values, euler_times_undirected, label="Graf nieskierowany", marker='o')
    axes[0].plot(saturation_values, euler_times_directed, label="Graf skierowany", marker='s')
    axes[0].set_title(f"Algorytm Eulera — czas vs nasycenie (n={n_fixed})")
    axes[0].set_xlabel("Nasycenie (s)")
    axes[0].set_ylabel("Czas obliczeń (s)")
    axes[0].legend()
    axes[0].grid(True)

    # Wykres Hamilton
    axes[1].plot(saturation_values, hamilton_times_undirected, label="Graf nieskierowany", marker='o')
    axes[1].plot(saturation_values, hamilton_times_directed, label="Graf skierowany", marker='s')
    axes[1].set_title(f"Algorytm Hamiltona — czas vs nasycenie (n={n_fixed})")
    axes[1].set_xlabel("Nasycenie (s)")
    axes[1].set_ylabel("Czas obliczeń (s)")
    axes[1].legend()
    axes[1].grid(True)

    plt.tight_layout()
    plt.savefig(plot_path, dpi=300)
    plt.show()

def benchmark_surface_plot_directed(
    n_values,
    saturation_values,
    generate_directed_graph,
    eulerian_cycle_func_directed,
    hamiltonian_cycle_func_directed,
    euler_plot_path="surface_euler_directed.png",
    hamilton_plot_path="surface_hamilton_directed.png"
):
    
    euler_times = np.zeros((len(n_values), len(saturation_values)))
    hamilton_times = np.zeros((len(n_values), len(saturation_values)))

    for i, n in enumerate(n_values):
        for j, s in enumerate(saturation_values):
            graph = generate_directed_graph(n, s)
            successors = edges_to_successors(graph)

            # Euler
            start = time.perf_counter()
            eulerian_cycle_func_directed(successors)
            euler_times[i][j] = time.perf_counter() - start

            # Hamilton
            start = time.perf_counter()
            hamiltonian_cycle_func_directed(successors)
            hamilton_times[i][j] = time.perf_counter() - start

    X, Y = np.meshgrid(saturation_values, n_values)

    # Wykres Eulera
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, euler_times, cmap='viridis')
    ax.set_title("Czas działania algorytmu Eulera (graf skierowany)")
    ax.set_xlabel("Nasycenie (s)")
    ax.set_ylabel("Liczba wierzchołków (n)")
    ax.set_zlabel("Czas obliczeń (s)")
    plt.tight_layout()
    plt.savefig(euler_plot_path, dpi=300)
    plt.show()

    # Wykres Hamiltona
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, hamilton_times, cmap='plasma')
    ax.set_title("Czas działania algorytmu Hamiltona (graf skierowany)")
    ax.set_xlabel("Nasycenie (s)")
    ax.set_ylabel("Liczba wierzchołków (n)")
    ax.set_zlabel("Czas obliczeń (s)")
    plt.tight_layout()
    plt.savefig(hamilton_plot_path, dpi=300)
    plt.show()

def benchmark_surface_plot_undirected(
    n_values,
    saturation_values,
    generate_undirected_graph,
    eulerian_cycle_func_undirected,
    hamiltonian_cycle_func_undirected,
    euler_plot_path="surface_euler_undirected.png",
    hamilton_plot_path="surface_hamilton_undirected.png"
):
    euler_times = np.zeros((len(n_values), len(saturation_values)))
    hamilton_times = np.zeros((len(n_values), len(saturation_values)))

    for i, n in enumerate(n_values):
        for j, s in enumerate(saturation_values):
            graph = generate_undirected_graph(n, s)

            # Euler
            start = time.perf_counter()
            eulerian_cycle_func_undirected(graph)
            euler_times[i][j] = time.perf_counter() - start

            # Hamilton
            start = time.perf_counter()
            hamiltonian_cycle_func_undirected(graph)
            hamilton_times[i][j] = time.perf_counter() - start

    X, Y = np.meshgrid(saturation_values, n_values)

    # Wykres Eulera
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, euler_times, cmap='viridis')
    ax.set_title("Czas działania algorytmu Eulera (graf nieskierowany)")
    ax.set_xlabel("Nasycenie (s)")
    ax.set_ylabel("Liczba wierzchołków (n)")
    ax.set_zlabel("Czas obliczeń (s)")
    plt.tight_layout()
    plt.savefig(euler_plot_path, dpi=300)
    plt.show()

    # Wykres Hamiltona
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, hamilton_times, cmap='plasma')
    ax.set_title("Czas działania algorytmu Hamiltona (graf nieskierowany)")
    ax.set_xlabel("Nasycenie (s)")
    ax.set_ylabel("Liczba wierzchołków (n)")
    ax.set_zlabel("Czas obliczeń (s)")
    plt.tight_layout()
    plt.savefig(hamilton_plot_path, dpi=300)
    plt.show()

import sys
sys.setrecursionlimit(10**9)  # Zwiększenie limitu rekurencji

n_values =  range(6, 16, 2)  # liczba wierzchołków do testów 
saturation = 0.5

"""benchmark_cycle_algorithms(
    n_values=n_values,
    saturation=0.5,
    generate_undirected_graph=generate_undirected_graph,
    generate_directed_graph=generate_directed_graph,
    eulerian_cycle_func_undirected=find_euler_cycle_undirected,
    eulerian_cycle_func_directed=find_euler_cycle_directed,
    hamiltonian_cycle_func_undirected=find_hamilton_cycle_undirected,
    hamiltonian_cycle_func_directed=find_hamilton_cycle_directed,
    plot_path="czas_vs_n.png"
)



test_time_vs_n_for_two_algorithms(
    euler_directed=find_euler_cycle_directed,
    euler_undirected=find_euler_cycle_undirected,
    hamilton_directed=find_hamilton_cycle_directed,
    hamilton_undirected=find_hamilton_cycle_undirected,
    generate_directed_graph=generate_directed_graph,
    generate_undirected_graph=generate_undirected_graph,
    n_values=n_values,  
    saturation=0.5                
)

benchmark_vs_saturation(
    saturation_values=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    n_fixed=15,
    generate_undirected_graph=generate_undirected_graph,
    generate_directed_graph=generate_directed_graph,
    eulerian_cycle_func_undirected=find_euler_cycle_undirected,
    eulerian_cycle_func_directed=find_euler_cycle_directed,
    hamiltonian_cycle_func_undirected=find_hamilton_cycle_undirected,
    hamiltonian_cycle_func_directed=find_hamilton_cycle_directed,
    plot_path="czas_vs_s.png"
)

benchmark_vs_saturation_by_algorithm(
    saturation_values=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    n_fixed=15,
    generate_undirected_graph=generate_undirected_graph,
    generate_directed_graph=generate_directed_graph,
    eulerian_cycle_func_undirected=find_euler_cycle_undirected,
    eulerian_cycle_func_directed=find_euler_cycle_directed,
    hamiltonian_cycle_func_undirected=find_hamilton_cycle_undirected,
    hamiltonian_cycle_func_directed=find_hamilton_cycle_directed,
    plot_path="czas_vs_s_algorytm.png"
)

benchmark_surface_plot_directed(
    n_values=n_values,
    saturation_values=[0.2, 0.4, 0.6, 0.8, 1.0],
    generate_directed_graph=generate_directed_graph,
    eulerian_cycle_func_directed=find_euler_cycle_directed,
    hamiltonian_cycle_func_directed=find_hamilton_cycle_directed
)"""


benchmark_surface_plot_undirected(
    n_values=n_values,
    saturation_values=[0.2, 0.4, 0.6, 0.8, 1.0],
    generate_undirected_graph=generate_undirected_graph,
    eulerian_cycle_func_undirected=find_euler_cycle_undirected,
    hamiltonian_cycle_func_undirected=find_hamilton_cycle_undirected
)