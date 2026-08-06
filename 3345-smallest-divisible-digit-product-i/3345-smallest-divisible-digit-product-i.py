class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
     
        for num in range(n,n+t):
            x = 1
            ans = num
            while num:
                x *= num% 10
                num //= 10
            if x% t == 0:
                return ans
            

