# class Solution(object):
#     def sumAndMultiply(self, s, queries):

#         # n = len(s)

#         # prefix_sum = [-1] * n
#         # prefix_num = [-1] * n

#         # numX = ""
#         # sumX = 0

#         # for i in range(n):
#         #     if s[i] != '0':
#         #         numX += s[i]
#         #         sumX += int(s[i])

#         #         prefix_sum[i] = sumX
#         #         prefix_num[i] = int(numX)

#         # print(prefix_sum)
#         # print(prefix_num)

#         # ans = []

#         # for l, r in queries:
#         #     pass

#         # return ans
#         # ans = []
#         # for i , j in queries:
#         #     subS = str(s)[i:j+1]
#         #     num =""
#         #     sumS = 0
#         #     for ch in subS:
#         #         if ch !="0":
#         #             num+=  ch
#         #             sumS+= int(ch)
#         #     if num== "":
#         #         ans.append(0)
#         #     else:
#         #         ans.append((int(num)*sumS) % (10**9+7))
#         # return ans


from bisect import bisect_left, bisect_right

class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7

        # Store positions and values of non-zero digits
        pos = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        m = len(digits)

        # Prefix sum of non-zero digits
        prefixSum = [0] * (m + 1)
        for i in range(m):
            prefixSum[i + 1] = prefixSum[i] + digits[i]

        # Powers of 10
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # Prefix concatenated number
        prefixNum = [0] * (m + 1)
        for i in range(m):
            prefixNum[i + 1] = (prefixNum[i] * 10 + digits[i]) % MOD

        ans = []

        for l, r in queries:

            # First non-zero digit inside [l, r]
            left = bisect_left(pos, l)

            # Last non-zero digit inside [l, r]
            right = bisect_right(pos, r) - 1

            if left > right:
                ans.append(0)
                continue

            # Sum of digits
            digitSum = prefixSum[right + 1] - prefixSum[left]

            # Number of digits
            length = right - left + 1

            # Concatenated number
            number = (
                prefixNum[right + 1]
                - prefixNum[left] * pow10[length]
            ) % MOD

            ans.append((number * digitSum) % MOD)

        return ans


