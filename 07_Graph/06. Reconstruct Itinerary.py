from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        Reconstruct itinerary using Hierholzer's algorithm
        
        Args:
            tickets: List of [from, to] pairs
        
        Returns:
            List of airports in itinerary order
        """
        # Build graph as adjacency list
        graph = defaultdict(list)
        
        # Create a graph for each airport with list of reachable airports
        for src, dst in tickets:
            graph[src].append(dst)
        
        # Sort children in reverse order so we can pop from end (O(1))
        for src in graph:
            graph[src].sort(reverse=True)
        
        print("Graph representation (sorted in reverse order):")
        for airport in sorted(graph.keys()):
            print(f"  {airport}: {graph[airport]}")
        print("-" * 50)
        
        # Hierholzer's algorithm using stack
        stack = ["JFK"]  # Start from JFK
        result = []
        
        print("Starting Hierholzer's algorithm:")
        print("=" * 50)
        
        step = 1
        while stack:
            current = stack[-1]
            print(f"\nStep {step}:")
            print(f"  Current stack: {stack}")
            print(f"  Current airport: {current}")
            
            # If current airport has outgoing flights
            if current in graph and graph[current]:
                next_airport = graph[current].pop()
                stack.append(next_airport)
                print(f"  → Flying from {current} to {next_airport}")
                print(f"  Remaining flights from {current}: {graph[current]}")
            else:
                # Dead end - add to result (this will be in reverse order)
                airport = stack.pop()
                result.append(airport)
                print(f"  ✈️  Dead end at {airport}, adding to result")
                print(f"  Current result (reverse order): {result}")
            
            step += 1
        
        # Reverse the result to get correct order
        final_result = result[::-1]
        
        print("\n" + "=" * 50)
        print(f"Final itinerary (reversed): {final_result}")
        
        return final_result
    
    def findItineraryDFS(self, tickets: List[List[str]]) -> List[str]:
        """
        Alternative DFS recursive implementation
        """
        from collections import defaultdict
        
        # Build graph
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        
        # Sort in reverse for pop()
        for src in graph:
            graph[src].sort(reverse=True)
        
        result = []
        
        def dfs(airport):
            """DFS to find Eulerian path"""
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            result.append(airport)
        
        dfs("JFK")
        return result[::-1]


# Driver Code
def main():
    print("=" * 60)
    print("LEETCODE 332: RECONSTRUCT ITINERARY")
    print("=" * 60)
    
    solution = Solution()
    
    # Example 1: Basic example
    print("\nExample 1:")
    tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    print(f"Tickets: {tickets1}")
    
    result1 = solution.findItinerary(tickets1)
    print(f"\nItinerary: {result1}")
    
    # Example 2: More complex (from LeetCode)
    print("\n" + "=" * 60)
    print("\nExample 2:")
    tickets2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    print(f"Tickets: {tickets2}")
    
    result2 = solution.findItinerary(tickets2)
    print(f"\nItinerary: {result2}")
    
    # Example 3: Multiple destinations from same airport
    print("\n" + "=" * 60)
    print("\nExample 3:")
    tickets3 = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
    print(f"Tickets: {tickets3}")
    
    result3 = solution.findItinerary(tickets3)
    print(f"\nItinerary: {result3}")
    
    # Example 4: Circular trip
    print("\n" + "=" * 60)
    print("\nExample 4:")
    tickets4 = [["JFK", "LAX"], ["LAX", "JFK"], ["JFK", "SFO"], ["SFO", "JFK"]]
    print(f"Tickets: {tickets4}")
    
    result4 = solution.findItinerary(tickets4)
    print(f"\nItinerary: {result4}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()