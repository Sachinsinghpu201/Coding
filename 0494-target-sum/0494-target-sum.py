class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = {}

        def dfs(idx,currSum):
            
            if idx == len(nums):
                if currSum == target:
                    return 1
                else:
                    return 0 
            if (idx,currSum) in memo:
                return memo[idx,currSum]
                
                
            
            add = dfs(idx+1,currSum+nums[idx])
            subtract = dfs(idx+1,currSum-nums[idx])
            memo[(idx,currSum )] = add+subtract

            return memo[(idx,currSum)]
        return dfs(0,0)

        dfs(0,0)
        return self.ans


        