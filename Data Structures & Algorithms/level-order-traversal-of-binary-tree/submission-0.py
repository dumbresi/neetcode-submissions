# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result:List[List[int]]=[]

        def bfs(node:TreeNode,result:List[List[int]]):
            if node==None:
                return
            q=deque()
            q.append(node)
            while q:
                lis=[]
                for i in range(len(q)):
                    element=q.popleft()
                    lis.append(element.val)
                    if element.left!=None:
                        q.append(element.left)
                    if element.right!=None:
                        q.append(element.right)
                result.append(lis)
        bfs(root,result)
        return result

        