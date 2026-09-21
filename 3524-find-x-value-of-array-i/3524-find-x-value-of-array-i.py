class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dp = [0]*k
        result = [0]*k 
        for num in nums:
            new_dp = [0]*k
            new_dp[num%k] +=1
            for r in range(k):
                if dp[r]>0:
                    new_r = (r*num)%k
                    new_dp [new_r] += dp [r]
            dp = new_dp
            for r in range(k):
                result[r] += dp[r]
        return result