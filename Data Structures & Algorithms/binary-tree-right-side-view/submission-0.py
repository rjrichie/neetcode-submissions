# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS -> track height
        # -> get the most right node of each level
        queue = [root]
        cam = []
        while queue:
            n = len(queue)
            for i in range(n):
                el = queue.pop(0)
                if i == n - 1:
                    cam.append(el.val)
                
                if el.left: queue.append(el.left)
                if el.right: queue.append(el.right)
        return cam