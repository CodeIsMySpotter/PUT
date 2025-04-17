import sqlite3

from generator import *
from AVL import *
from BST import *
from Node import *



ARRAY = [1, 2, 3, 4, 5, 6, 7,8 ,9]


def main():
  #bst_test()
  avl_test()

def avl_test():
  print("///////// AVL //////////")
  tree = AVL()
  tree.insert(ARRAY.copy())
  tree.pre_order()

  tree.delete_multiple()
  tree.pre_order()
  
  tree.in_order()

def bst_test():
  print("///////// BST //////////")
  tree = BST()
  tree.insert(ARRAY.copy())
  tree.pre_order()

  tree.balance_by_root_deletion()
  tree.pre_order()

  tree.delete_multiple()
  tree.pre_order()

  tree.in_order()
  

main()