class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        result = 0
        for i in range(0, len(nums)):
            dp.append(1) ###初始化全为1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] +1)
            result = max(result, dp[i])
        return result


if __name__ == "__main__":
    test = Solution()
    list1 = [10, 9, 2, 5, 3, 7, 101, 18]
    result = test.lengthOfLIS(list1)
    print(str(result))
