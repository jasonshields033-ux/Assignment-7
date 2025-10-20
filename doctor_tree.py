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

# Design Memo
#The doctor_tree.py file uses a binary tree to represent a doctor reporting structure. This is a good fit because trees are designed to show hierarchical relationships. 
#Each doctor can have up to two direct reports, which makes a binary tree a simple and effective way to model the organization. 
#The DoctorNode class stores each doctor's name and their left and right reports, while the DoctorTree class manages the overall structure and provides methods to insert new doctors and explore the tree.
#The insert method allows new doctors to be added under a specific parent on either the left or right side. It also includes error handling for cases where the parent is not found or the side is invalid. 
#This helps keep the tree organized and prevents mistakes. The traversal methods—preorder, inorder, and postorder—are used to explore the tree in different ways. 
#Preorder is useful for top-down reporting, inorder gives a balanced view, and postorder is helpful when you want to process reports before their supervisor.
#Using a tree for this kind of structure makes it easy to search, update, and display relationships. 
#For example, a hospital administrator could use preorder traversal to see the chain of command starting from the top, or postorder to evaluate performance from the bottom up. 
#The recursive nature of the traversal methods also reinforces important programming concepts.
#This design is a practical way to represent a reporting system. It is flexible, easy to understand, and supports different ways of viewing the data. 
#The implementation also shows how object-oriented programming and recursion can be used to solve real-world problems.
