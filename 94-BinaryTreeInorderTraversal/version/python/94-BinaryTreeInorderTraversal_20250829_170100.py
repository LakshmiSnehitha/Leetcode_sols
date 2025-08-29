# Last updated: 8/29/2025, 5:01:00 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)   # Left
            res.append(node.val) # Root
            inorder(node.right)  # Right

        inorder(root)
        return res
