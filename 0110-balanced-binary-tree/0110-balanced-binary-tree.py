# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        heights = {}
        stack = [(root, False)]
    
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
        
            if not visited:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
            else:
                left_h = heights.get(node.left, 0)
                right_h = heights.get(node.right, 0)
                if abs(left_h - right_h) > 1:
                    return False
                heights[node] = max(left_h, right_h) + 1
    
        return True