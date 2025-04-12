import bubblesort
import insertionsort
import selectionsort
import mergesort
import quicksort
import heapsort

import sys

from generator import *
import sqlite3
import matplotlib.pyplot as plt
import time as ti

sys.setrecursionlimit(10000)


def plot_time_for_each_alg(cursor: sqlite3.Cursor, conn: sqlite3.Connection):


  try:
    cursor.execute("SELECT DISTINCT n FROM records ORDER BY n")
    n_values = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT DISTINCT title FROM records")
    algorithms = [row[0] for row in cursor.fetchall()]
    cursor.execute("SELECT DISTINCT dataType FROM records")
    data_types = [row[0] for row in cursor.fetchall()]


    for title in algorithms:
      plt.figure(figsize=(14, 8))
      for dataType in data_types:
        cursor.execute('''
            SELECT n, AVG(time) as avg_time
            FROM records
            WHERE title = ? AND dataType = ?
            GROUP BY n
            ORDER BY n
        ''', (title, dataType))
        results = cursor.fetchall()

        if results:
          n_vals, times = zip(*results)
          plt.plot(n_vals, times, marker='o', label=f"{title} ({dataType})")

      plt.xlabel('Rozmiar danych (n)')
      plt.ylabel('Średni czas (s)')
      plt.title('Średni czas wykonania dla każdego algorytmu i rodzaju danych')
      plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
      plt.grid(True)
      plt.tight_layout()

      # Zapisanie wykresu
      plt.savefig(f"PUT/Sorting/Plots/time_algs_{title}.png", bbox_inches='tight')
      plt.close()

  except sqlite3.Error as e:
      print(f"Wystąpił błąd podczas dostępu do bazy danych: {e}")
      return []
    
def plot_time_for_each_data(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
  try:
    cursor.execute("SELECT DISTINCT n FROM records ORDER BY n")
    n_values = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT DISTINCT title FROM records")
    algorithms = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT DISTINCT dataType FROM records")
    data_types = [row[0] for row in cursor.fetchall()]

    for data_type in data_types:
        plt.figure(figsize=(14, 8))

        for algorithm in algorithms:
            cursor.execute('''
                SELECT n, AVG(time) as avg_time
                FROM records
                WHERE title = ? AND dataType = ?
                GROUP BY n
                ''', (algorithm, data_type))
            results = cursor.fetchall()

            if results:
                n_vals, times = zip(*results)  # Unzip tylko jeśli są dane
                plt.plot(n_vals, times, marker='o', label=f"{algorithm}")

        plt.xlabel('Rozmiar danych (n)')
        plt.ylabel('Średni czas (s)')
        plt.title(f'Średni czas wykonania dla każdego algorytmu dla danych {data_type}')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
        plt.grid(True)
        plt.tight_layout()

        plt.savefig(f"PUT/Sorting/Plots/time_algs_{data_type}.png", bbox_inches='tight')
        plt.close()

  except sqlite3.Error as e:
    print(f"Wystąpił błąd podczas dostępu do bazy danych: {e}")

def plot_op_for_each_alg(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
  try:
    cursor.execute("SELECT DISTINCT n FROM records ORDER BY n")
    n_values = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT DISTINCT title FROM records")
    algorithms = [row[0] for row in cursor.fetchall()]
    cursor.execute("SELECT DISTINCT dataType FROM records")
    data_types = [row[0] for row in cursor.fetchall()]


    for title in algorithms:
      plt.figure(figsize=(14, 8))
      for dataType in data_types:
        cursor.execute('''
            SELECT n, AVG(op) as avg_op
            FROM records
            WHERE title = ? AND dataType = ?
            GROUP BY n
            ORDER BY n
        ''', (title, dataType))
        results = cursor.fetchall()

        if results:
          n_vals, times = zip(*results)
          plt.plot(n_vals, times, marker='o', label=f"{title} ({dataType})")

      plt.xlabel('Rozmiar danych (n)')
      plt.ylabel('Średni czas (s)')
      plt.title('Średni czas wykonania dla każdego algorytmu i rodzaju danych')
      plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
      plt.grid(True)
      plt.tight_layout()

      # Zapisanie wykresu
      plt.savefig(f"PUT/Sorting/Plots/time_algs_{title}.png", bbox_inches='tight')
      plt.close()

  except sqlite3.Error as e:
    print(f"Wystąpił błąd podczas dostępu do bazy danych: {e}")


def session(cursor:sqlite3.Cursor, conn: sqlite3.Connection):

  for _ in range(5):
    start = ti.time()

    for record in bubblesort.test():
      record.save_to_db(conn, cursor)
  
    for record in insertionsort.test():
      record.save_to_db(conn, cursor)
  
    for record in selectionsort.test():
      record.save_to_db(conn, cursor)
    
    for record in mergesort.test():
      record.save_to_db(conn, cursor)

    for record in quicksort.test():
      record.save_to_db(conn, cursor)
    
    for record in heapsort.test():
      record.save_to_db(conn, cursor)

    end = ti.time() - start
    print("THE SESSION TOOK: ", end)


def main():
  conn = sqlite3.connect("PUT/Sorting/Plots/database.db")
  cursor = conn.cursor()
  #session(cursor, conn)    

  #plot_time_for_each_alg(cursor, conn)
  plot_time_for_each_data(cursor, conn)
  #plot_op_for_each_alg(cursor, conn)
  


  conn.close()

main()





