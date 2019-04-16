from decimal import *
getcontext().prec = 50
class Solution:
    def maxPoints(self, points ) -> int:
        l = len(points)
        m = 0
        for i in range(l):
            dic = {'i': 1}
            same = 0
            for j in range(i+1, l):
                tx, ty = points[j][0], points[j][1]
                if tx == points[i][0] and ty == points[i][1]:
                    same += 1
                    continue
                if points[i][0] == tx:
                    slope = 'i'
                else:
                    slope = Decimal(points[i][1]-ty)  /Decimal(points[i][0]-tx)
                if slope not in dic:
                    dic[slope] = 1
                dic[slope] += 1
            m = max(m, max(dic.values()) + same)
        return m



if __name__ == '__main__':
    t = Solution()
    ratings = [[0,0],[94911151,94911150],[94911152,94911151]]
    result = t.maxPoints(ratings)
    print(result)
