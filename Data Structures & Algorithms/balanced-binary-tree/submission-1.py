# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.right),height(root.left))

        if root:
            right_height = height(root.right)
            left_height = height(root.left)
            if abs(right_height-left_height) > 1:
                return False
            return Solution.isBalanced(self, root.right) and Solution.isBalanced(self, root.left)
        return True
        