class Solution:
    #总体注意考虑边界条件
    def longestValidParentheses(self, s: str) -> int:
        maxls = 0
        #dp数组存储以s[i]为结尾的满足要求的子串长度
        dp = [0 for i in range(len(s))]
        for i in range(1, len(s)):
            ##为（时不用考虑
            if s[i] == ')':
                #当找到右括号时，如果前面一个恰好是（，直接dp[i - 2]的长度加2即可
                if s[i - 1] == '(':
                    add = dp[i - 2] if i > 2 else 0
                    dp[i] = add + 2
                #当找到右括号时，如果前面一个不是（即是），此时需要考虑s[i - dp[i - 1] - 1]韦仕是不是左括号，
                # 如果是，那么就能把dp[i - dp[i - 1] - 2]和dp[i-1]长度接起来了，即dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    add = dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0
                    dp[i] = dp[i - 1] + add + 2
                maxls = max(maxls, dp[i])
        return maxls


if __name__ == '__main__':
    t = Solution()
    ratings = ")()())"
    result = t.longestValidParentheses(ratings)
    print(result)
