######find next palindrome number after current palindrome number
####找到正数回文数的下一个回文数
def findNextPalindrome(a):
    i = len(a)
    overflag = 0
    left_fit = [1]
    right_fit = [1]

    left = int((i - 1) / 2)
    right = int(i / 2)

    for j, k in zip(range(left, -1, -1), range(right, i)):
        if a[j] < 9:
            a[j] = a[j] + max(1, overflag)
            if k != j:
                a[k] = a[k] + max(1, overflag)
            overflag = 0
            break
        else:
            overflag = 1
            a[j] = 0
            a[k] = 0
    if overflag == 1:
        b = left_fit + a[:-1] + right_fit
    else:
        b = a
    return b


b = [1,1]
for i in range(1000):
    print(b)
    b=findNextPalindrome(b)

