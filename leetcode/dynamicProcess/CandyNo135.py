class Solution:
    def candy(self, ratings) -> int:
        ##1.如果当前rate大于pre  ，pre_candy+1
        # 2.如果当前rate等于pre，给1个
        # 3.如果当前rate小于pre，countDown+1，后面处理
        if len(ratings) == 0:
            return 0
        total = 1
        prev = 1
        countDown = 0
        for i in range(1, len(ratings)):
            if ratings[i] >= ratings[i - 1]:
                if countDown > 0:
                    total += int(countDown * (countDown + 1) / 2)
                    if countDown >= prev:
                        total += countDown - prev + 1
                    countDown = 0;
                    prev = 1
                prev = 1 if ratings[i] == ratings[i - 1] else prev + 1
                total += prev
            else:
                countDown += 1

        if countDown > 0:
            total += int(countDown * (countDown + 1) / 2)
            if countDown >= prev:
                total += countDown - prev + 1
        return total


if __name__ == '__main__':
    t = Solution()
    ratings = [1, 0, 2]
    result = t.candy(ratings)
    print(result)
