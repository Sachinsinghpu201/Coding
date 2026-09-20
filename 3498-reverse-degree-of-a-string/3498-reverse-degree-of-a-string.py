class Solution(object):
    def reverseDegree(self, s):
        ans = 0

        for i in range(len(s)):
            ch = s[i]

            value = 123 - ord(ch)

            ans += value * (i + 1)

        return ans