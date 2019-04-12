class Solution:
    def intersectionSizeTwo(self, intervals) -> int:
        res = 0
        if len(intervals) == 0:
            return res
        ##排序，先按照右边排，右边相等按照左边倒排
        sort_intervals = sorted(intervals, key=lambda x: (x[1], -x[0]), reverse=False)
        print(sort_intervals)
        left = sort_intervals[0][1] - 1
        right = sort_intervals[0][1]
        res += 2
        for i in range(1, len(sort_intervals)):
            X = sort_intervals[i]
            if left < X[0] and X[0] <= right:
                res += 1
                left = right
                right = X[1]
            elif X[0] > right:
                res += 2
                left = X[1] - 1
                right = X[1]
        return res


t = Solution()
intervals = [[1,5],[4,5],[5,9],[7,9],[9,10]]
print(t.intersectionSizeTwo(intervals))
