class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #预处理
        s='#'+'#'.join(s)+'#'

        RL=[0]*len(s)
        MaxRight=0
        pos=0
        MaxLen=0
        final_pos = 0
        for i in range(len(s)):
            if i<MaxRight:
                RL[i]=min(RL[2*pos-i], MaxRight-i)
            else:
                RL[i]=1
            #尝试扩展，注意处理边界
            while i-RL[i]>=0 and i+RL[i]<len(s) and s[i-RL[i]]==s[i+RL[i]]:
                RL[i]+=1
            #更新MaxRight,pos
            if RL[i]+i-1>MaxRight:
                MaxRight=RL[i]+i-1
                pos=i
            #更新最长回文串的长度
            MaxLen=max(MaxLen, RL[i])
        subs = s[pos-MaxLen+1:pos+MaxLen-1]
        return subs.replace('#','')
        #return MaxLen-1

if __name__ == "__main__":
    test = Solution()

    print(test.longestPalindrome('abba'))
