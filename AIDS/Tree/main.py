import sqlite3

from generator import *
from BST import *
from Node import *



def main():
  BSTTree = BST()
  array = Generator.generate_int(100, 10)

  BSTTree.insert([5, 4, 6, 3, 7, 2, 8, 1, 9])
  BSTTree.pre_order()
  BSTTree.in_order()


main()