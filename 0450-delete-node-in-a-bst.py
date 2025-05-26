# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_min(self, node):
        while node.left:
            node = node.left
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Approach:
        # Find the node to remove 
        # Case 1: No children (set self to null)
        # Case 2: One child (swap with child and delete child)
        # Case 3: Two children (find and swap with minimum in right subtree, call delete on that node)
        if root is None:
            return None
        
        # Find node to remove
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            # Found node

            # Case 1: no children
            if not root.left and not root.right:
                root = None
            # Case 2: one child
            elif not root.left and root.right:
                root = root.right
            elif root.left and not root.right:
                root = root.left
            # Case 2: two children
            else:
                min_node = self.find_min(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)

        return root 