# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    list:List[int]
    def inorder(self,node: Optional[TreeNode])->None:
        if node==None:
            return
        self.inorder(node.left)
        self.list.append(node.val)
        self.inorder(node.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.list=[]
        self.inorder(root)
        return self.list
        