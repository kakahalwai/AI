import heapq

def a_star(grid, start, goal):
    """
    Solves robot navigation using A* algorithm
    :param grid: 2D list where 0=free path, 1=obstacle
    :param start: (row, col) starting position
    :param goal: (row, col) target position
    :return: path as list of positions or None if no path exists
    """
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Priority queue: (f_score, row, col, path, g_score)
    heap = []
    heapq.heappush(heap, (0, start[0], start[1], [start], 0))
    
    visited = set()
    
    while heap:
        _, row, col, path, g = heapq.heappop(heap)
        
        if (row, col) == goal:
            return path
        
        if (row, col) in visited:
            continue
        visited.add((row, col))
        
        for dr, dc in directions:
            r, c = row + dr, col + dc
            
            # Check boundaries and obstacles
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0:
                new_g = g + 1
                # Manhattan distance heuristic
                h = abs(r - goal[0]) + abs(c - goal[1])
                heapq.heappush(heap, (new_g + h, r, c, path + [(r, c)], new_g))
    
    return None  # No path found

def print_grid(grid, path=None):
    """Print the grid with optional path visualization"""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if path and (i, j) in path:
                print('*', end=' ')
            elif grid[i][j] == 1:
                print('1', end=' ')
            else:
                print('.', end=' ')
        print()

# Example usage
if __name__ == "__main__":
    # 0 = free path, 1 = obstacle
    grid = [
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    
    start = (0, 0)  # Top-left corner
    goal = (4, 4)    # Bottom-right corner
    
    path = a_star(grid, start, goal)
    
    if path:
        print("Path found:")
        print_grid(grid, path)
        print("\nStep-by-step path:")
        for step, (r, c) in enumerate(path):
            print(f"Step {step}: ({r}, {c})")
    else:
        print("No path exists")