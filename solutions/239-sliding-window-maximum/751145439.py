from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dq=deque()
        output=[]
        for i in range(len(nums)):
            while dq and nums[i]>nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if (i-dq[0])==k:
                dq.popleft()
            if i>=k-1:
                output.append(nums[dq[0]])
        return output

        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        