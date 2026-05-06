# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root:
            if (root.left and root.left.val >= root.val) or (root.right and root.right.val <= root.val):
                return False
            return self.isValidBST(root.right) and self.isValidBST(root.left)
        return True