from BST import BST
from Node import Node

class AVL(BST):

    def insert(self, keys):
        self.root = self._insert(keys)
        

    
    def _insert(self, keys):
        if not keys:
            return None
        mid = len(keys) // 2
        node = Node(keys[mid])
        node.left = self._insert(keys[:mid])
        node.right = self._insert(keys[mid + 1:])

        
        return node

    def delete_multiple(self):
        try:
            n = int(input("Podaj liczbę węzłów do usunięcia: "))
            keys = list(map(int, input(f"Podaj {n} wartości kluczy do usunięcia (oddzielone spacją): ").split()))

            for key in keys:
                print(f"Usuwam: {key}")
                self.delete(key)
            self.balance_by_root_deletion()

        except ValueError:
            print("Błąd: Podaj poprawne liczby!")

    
    def delete(self, key):
        self._delete_recursive(self.root, key)
        self.balance_by_root_deletion()

    def _delete_recursive(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            print(f"Usuwam węzeł: {node.key}")
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self.find_min(node.right)
            node.key = temp.key
            node.right = self._delete_recursive(node.right, temp.key)

        

        return node