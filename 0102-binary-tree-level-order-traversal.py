# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # High level approach: Add node's value into levels[level + 1], extend list as needed
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []

        def search(node, level):
            nonlocal levels
            
            if not node:
                return
            
            curr_level = level + 1
            if curr_level == len(levels):
                levels.append([])
            levels[curr_level].append(node.val)

            search(node.left, level + 1)
            search(node.right, level + 1)

        search(root, -1)
        return levels

            
