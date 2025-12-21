# https://www.interviewbit.com/problems/subarray-with-given-xor/
# https://youtu.be/lO9R5CaGRPY
'''
Use the concept of Largest subarray with 0 sum.
Keep a dictionary to store the current_perfix_xor(cpx). Suppose the current subarray can be devided 
into 2 parts y and k.

<----cpx---->
[4, 2, 2,  6,  4]
<---y--> <-k->

y ^ k = cpx
take ^ on both side(as k^k = 0)
y = cpx ^ k 

if we got y previously in dictionary then increase the res by that count.
'''
class Solution:
    def solve(self, arr, k):
        freq = {}      # stores prefix_xor frequency
        cpx = 0        # current prefix xor
        res = 0

        for num in arr:
            cpx ^= num

            # case 1: subarray from index 0
            if cpx == k:
                res += 1

            # case 2: subarray from some middle index
            y = cpx ^ k
            if y in freq:
                res += freq[y]

            # store prefix xor
            freq[cpx] = freq.get(cpx, 0) + 1

        return res


# -------------------- DRIVER CODE --------------------
if __name__ == "__main__":
    sol = Solution()

    arr = [4, 2, 2, 6, 4]
    k = 6

    print("Subarrays with XOR =", k)
    print(sol.solve(arr, k))

# Time: O(N)
# Space: O(N)


'''
# Brute Force:
# The brute force solution is to generate all possible subarrays.
# For each generated subarray we get the respective XOR and then check if this XOR is equal to B. 

class Solution:
    def solve(self, arr, k):
        res = 0
        for i in range(len(arr)):
            xor = 0
            for j in range(i, len(arr)):
                xor = xor ^ arr[j]
                if xor == k: res += 1
        
        return res 
# Time Limit Exceeded
# Time: O(N^2)
# Space: O(1)
'''


