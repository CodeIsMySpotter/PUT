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


    def pre_order(self, key=None):
        if key is None:
            self._in_order(self.root)
        else:
            node = self._find(self.root, key)
            if node:
                self._pre_order(node)
            else:
                print(f"Nie znaleziono węzła o kluczu {key}")
        print()

    def _pre_order(self, node: Node):
        if node:
            print(node.key, end =" ")
            self._pre_order(node.left)
            self._pre_order(node.right)

    
    def in_order(self, key=None):
        if key is None:
            self._in_order(self.root)
        else:
            node = self._find(self.root, key)
            if node:
                self._in_order(node)
            else:
                print(f"Nie znaleziono węzła o kluczu {key}")
        print()
    
    def _in_order(self, node):
        if node:
            self._in_order(node.left)
            print(node.key, end=" ")
            self._in_order(node.right)


    def find_max(self, node=None):
        if node is None:
            node = self.root

        if node is None:
            return None 

        #print("Szukam maksimum")
        current = node
        while current.right is not None:
            #print(f'Wartość: {current.key}')
            current = current.right
        #print(f'Maksimum: {current.key}')
        return current
    
    def _find(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        elif key < node.key:
            return self._find(node.left, key)
        else:
            return self._find(node.right, key)


    def find_min(self, node=None):
        if node is None:
            node = self.root

        if node is None:
            return None 

        #print("Szukam minimum")
        current = node
        while current.left is not None:
            #print(f'Wartość: {current.key}')
            current = current.left
        #print(f'Minimum: {current.key}')
        return current


    
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)
    
    def delete_multiple(self):
        try:
            n = int(input("Podaj liczbę węzłów do usunięcia: "))
            keys = list(map(int, input(f"Podaj {n} wartości kluczy do usunięcia (oddzielone spacją): ").split()))

            for key in keys:
                #print(f"Usuwam: {key}")
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
    
    def delete_tree(self):
        self._delete_post_order_recursive(self.root)
        self.root = None

    def _delete_post_order_recursive(self, node):
        if node is None:
            return None

        node.left = self._delete_post_order_recursive(node.left)
        node.right = self._delete_post_order_recursive(node.right)

        #print(f'Usuwam węzeł: {node.key}')  
        return None 
    
    def balance_by_root_deletion(self):
        keys = []
        self._gather_in_order(self.root, keys)
        self.root = self._delete_post_order_recursive(self.root)
        self.root = self._build_balanced(keys)

    def _gather_in_order(self, node, result):
        if node:
            self._gather_in_order(node.left, result)
            result.append(node.key)
            self._gather_in_order(node.right, result)

    def _build_balanced(self, keys):
        if not keys:
            return None
        mid = len(keys) // 2
        node = Node(keys[mid])
        node.left = self._build_balanced(keys[:mid])
        node.right = self._build_balanced(keys[mid + 1:])
        return node


    def _count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)
   
    