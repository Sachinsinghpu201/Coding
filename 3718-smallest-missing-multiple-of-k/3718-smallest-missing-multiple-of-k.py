class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        num_set = set(nums)
        
       
        i = 1
        while True:
            if i * k not in num_set:
                return i * k
            i += 1
