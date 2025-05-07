# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
    
        left_values = self.postorderTraversal(root.left)

        right_values = self.postorderTraversal(root.right)

        current_value = [root.val]
    
        return left_values + right_values + current_value