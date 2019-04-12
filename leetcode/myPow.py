class Solution(object):
    def myPow(self, x, n):
        if (x == 0.0): return 0.0
        if (n == 0): return 1.0
        if n < 0:
            x = 1 / x
            n = -n
        mpow = 1.0
        while n:
            if n & 1:
                mpow *= x
            x *= x
            n >>= 1
        return mpow


if __name__ == "__main__":
    test = Solution()

    print(test.myPow(-2.0 , -10))

    a = [1,2,3,4,5]
    print(a.index(max(a)))
