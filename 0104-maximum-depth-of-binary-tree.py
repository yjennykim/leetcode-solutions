# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            curr_height = max(left_height, right_height) + 1

            return curr_height
        
        return dfs(root)