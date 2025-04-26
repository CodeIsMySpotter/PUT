import sqlite3
import os

class Record():
  def __init__(self, time: int, name: str, type: str = None):
      self.type = type
      self.time = time
      self.name = name

from matplotlib import pyplot as plt
from AVL import AVL
from BST import BST
from generator import Generator
import time as ti
import sys

sys.setrecursionlimit(10**6)


K = [2500, 5000, 7500, 10000, 12500, 15000, 
     17500, 20000, 22500, 25000, 27500, 30000]

def main_test():

  conn = sqlite3.connect('./AIDS/Tree/test.db')
  cursor = conn.cursor()
  cursor.execute('''
      CREATE TABLE IF NOT EXISTS test_results (
          time REAL,
          name TEXT,
          k INTEGER,
          type TEXT
      )
  ''')


  for k in K:
    array = Generator.generate_int(k)
    bst_session(array, cursor, k)


  plot_create(conn, cursor)
  
  conn.commit()
  conn.close()

def bst_session(array: list, cursor, k):
  bst = BST()

  bst_create, bst = test_create_bst(bst, array.copy())
  bst_find_min = test_find_min_bst(bst)
  bst_in_order = test_in_order_bst(bst)
  bst_balance = test_balance_bst(bst)
  print(f"BST: k: {k} {bst_create.time}, {bst_find_min.time}, {bst_in_order.time}, {bst_balance.time}")


  cursor.execute('''
      INSERT INTO test_results (time, name, k, type) VALUES (?, ?, ?, ?)
  ''', (bst_create.time, bst_create.name, k, "bst"))
  cursor.execute('''
      INSERT INTO test_results (time, name, k, type) VALUES (?, ?, ?, ?)
  ''', (bst_find_min.time, bst_find_min.name, k, "bst"))
  cursor.execute('''
      INSERT INTO test_results (time, name, k, type) VALUES (?, ?, ?, ?)
  ''', (bst_in_order.time, bst_in_order.name, k, "bst"))
  cursor.execute('''
      INSERT INTO test_results (time, name, k, type) VALUES (?, ?, ?, ?)
  ''', (bst_balance.time, bst_balance.name, k, "bst"))



def plot_create(conn, cursor):
  cursor.execute('SELECT * FROM test_results WHERE name = "create"')
  rows = cursor.fetchall()
  x = [row[2] for row in rows]
  y = [row[0] for row in rows]

  plt.plot(x, y, label='create')
  plt.xlabel('n')
  plt.ylabel('time (s)')
  plt.title('Create time vs k')
  plt.legend()
  plt.grid(True)
  plt.tight_layout()

  plt.savefig('AIDS/Tree/plots/create_time_vs_k.png')
  plt.close()


# ///////////////////////////////////////////////////////////////

def test_create_bst(tree: BST, k):
  now = ti.time()
  tree.insert(k)
  then = ti.time()
  return Record(then - now, "create", "bst"), tree


def test_find_min_bst(tree: BST):
  now = ti.time()
  tree.find_min()
  then = ti.time()
  return Record(then - now, "find min", "bst")

def test_in_order_bst(tree: BST):
  now = ti.time()
  tree.in_order()
  then = ti.time()
  return Record(then - now, "in order", "bst")

def test_balance_bst(tree: BST):
  now = ti.time()
  tree.balance_by_root_deletion()
  then = ti.time()
  return Record(then - now, "balance", "bst")

# ///////////////////////////////////////////////////////////////

def test_create_avl(tree: AVL, k: list):
  pass

def test_find_min_avl(tree: AVL, k: list):
  pass

def test_in_order_avl(tree: AVL, k: list):
  pass



main_test()
