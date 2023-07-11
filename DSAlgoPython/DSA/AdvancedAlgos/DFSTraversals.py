class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder_traversal(root):
    if root is None:
        return []

    traversal = [root.val]  # Process the current node (preorder)
    traversal += preorder_traversal(root.left)  # Traverse left subtree
    traversal += preorder_traversal(root.right)  # Traverse right subtree

    return traversal


def inorder_traversal(root):
    if root is None:
        return []

    traversal = inorder_traversal(root.left)  # Traverse left subtree
    traversal.append(root.val)  # Process the current node (inorder)
    traversal += inorder_traversal(root.right)  # Traverse right subtree

    return traversal


def postorder_traversal(root):
    if root is None:
        return []

    traversal = postorder_traversal(root.left)  # Traverse left subtree
    traversal += postorder_traversal(root.right)  # Traverse right subtree
    traversal.append(root.val)  # Process the current node (postorder)

    return traversal

def reverse_postorder_traversal(root):
    traversal = postorder_traversal(root)  # Perform postorder traversal
    traversal.reverse()  # Reverse the postorder traversal

    return traversal

# Creating a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

"""
      1
     / \
    2   3
   / \
  4   5

"""

# Perform traversals
print("Preorder Traversal:", preorder_traversal(root))
print("Inorder Traversal:", inorder_traversal(root))
print("Postorder Traversal:", postorder_traversal(root))
print("Reverse Postorder Traversal gives 1 valid topological sort:", reverse_postorder_traversal(root))