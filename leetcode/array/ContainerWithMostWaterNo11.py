#similar:No11,No42,No84
class Solution:
    def maxArea(self, height ) -> int:
        maxV =0
        left = 0
        right = len(height) -1
        while left < right :
            maxV = max(maxV,(right -left)*min(height[left],height[right]))
            if height[left] <= height[right] :
                left += 1
            else :
                right -= 1
        return maxV
if __name__ == '__main__':
    t = Solution()
    heights = [2,1,5,6,2,3]
    print(t.maxArea(heights))