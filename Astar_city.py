import heapq

def a_star(cities, start, goal, heuristics):
    """
    Finds shortest path between cities using A* algorithm
    :param cities: Dictionary {city: [(neighbor, distance), ...]}
    :param start: Starting city
    :param goal: Target city
    :param heuristics: Dictionary {city: estimated_distance_to_goal}
    :return: (path, total_distance) or (None, inf) if no path exists
    """
    # Priority queue: (f_score, city, path, g_score)
    heap = [(heuristics[start], start, [start], 0)]
    visited = set()
    
    while heap:
        f, current, path, g = heapq.heappop(heap)
        
        if current == goal:
            return path, g
        
        if current in visited:
            continue
        visited.add(current)
        
        for neighbor, distance in cities.get(current, []):
            if neighbor not in visited:
                new_g = g + distance
                heapq.heappush(
                    heap,
                    (new_g + heuristics[neighbor],  # f = g + h
                     neighbor,
                     path + [neighbor],
                     new_g)
                )
    
    return None, float('inf')

# Example Usage
if __name__ == "__main__":
    # City connections (your format)
    cities = {
        'A': [('B', 5), ('C', 10)],
        'B': [('A', 5), ('C', 3), ('D', 2)],
        'C': [('A', 10), ('B', 3), ('D', 1), ('E', 7)],
        'D': [('B', 2), ('C', 1), ('E', 2)],
        'E': [('C', 7), ('D', 2)]
    }

    # Heuristic (straight-line distance to 'E')
    heuristics = {
        'A': 10, 'B': 6, 'C': 5, 
        'D': 2, 'E': 0  # Goal has heuristic 0
    }

    start = 'A'
    goal = 'E'
    path, distance = a_star(cities, start, goal, heuristics)
    
    if path:
        print(f"Shortest path from {start} to {goal}:")
        print(" → ".join(path))
        print(f"Total distance: {distance} km")
    else:
        print("No path exists")