class Solution:
    def trap(self, height) -> int:
        if len(height) <=2 :
            return 0
        volumn = 0
        head = 0
        tail = len(height) - 1
        lMax = height[head]
        rMax = height[tail]
        #从两头分别开始查找，哪边小就先处理那边
        #当前位置容量为头最大值-当前值
        while head < tail:
            if height[head] <= height[tail]:
                lMax = max(height[head],lMax)
                volumn +=  lMax - height[head]
                head += 1
            else:
                rMax = max(height[tail],rMax)
                volumn +=  rMax - height[tail]
                tail -= 1
        return volumn


if __name__ == '__main__':
    t = Solution()
    ratings = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = t.trap(ratings)
    print(result)
