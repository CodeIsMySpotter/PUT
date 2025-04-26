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
        self.root = self.balande_by_rotation(self.root)


    def _delete_recursive(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            #print(f"Usuwam węzeł: {node.key}")
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self.find_min(node.right)
            node.key = temp.key
            node.right = self._delete_recursive(node.right, temp.key)
        
        

        

        return node
    
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def get_height(self, node):
        if not node:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))
    
    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        return y
    
    def rotate_right(self, z): 
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        return y
    
    def balande_by_rotation(self, node):
        if not node:
            return node

        balance = self.get_balance(node)

        if balance > 1:
            if self.get_balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1:
            if self.get_balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node
        