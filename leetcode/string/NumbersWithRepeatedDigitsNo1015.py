# given number n, see whether n has repeated number
#思路是先统计不含重复数字的个数，再用N减去就得到重复的个数了
def has_repeated(n):
    str_n = str(n)
    #set("20")={'0','2'}
    return len(set(str_n)) != len(str_n)

def permutation(n, k):
    prod = 1
    for i in range(k):
        prod *= (n-i)
    return prod

# calculate number of non-repeated n-digit numbers
# note: the n-digit number can't start with 0
# i.e: n_digit_no_repeat(2) calculates the non-repeated
#   numbers in range [10, 99] (inclusive)
def n_digit_no_repeat(n):
    if n == 1:
        return 9
    else:
        return  9 * permutation(9, n-1)

class Solution(object):
    def numDupDigitsAtMostN(self, N):
        """
        :type N: int
        :rtype: int
        """
        N_str = str(N)
        n_digit = len(N_str)
        digits = list(map(int, N_str))
        result = N - 1
        prefix = 0
        for i in range(1, n_digit):
            result -= n_digit_no_repeat(i)
        for i in range(n_digit):
            # when we fix the most significant digit, it 
            # can't be zero
            start = 0 if i else 1
            for j in range(start, digits[i]):
                if has_repeated(prefix * 10 + j):
                    continue
                if i != n_digit-1:
                    result -= permutation(10-i-1, n_digit-1-i)
                else:
                    # optmized from `result -= has_repeated(prefix*10+j)`
                    result -= 1
            prefix = prefix*10 + digits[i]
        return result + has_repeated(N)
t=Solution()
num=t.numDupDigitsAtMostN(1234)
print(num)