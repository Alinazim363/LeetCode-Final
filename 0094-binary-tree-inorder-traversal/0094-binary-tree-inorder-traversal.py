# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
    
        left_values = self.inorderTraversal(root.left)
    
        current_value = [root.val]
    
        right_values = self.inorderTraversal(root.right)
    
        return left_values + current_value + right_values    