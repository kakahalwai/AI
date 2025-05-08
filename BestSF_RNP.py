import heapq

def best_first_search(grid, start, goal):
    """
    Solves robot navigation using Best-First Search with Manhattan distance heuristic
    :param grid: 2D list representing the map (0 = free, 1 = obstacle)
    :param start: (row, col) starting position
    :param goal: (row, col) target position
    :return: path as list of positions or None if no path exists
    """
    # Directions: up, down, left, right (and optionally diagonals)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Priority queue: (heuristic, row, col, path)
    heap = []
    heapq.heappush(heap, (0, start[0], start[1], [start]))
    
    visited = set()
    visited.add(start)
    
    while heap:
        _, row, col, path = heapq.heappop(heap)
        
        # Check if current position is the goal
        if (row, col) == goal:
            return path
        
        # Explore neighbors
        for dr, dc in directions:
            r, c = row + dr, col + dc
            
            # Check boundaries and obstacles
            if (0 <= r < len(grid) and 0 <= c < len(grid[0]) 
                and grid[r][c] == 0 and (r, c) not in visited):
                
                # Calculate Manhattan distance heuristic
                heuristic = abs(r - goal[0]) + abs(c - goal[1])
                
                heapq.heappush(heap, (heuristic, r, c, path + [(r, c)]))
                visited.add((r, c))
    
    return None  # No path found

# Example usage:
if __name__ == "__main__":
    # 0 = free path, 1 = obstacle
    grid = [
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    
    start = (0, 0)  # Top-left corner
    goal = (4, 4)    # Bottom-right corner
    
    path = best_first_search(grid, start, goal)
    
    if path:
        print("Path found:")
        for step in path:
            print(step)
    else:
        print("No path exists")