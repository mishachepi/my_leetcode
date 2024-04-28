"""
How tree works
"""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder_traversal(root):
    if root:
        yield from inorder_traversal(root.left)
        yield root.value
        yield from inorder_traversal(root.right)
#         1
#        / \
#       2   3
#      / \
#     4   5

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3)

for value in inorder_traversal(root):
    print(value)
