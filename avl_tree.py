class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    # ---------- Utility Functions ----------
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    # ---------- Rotations ----------
    def rightRotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        return x

    def leftRotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    # ---------- Insertion ----------
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # no duplicates

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        # Balance Cases
        if balance > 1 and key < root.left.key:  # LL
            return self.rightRotate(root)
        if balance < -1 and key > root.right.key:  # RR
            return self.leftRotate(root)
        if balance > 1 and key > root.left.key:  # LR
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and key < root.right.key:  # RL
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root

    # ---------- Traversals ----------
    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.key] + self.inorder(root.right)

    def preorder(self, root):
        if not root:
            return []
        return [root.key] + self.preorder(root.left) + self.preorder(root.right)

    def postorder(self, root):
        if not root:
            return []
        return self.postorder(root.left) + self.postorder(root.right) + [root.key]

    # ---------- Vertical Tree Display ----------
    def printTree(self, root, indent="", position="Root"):
        """Display the tree in a top-down, straight vertical format"""
        if root is not None:
            print(f"{indent}[{position}]-- {root.key}")
            indent += "     "  # increase indentation for children
            self.printTree(root.left, indent, "L")
            self.printTree(root.right, indent, "R")


# ---------- Driver Code ----------
if __name__ == "__main__":
    tree = AVLTree()
    root = None

    print("Enter numbers to insert into AVL Tree (space separated):")
    nums = list(map(int, input().split()))

    for num in nums:
        root = tree.insert(root, num)

    # Traversals
    print("\nInorder Traversal   :", tree.inorder(root))
    print("Preorder Traversal  :", tree.preorder(root))
    print("Postorder Traversal :", tree.postorder(root))

    print("\nAVL Tree Structure (Vertical Form):")
    tree.printTree(root)
