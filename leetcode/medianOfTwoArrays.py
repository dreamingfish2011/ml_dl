class Solution(object):
    def medianOfTwoArrays(self, nums1, nums2):
        oddFlag = 1
        median = 0.0
        an = len(nums1)
        bn = len(nums2)
        i = (int)((an + bn - 1) / 2)
        if (an + bn) % 2 == 0:
            oddFlag = 0
        ai = 0
        bi = 0
        for j in range(i):
            if ai <= an - 1 and (bn == 0 or bi == bn or (bi <= bn -1 and nums1[ai] <= nums2[bi])):
                ai += 1
            else:
                bi += 1
        if oddFlag == 1:
            if ai <= an - 1 and (bn == 0 or bi == bn or (bi <= bn -1 and nums1[ai] <= nums2[bi])):
                median = nums1[ai]
            else:
                median = nums2[bi]
        else:
            result = nums1[ai:ai + 2] + nums2[bi:bi + 2]
            result = sorted(result)
            median = (result[0] + result[1]) / 2
        return median


if __name__ == "__main__":
    test = Solution()
    a1 = [2,2,2,2]
    a2 = [ ]

    print(test.medianOfTwoArrays(a1, a2))
