def findmaxsum(a):
    sum = 0
    max = -9999
    all_neg_flag = 1
    currneg = -99999

    for i in range(len(a)):
        if a[i] >= 0:
            all_neg_flag = 0
        if all_neg_flag == 1:
            if a[i] > currneg:
                currneg = a[i]
        sum = sum + a[i]
        if (sum < 0):
            sum = 0
        if sum > max:
            max = sum


    if all_neg_flag == 1:
        max = currneg

    return max


a = [-1, 3, -8, 7, 50, -1, -1]
print(findmaxsum(a))
