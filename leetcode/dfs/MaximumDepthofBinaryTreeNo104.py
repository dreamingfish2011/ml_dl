class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    #recursion method
    def maxDepth(self, root: TreeNode) -> int:
        if not root :
            return 0
        else:
            return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
    #bfs method
    def maxDepth(self, root: TreeNode) -> int:
        if not root :
            return 0
        result =0
        q =[]
        q.append(root)
        # q = Queue.Queue()
        # q.put(root)
        while len(q) >0 :
            result +=1
            n = len(q)
            for i in range(0,n) :
                currNode = q[i]
                if currNode.left :
                    q.append(currNode.left)
                if currNode.right :
                    q.append(currNode.right)
            q=q[n:]
        return result
if __name__ == '__main__':
    t = Solution()
    root= TreeNode(3)
    node2= TreeNode(9)
    node3= TreeNode(20)
    node4= TreeNode(15)
    node5= TreeNode(7)
    root.left =node2
    root.right =node3
    node3.left =node4
    node3.right =node5
    result = t.maxDepth(root)
    print(result)