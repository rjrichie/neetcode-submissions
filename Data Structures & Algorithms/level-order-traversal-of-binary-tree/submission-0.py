# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        result = []

        while queue:
            # iterate over queue
            n = len(queue)
            nest = []
            for i in range(n):
                element = queue.pop(0)
                if not element:
                    continue
                nest.append(element.val)
                queue.append(element.left)
                queue.append(element.right)
            if len(nest) == 0:
                continue
            result.append(nest)
        
        return result