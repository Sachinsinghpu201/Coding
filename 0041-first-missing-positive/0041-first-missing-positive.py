class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        hashmap = {}
        for i in range(1,n+2):
            hashmap[i] = False
        
        for num in nums:
            if num in hashmap:
                hashmap[num] = True
        ans = -1
        for key , value in hashmap.items():
            if value == False:
                ans = key 
                break 
        return ans

        