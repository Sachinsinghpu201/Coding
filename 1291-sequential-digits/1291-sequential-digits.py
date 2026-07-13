class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        ans = []
        digits = "123456789"
        
        low_len = len(str(low))
        high_len = len(str(high))
        
      
        for length in range(low_len, high_len + 1):
           
            for start in range(10 - length):
                sub_str = digits[start : start + length]
                num = int(sub_str)
                
               
                if low <= num <= high:
                    ans.append(num)
                    
        return ans
