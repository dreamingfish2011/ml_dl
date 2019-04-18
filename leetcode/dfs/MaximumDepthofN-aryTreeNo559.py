# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    #recursion method
    def maxDepthByR(self, root: 'Node') -> int:
        if root is None:
            return 0
        if root.children is None or root.children == []:
            return 1
        return max(map(self.maxDepth, root.children)) + 1
    #bfs method
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        result = 0
        q = []
        q.append(root)
        # q = Queue.Queue()
        # q.put(root)
        while len(q) > 0:
            result += 1
            n = len(q)
            for i in range(0, n):
                currNode = q[i]
                for child in currNode.children :
                    q.append(child)
            q = q[n:]
        return result


if __name__ == '__main__':
    t = Solution()
    root = Node(3, [])
    node2 = Node(9, [])
    node3 = Node(20, [])
    node4 = Node(15, [])
    node5 = Node(7, [])
    node6 = Node(6, [])
    root.children = [node2, node3, node4]
    node2.children = [node5, node6]
    result = t.maxDepth(root)
    print(result)
