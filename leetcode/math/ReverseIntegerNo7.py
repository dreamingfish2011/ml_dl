import sys
class Solution:
    def reverse(self, x: int) -> int:
        flag =-1 if x <0 else 1
        val = 0
        while 1:
            val = int(val * 10 + abs(x) % 10)
            x = int(x/10)
            if not x :
                break
        if (val > sys.maxsize or val <= -sys.maxsize):
            val =0
        return flag*val

if __name__ == '__main__':
    t = Solution()
    ratings =-123
    result = t.reverse(ratings)
    print(result)