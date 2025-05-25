# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Diameter = Left + right

        max_diameter = 0
        def search(node):
            nonlocal max_diameter
            if node is None:
                return 0
            
            left_height = search(node.left)
            right_height = search(node.right)

            this_height = max(left_height, right_height) + 1
            max_diameter = max(max_diameter, left_height + right_height)
            return this_height
        
        search(root)
        return max_diameter