import copy

# Goal state for the 8 puzzle
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]


def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x = (val - 1) // 3
                goal_y = (val - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance


def get_neighbors(state):
    neighbors = []
    x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)

    return neighbors


def hill_climbing(initial_state):
    current_state = initial_state
    current_cost = manhattan_distance(current_state)

    while True:
        neighbors = get_neighbors(current_state)
        neighbor_costs = [(manhattan_distance(state), state) for state in neighbors]
        neighbor_costs.sort(key=lambda x: x[0])

        best_cost, best_state = neighbor_costs[0]

        if best_cost >= current_cost:
            # No improvement
            break

        current_state = best_state
        current_cost = best_cost

    return current_state, current_cost


# Sample initial state (shuffled)
initial = [[1, 2, 3],
           [4, 0, 6],
           [7, 5, 8]]

solution, cost = hill_climbing(initial)

print("Final state:")
for row in solution:
    print(row)
print("Heuristic cost:", cost)

#[[5, 2, 7],
 #     [4, 0, 6],
  #         [3, 1, 8]]