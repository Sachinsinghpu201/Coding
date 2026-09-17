class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        pos = {0:-1}
        n = len(arr)
        ans = n+1
        min_l = n
        s = 0

        for i ,x in enumerate(arr):
            s+= x 
            if s - target in  pos:
                j = pos[s-target]
                length = i-j
                ans = min(ans,length+(n if j == -1 else arr[j]))
                min_l = min(min_l,length)
            arr[i] = min_l
            pos[s] = i
        return -1 if ans== n+1 else ans