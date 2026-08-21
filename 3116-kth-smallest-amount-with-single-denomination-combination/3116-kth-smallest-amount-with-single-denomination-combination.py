# # class Solution(object):

# #     def findKthSmallest(self, coins, k):
# #         """
# #         :type coins: List[int]
# #         :type k: int
# #         :rtype: int
# #         """

# #         hashmap = {}

       
# #         for val in coins:

# #             hashmap[val] = [-1]
# #             var = 0

# #             for j in range(k):

# #                 var = var + val

# #                 if var not in hashmap[val]:
# #                     hashmap[val].append(var)

# #         arr = []

# #         for val in hashmap:
# #             for x in hashmap[val]:
# #                 if x != -1 and x not in arr:
# #                     arr.append(x)

    
# #         arr.sort()

    
# #         return arr[k - 1]


# class Solution(object):

#     def findKthSmallest(self, coins, k):

#         values = set()

#         for coin in coins:

#             multiple = coin

#             for _ in range(k):
#                 values.add(multiple)
#                 multiple += coin

#         values = sorted(values)

#         return values[k - 1]



from itertools import combinations


class Solution(object):

    def findKthSmallest(self, coins, k):

        coins = list(set(coins))
        n = len(coins)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return (a // gcd(a, b)) * b

        def count(x):

            total = 0

            for r in range(1, n + 1):

                for group in combinations(coins, r):

                    value = 1

                    for coin in group:
                        value = lcm(value, coin)

                        if value > x:
                            break

                    if value > x:
                        continue

                    if r % 2 == 1:
                        total += x // value
                    else:
                        total -= x // value

            return total

        left = 1
        right = min(coins) * k

        while left < right:

            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
        while left < right:

            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left