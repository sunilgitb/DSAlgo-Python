# https://www.interviewbit.com/problems/distinct-numbers-in-window/

class Solution:
	def dNums(self, A, B):
		dic = {}
		count = 0
		res = []

		for i in range(len(A)):
			if i < B:
				if A[i] not in dic:
					dic[A[i]] = 1
					count += 1
				else:
					dic[A[i]] += 1
			else:
				dic[A[i-B]] -= 1
				if dic[A[i-B]] == 0: count -= 1
				if A[i] not in dic:
					dic[A[i]] = 1
					count += 1
				else:
					if dic[A[i]] == 0:
						dic[A[i]] += 1
						count += 1
					else:
						dic[A[i]] += 1
			
			if i >= B-1: res.append(count)
		
		return res


# Time: O(N)
# Space: O(N)
if __name__ == "__main__":
    solution = Solution()
    
    A = [1, 2, 1, 3, 4, 3]
    B = 3
    print(solution.dNums(A, B))  
    # Output: [2, 3, 3, 2]
    # Explanation: Windows of size 3 are [1,2,1], [2,1,3], [1,3,4], [3,4,3]

    A = [4, 1, 1, 2, 2, 3, 3]
    B = 2
    print(solution.dNums(A, B))  
    # Output: [2, 1, 2, 1, 2, 1]
    # Explanation: Windows of size 2 are [4,1], [1,1], [1,2], [2,2], [2,3], [3,3]
