from typing import List
import heapq

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = {}
        
        def addtoadjlist(a,b,v):
            if a not in adjList: adjList[a] = {(b,v)}
            else: adjList[a].add((b,v))
            if b not in adjList and v != 0: adjList[b] = {(a,1/v)}
            elif v != 0: adjList[b].add((a,1/v))
                
        for (a,b), v in zip(equations, values):
            addtoadjlist(a,b,v)
        
        res = []
        for a,b in queries:
            if a not in adjList or b not in adjList: 
                res.append(-1)
                continue
            if a == b: 
                res.append(1)
                continue
            minHeap = [(1,a)]
            visited = set()
            got = False
            while minHeap:
                v,c = heapq.heappop(minHeap)
                if c in visited: 
                    continue
                if c == b: 
                    res.append(v)
                    got = True
                    break
                visited.add(c)
                addtoadjlist(a,c,v)  # Note: This modifies the graph during traversal
                for nc, nv in adjList[c]:
                    heapq.heappush(minHeap, (v*nv, nc))
            if not got: 
                res.append(-1)
        return res

# Driver Code with one example
def main():
    print("=" * 60)
    print("EVALUATE DIVISION - SINGLE EXAMPLE")
    print("=" * 60)
    
    # Create solution instance
    solution = Solution()
    
    # Example from LeetCode
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    
    print("\nInput:")
    print(f"Equations: {equations}")
    print(f"Values: {values}")
    print(f"Queries: {queries}")
    print("\n" + "-" * 60)
    
    # Run the algorithm
    print("\nProcessing queries:")
    print("-" * 40)
    
    result = solution.cEquation(equations, values, queries)
    
    # Print results with explanations
    print("\nResults:")
    print("-" * 40)
    for i, (query, res) in enumerate(zip(queries, result)):
        a, b = query
        if res == -1:
            print(f"Query {i+1}: {a}/{b} = -1 (Cannot be determined)")
        else:
            print(f"Query {i+1}: {a}/{b} = {res}")
    
    print("\n" + "=" * 60)
    
    # Detailed explanation of each query
    print("\nDetailed Explanation:")
    print("-" * 40)
    
    # Query 1: a/c
    print("1. a / c:")
    print("   Graph: a --2.0--> b --3.0--> c")
    print("   Path: a → b → c")
    print("   Calculation: 2.0 × 3.0 = 6.0")
    
    # Query 2: b/a  
    print("\n2. b / a:")
    print("   Graph: b --0.5--> a (reciprocal of a/b)")
    print("   Path: b → a")
    print("   Calculation: 0.5 = 1/2.0")
    
    # Query 3: a/e
    print("\n3. a / e:")
    print("   'e' is not in the graph")
    print("   Result: -1 (Cannot be determined)")
    
    # Query 4: a/a
    print("\n4. a / a:")
    print("   Any variable divided by itself = 1")
    print("   Result: 1.0")
    
    # Query 5: x/x
    print("\n5. x / x:")
    print("   'x' is not in the graph")
    print("   Result: -1 (Cannot be determined)")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()