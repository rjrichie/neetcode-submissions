# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root:
            if root.left:
                resultL = self.inorderTraversal(root.left)
                result = resultL + result
            result.append(root.val)
            if root.right:
                resultR = self.inorderTraversal(root.right)
                result = result + resultR
        return result

