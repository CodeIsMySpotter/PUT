
from Sorts import *
from Generator import *
from Matrix import *
import sqlite3
import time
import matplotlib.pyplot as plt

def print_matrix(matrix):
    cut_matrix = [row[1:] for row in matrix[1:]]
    max_width = max(len(str(value)) for row in cut_matrix for value in row)

    for row in cut_matrix:
        print(' '.join(f'{value:>{max_width}}' for value in row))

def measure_time(func, *args):
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    return end - start

def setup_db():
    conn = sqlite3.connect("results.db")
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS timings (
        nodes INTEGER,
        method TEXT,
        matrix_type TEXT,
        duration REAL
    )
    """)
    conn.commit()
    return conn, c

def save_result(cursor, nodes, method, matrix_type, duration):
    cursor.execute("INSERT INTO timings (nodes, method, matrix_type, duration) VALUES (?, ?, ?, ?)",
                   (nodes, method, matrix_type, duration))


def run_tests():
    conn, cursor = setup_db()
    tests = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]

    for n in tests:
        print("generating dag: ", n)
        edges = generate_dag(n)
        print("building adjacency matrix")
        matrix = build_adjacency_matrix(n, edges)
        print("building graph matrix")
        gmatrix = build_graph_matrix(n, edges)

        print("testing: ", n)

        # DFS Sort
        duration = measure_time(dfs_sort_matrix, matrix)
        save_result(cursor, n, "dfs", "matrix", duration)

        duration = measure_time(dfs_sort_gmatrix, gmatrix)
        save_result(cursor, n, "dfs", "gmatrix", duration)

        # Kahn Sort
        duration = measure_time(kahn_sort_matrix, matrix)
        save_result(cursor, n, "kahn", "matrix", duration)

        duration = measure_time(kahn_sort_gmatrix, gmatrix, n)
        save_result(cursor, n, "kahn", "gmatrix", duration)

    conn.commit()
    conn.close()


def plot_results():
    conn = sqlite3.connect("results.db")
    cursor = conn.cursor()
    
    methods = ["dfs", "kahn"]
    matrices = ["matrix", "gmatrix"]

    for matrix in matrices:
        plt.figure()
        for method in methods:
            cursor.execute("""
                SELECT nodes, duration FROM timings
                WHERE method=? AND matrix_type=?
                ORDER BY nodes ASC
            """, (method, matrix))
            data = cursor.fetchall()
            x, y = zip(*data)
            plt.plot(x, y, label=method)

        plt.title(f"Topological Sort Times ({matrix})")
        plt.xlabel("Number of Nodes")
        plt.ylabel("Time (s)")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"sort_{matrix}.png")

    for method in methods:
        plt.figure()
        for matrix in matrices:
            cursor.execute("""
                SELECT nodes, duration FROM timings
                WHERE method=? AND matrix_type=?
                ORDER BY nodes ASC
            """, (method, matrix))
            data = cursor.fetchall()
            x, y = zip(*data)
            plt.plot(x, y, label=matrix)

        plt.title(f"{method.upper()} Comparison: Matrix vs GMatrix")
        plt.xlabel("Number of Nodes")
        plt.ylabel("Time (s)")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"{method}_matrix_comparison.png")

    conn.close()


if __name__ == "__main__":
    run_tests()
    plot_results()
    #edges, n = read_from_file()
    #print_matrix(build_graph_matrix(n, edges))
