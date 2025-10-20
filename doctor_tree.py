class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, child_name, side):
        parent_node = self._find_node(self.root, parent_name)
        if not parent_node:
            print(f"Error: Parent '{parent_name}' not found.")
            return

        new_node = DoctorNode(child_name)

        if side == "left":
            if parent_node.left is None:
                parent_node.left = new_node
            else:
                print(f"Error: Left child already exists for '{parent_name}'.")
        elif side == "right":
            if parent_node.right is None:
                parent_node.right = new_node
            else:
                print(f"Error: Right child already exists for '{parent_name}'.")
        else:
            print("Error: Side must be 'left' or 'right'.")

    def _find_node(self, current, name):
        if current is None:
            return None
        if current.name == name:
            return current
        left_result = self._find_node(current.left, name)
        if left_result:
            return left_result
        return self._find_node(current.right, name)

    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


# Test your DoctorTree and DoctorNode classes here
tree = DoctorTree()
tree.root = DoctorNode("Dr. Croft")
tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Phan", "Dr. Carson", "right")
tree.insert("Dr. Phan", "Dr. Morgan", "left")

print("Preorder Traversal:", tree.preorder(tree.root))
# Expected: ["Dr. Croft", "Dr. Phan", "Dr. Morgan", "Dr. Carson", "Dr. Goldsmith"]

print("Inorder Traversal:", tree.inorder(tree.root))
# Expected: ["Dr. Morgan", "Dr. Phan", "Dr. Carson", "Dr. Croft", "Dr. Goldsmith"]

print("Postorder Traversal:", tree.postorder(tree.root))
# Expected: ["Dr. Morgan", "Dr. Carson", "Dr. Phan", "Dr. Goldsmith", "Dr. Croft"]
