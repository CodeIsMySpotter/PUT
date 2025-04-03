from Node import *


class BST():

    def __init__(self):
        self.root = None

    def insert(self, keys: list):
        for element in keys:
            if self.root is None:
                self.root = Node(element)
            else:
                self._insert(self.root, element)

    def _insert(self, node: Node, key: int):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def pre_order(self, node=None):
        if node is None:
           self._pre_order(self.root)
        else:
            self._pre_order(node)
        print()

    def _pre_order(self, node: Node):
        if node:
            print(node.key, end =" ")
            self._pre_order(node.left)
            self._pre_order(node.right)

    
    def in_order(self, node=None):
        if node is None:
            self._in_order(self.root)
        else:
            self._in_order(node)
        print()
    
    def _in_order(self, node):
        if node:
            self._in_order(node.left)
            print(node.key, end=" ")
            self._in_order(node.right)


    def find_max(self, node: None):
        print("Szukam maksimum")
        current = node
        while current.right is not None:
            print(f'Wartość: {current.key}')
            current = current.right
        return current

    def find_min(self, node: None):
        print("Szukam minimum")
        current = node
        while current.left is not None:
            print(f'Wartość: {current.key}')
            current = current.left
        return current

    
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)
    
    def delete_multiple(self):
        try:
            n = int(input("Podaj liczbę węzłów do usunięcia: "))
            keys = list(map(int, input(f"Podaj {n} wartości kluczy do usunięcia (oddzielone spacją): ").split()))

            for key in keys:
                print(f"Usuwam: {key}")
                self.delete(key)

        except ValueError:
            print("Błąd: Podaj poprawne liczby!")

    def _delete_recursive(self, node, key):
        if node is None:
            return node  

        if key < node.key:  
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:  
            node.right = self._delete_recursive(node.right, key)
        else:
            
            if node.left is None:
                return node.right  
            elif node.right is None:
                return node.left

            temp = self.find_min(node.right)
            node.key = temp.key  
            node.right = self._delete_recursive(node.right, temp.key)  

        return node
    
    def _delete_post_order_recursive(self, node):
        if node is None:
            return None

        node.left = self._delete_post_order_recursive(node.left)
        node.right = self._delete_post_order_recursive(node.right)

        print(f'Usuwam węzeł: {node.key}')  
        return None 
    

    def balance_DSW(self):
        self._create_vine()
        self._balance_vine()

    def _create_vine(self):
        grandparent = None
        parent = self.root
        while parent is not None:
            if parent.left is not None:
                child = parent.left
                parent.left = child.right
                child.right = parent
                if grandparent is None:
                    self.root = child
                else:
                    grandparent.right = child
                parent = child
            else:
                grandparent = parent
                parent = parent.right

    def _balance_vine(self):
        n = self._count_nodes(self.root)
        m = 2 ** (n.bit_length() - 1) - 1  # 2^floor(log2(n+1)) - 1

        self._compress(n - m)
        while m > 1:
            m //= 2
            self._compress(m)

    def _compress(self, count):
        grandparent = None
        parent = self.root
        for _ in range(count):
            if parent.right is None:
                break
            child = parent.right
            parent.right = child.left
            child.left = parent
            if grandparent is None:
                self.root = child
            else:
                grandparent.right = child
            grandparent = child
            parent = child.right

    def _count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)
   
    