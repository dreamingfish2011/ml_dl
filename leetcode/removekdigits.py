######find next palindrome number after current palindrome number
####删除K个数字
class Solution:
    def removeKdigits(self, num, k):
        stackList = []
        result = ''
        for i in range(len(num)):
            currNum = int(num[i])
            while (len(stackList) != 0 and stackList[
                    len(stackList) - 1] > currNum and k > 0):
                stackList = stackList[:-1]
                k -= 1
            if (currNum != 0 or len(stackList) != 0):
                stackList.append(currNum)
        while (len(stackList) != 0 and k > 0):
            stackList = stackList[:-1]
            k -= 1
        for i in range(len(stackList)):
            result = result + str(stackList[i])
        if not result:
            return "0"
        return "".join(result)


if __name__ == "__main__":
    test = Solution()
    strR = test.removeKdigits("1432219", k=3)
    print(strR)