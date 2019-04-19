#similar:No11,No42,No84
class Solution:
    def largestRectangleArea(self, heights ) -> int:
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans
if __name__ == '__main__':
    t = Solution()
    heights = [2,1,5,6,2,3]
    print(t.largestRectangleArea(heights))
