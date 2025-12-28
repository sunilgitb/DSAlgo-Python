# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/
# https://youtu.be/I3lnDUIzIG4

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj = defaultdict(list)
        for a, b in roads: adj[a].append(b), adj[b].append(a)
        
        def dfs(node, parent):
            nonlocal res
            passengers = 0
            for child in adj[node]:
                if child != parent:
                    p = dfs(child, node)
                    res += ceil(p / seats)
                    passengers += p
            return passengers + 1
         
        res = 0
        dfs(0, -1)
        return res
    
    
# Time: O(N)
if __name__ == "__main__":
    solution = Solution()
    
    roads = [[0,1],[0,2],[0,3]]
    seats = 5
    print(solution.minimumFuelCost(roads, seats))  # Output: 3
    # Explanation: Each node has 1 representative. Each car can carry all, so each edge contributes 1 fuel unit.

    roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]]
    seats = 2
    print(solution.minimumFuelCost(roads, seats))  # Output: 7
    # Explanation: Calculated using ceil of passengers/seats for each subtree.


'''
from collections import defaultdict

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # Create a dictionary to store the edges in the graph
        graph = defaultdict(list)
        for c1, c2 in roads: graph[c1].append(c2), graph[c2].append(c1)
        
        # Initialize the minimum fuel cost to 0
        minimum_fuel_cost = 0
        # Create a set to store the cities that have been visited
        visited_cities = set()
        
        # Define a helper function to traverse the graph
        def dfs(city):
            nonlocal minimum_fuel_cost
            # If the city has already been visited, return 0
            if city in visited_cities: return 0
            # Mark the city as visited
            visited_cities.add(city)
            # Initialize a variable to store the number of representatives in this city
            representatives = 0
            # Loop through the cities connected to this city
            for connected_city in graph[city]:
                # Recursively call the dfs function to count the number of representatives in the connected city
                connected_city_representatives = dfs(connected_city)
                # Calculate the number of cars needed to transport all the representatives in the connected city
                minimum_fuel_cost += ceil(connected_city_representatives / seats)
                # Add the number of representatives in the connected city to the representatives variable
                representatives += connected_city_representatives
            # Return the number of representatives in this city, plus the representative from this city
            return representatives + 1
        
        # Call the dfs function starting from city 0 (the capital city)
        dfs(0)
        # Return the minimum fuel cost
        return minimum_fuel_cost
    
    
# Time: O(N)

'''
