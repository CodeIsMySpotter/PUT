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


K = [1000, 2000, 3000, 4000]

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
    print(f"Test for k = {k} started")
    array = Generator.generate_int(k)
    bst_session(array.copy(), cursor, conn, k)
    avl_session(array.copy(), cursor, conn, k)
  
  conn.commit()
  

  plot_operation(cursor, "create", "AIDS/Tree/plots/create.png")
  plot_operation(cursor, "find min", "AIDS/Tree/plots/find_min.png")
  plot_operation(cursor, "in order", "AIDS/Tree/plots/in_order.png")
  plot_operation(cursor, "balance", "AIDS/Tree/plots/balance.png")
  
  conn.close()



def plot_operation(cursor, operation_name, output_file):
    cursor.execute('SELECT * FROM test_results WHERE name = ?', (operation_name,))
    rows = cursor.fetchall()

    x_bst = [row[2] for row in rows if row[3] == 'bst']
    y_bst = [row[0] for row in rows if row[3] == 'bst']
    x_avl = [row[2] for row in rows if row[3] == 'avl']
    y_avl = [row[0] for row in rows if row[3] == 'avl']

    plt.plot(x_bst, y_bst, label='BST')
    plt.plot(x_avl, y_avl, label='AVL')

    plt.xlabel('n')
    plt.ylabel('time (s)')
    plt.title(f'{operation_name.capitalize()} time vs k')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(output_file)
    plt.close()

def bst_session(array: list, cursor, conn, k):
  bst = BST()

  bst_create, bst = test_create_bst(bst, array)
  bst_find_min = test_find_min_bst(bst)
  bst_in_order = test_in_order_bst(bst)
  bst_balance = test_balance_bst(bst)
  print(f"BST: k: {k} {bst_create.time}, {bst_find_min.time}, {bst_in_order.time}, {bst_balance.time}")


  cursor.execute('''
      INSERT INTO test_results (time, name, k, type) VALUES (?, ?, ?, ?)
  ''', (bst_create.time, bst_create.name, k, "bst"))
  conn.commit()
  cursor.execute('''
      INSERT INTO test_results (time, name, k, type) VALUES (?, ?, ?, ?)
  ''', (bst_find_min.time, bst_find_min.name, k, "bst"))
  conn.commit()
  cursor.execute('''
      INSERT INTO test_results (time, name, k, type) VALUES (?, ?, ?, ?)
  ''', (bst_in_order.time, bst_in_order.name, k, "bst"))
  conn.commit()
  cursor.execute('''
      INSERT INTO test_results (time, name, k, type) VALUES (?, ?, ?, ?)
  ''', (bst_balance.time, bst_balance.name, k, "bst"))
  conn.commit()




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

def avl_session(array: list, cursor, conn, k):
  avl = AVL()

  avl_create, avl = test_create_avl(avl)
  avl_find_min = test_find_min_avl(avl)
  avl_in_order = test_in_order_avl(avl)
  print(f"AVL: k: {k} {avl_create.time}, {avl_find_min.time}, {avl_in_order.time}")

  cursor.execute('''
      INSERT INTO test_results (time, name, k, type) VALUES (?, ?, ?, ?)
  ''', (avl_create.time, avl_create.name, k, "avl"))
  conn.commit()
  cursor.execute('''
      INSERT INTO test_results (time, name, k, type) VALUES (?, ?, ?, ?)
  ''', (avl_find_min.time, avl_find_min.name, k, "avl"))
  conn.commit()
  cursor.execute('''
      INSERT INTO test_results (time, name, k, type) VALUES (?, ?, ?, ?)
  ''', (avl_in_order.time, avl_in_order.name, k, "avl"))
  conn.commit()


def test_create_avl(tree: AVL, k: list):
  now = ti.time()
  tree.insert(k)
  then = ti.time()
  return Record(then - now, "create", "avl"), tree

def test_find_min_avl(tree: AVL, k: list):
  now = ti.time()
  tree.find_min()
  then = ti.time()
  return Record(then - now, "find min", "avl")

def test_in_order_avl(tree: AVL, k: list):
  now = ti.time()
  tree.in_order()
  then = ti.time()
  return Record(then - now, "in order", "avl")  



main_test()
