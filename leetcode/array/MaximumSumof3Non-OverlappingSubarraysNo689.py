class Solution:
    #leetcode原题求3*k最大
    ##假设求 4*k最大
    def maxSumOfThreeSubarrays(self, nums, k: int):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Best single, double, and triple sequence found so far
        bestSeq = 0
        bestSeq2 = [0, k]
        bestSeq3 = [0, k, k * 2]
        bestSeq4 = [0, k, k * 2,k*3]
        # Sums of each window
        win1sum = sum(nums[0:k])
        win2sum = sum(nums[k:k * 2])
        win3sum = sum(nums[k * 2:k * 3])
        win4sum = sum(nums[k * 3:k * 4])

        # Sums of combined best windows
        bestsum1 = win1sum
        bestsum2 = win1sum + win2sum
        bestsum3 = win1sum + win2sum + win3sum
        bestsum4 = win1sum + win2sum + win3sum + win4sum

        # Current window positions
        seqIndex = 1
        twoSeqIndex = k + 1
        threeSeqIndex = k * 2 + 1
        fourSeqIndex = k * 3 + 1
        while fourSeqIndex <= len(nums) - k:
            # Update the three sliding windows
            win1sum = win1sum - nums[seqIndex - 1] + nums[seqIndex + k - 1]
            win2sum = win2sum - nums[twoSeqIndex - 1] + nums[twoSeqIndex + k - 1]
            win3sum = win3sum - nums[threeSeqIndex - 1] + nums[threeSeqIndex + k - 1]
            win4sum = win4sum - nums[fourSeqIndex - 1] + nums[fourSeqIndex + k - 1]

            # Update best single window
            if win1sum > bestsum1:
                bestSeq = seqIndex
                bestsum1 = win1sum

            # Update best two windows
            if win2sum + bestsum1 > bestsum2:
                bestSeq2 = [bestSeq, twoSeqIndex]
                bestsum2 = win2sum + bestsum1

            # Update best three windows
            if win3sum + bestsum2 > bestsum3:
                bestSeq3 = bestSeq2 + [threeSeqIndex]
                bestsum3 = win3sum + bestsum2

            # Update best four windows
            if win4sum + bestsum3 > bestsum4:
                bestSeq4 = bestSeq3 + [fourSeqIndex]
                bestsum4 = win4sum + bestsum3

            # Update the current positions
            seqIndex += 1
            twoSeqIndex += 1
            threeSeqIndex += 1
            fourSeqIndex += 1
        return bestSeq4


if __name__ == '__main__':
    t = Solution()
    nums = [1, 2, 1, 2, 6, 7, 5, 1]
    k = 2
    print(t.maxSumOfThreeSubarrays(nums, k))
