import sqlite3

from generator import *
from BST import *
from Node import *



def main():
  BSTTree = BST()
  array = Generator.generate_int(100, 10)

  BSTTree.insert([10, 20, 30, 40, 50])
  BSTTree.pre_order()
  BSTTree.balance_DSW()
  BSTTree.pre_order()

main()