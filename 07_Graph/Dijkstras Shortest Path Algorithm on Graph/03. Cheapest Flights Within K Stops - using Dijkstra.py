from typing import List
import heapq
import math

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Make graph
        adj_list = {i: [] for i in range(n)}
        for frm, to, price in flights:
            adj_list[frm].append((to, price))
        
        # We need to track both cost and stops for each node
        # best_visited[node][stops] = min_cost to reach node with exactly 'stops' stops
        # But since k can be up to n, we use a dictionary approach
        
        # Store minimum cost to reach each node with given number of stops
        min_cost = [math.inf] * n
        stops_count = [math.inf] * n
        
        # Priority queue: (cost, stops, node)
        heap = [(0, -1, src)]  # -1 stops because source doesn't count as a stop
        
        while heap:
            cost, stops, node = heapq.heappop(heap)
            
            # If we've already found a path to this node with fewer or equal stops 
            # and lower or equal cost, skip
            if stops > k:
                continue
                
            # If we've already found a better or equal path (lower cost with same or fewer stops)
            if cost > min_cost[node] and stops >= stops_count[node]:
                continue
            
            # Update the best known cost and stops for this node
            if cost < min_cost[node]:
                min_cost[node] = cost
                stops_count[node] = stops
            
            # If we reached destination, we can't necessarily return immediately
            # because we might find a cheaper path with more stops
            if node == dst:
                continue
            
            # Explore neighbors
            for neighbor, price in adj_list[node]:
                new_cost = cost + price
                new_stops = stops + 1
                
                # Only push if new_stops <= k and new_cost is promising
                if new_stops <= k + 1:  # k stops means k+1 edges max
                    heapq.heappush(heap, (new_cost, new_stops, neighbor))
        
        return min_cost[dst] if min_cost[dst] < math.inf else -1


# Driver code with example
if __name__ == "__main__":
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    sol = Solution()
    print(sol.findCheapestPrice(n, flights, src, dst, k))  # Output: 200
    
    # Additional test case
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    src = 0
    dst = 3
    k = 1
    print(sol.findCheapestPrice(n, flights, src, dst, k))  # Output: 700