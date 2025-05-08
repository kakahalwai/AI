import heapq

class CityGraph:
    def __init__(self):
        self.graph = {}         # city -> [(neighbor, distance)]
        self.heuristic = {}     # city -> estimated distance to goal

    def add_edge(self, city1, city2, distance):
        self.graph.setdefault(city1, []).append((city2, distance))
        self.graph.setdefault(city2, []).append((city1, distance))

    def set_heuristic(self, city, value):
        self.heuristic[city] = value

    def best_first_search(self, start, goal):
        visited = set()
        # (heuristic, current_city, path, path_cost)
        heap = [(self.heuristic.get(start, float('inf')), start, [start], 0)]

        while heap:
            _, current, path, cost = heapq.heappop(heap)

            if current == goal:
                return path, cost

            if current in visited:
                continue
            visited.add(current)

            for neighbor, distance in self.graph.get(current, []):
                if neighbor not in visited:
                    new_cost = cost + distance
                    heapq.heappush(
                        heap, 
                        (self.heuristic.get(neighbor, float('inf')),
                         neighbor,
                         path + [neighbor],
                         new_cost)
                    )

        return None, float('inf')  # No path found

# -------------------------------------
# Example Usage
# -------------------------------------
if __name__ == "__main__":
    graph = CityGraph()

    # Define city connections
    graph.add_edge("A", "B", 5)
    graph.add_edge("A", "C", 10)
    graph.add_edge("B", "D", 3)
    graph.add_edge("C", "D", 2)
    graph.add_edge("D", "E", 4)
    graph.add_edge("B", "E", 9)

    # Set heuristic values (straight-line estimates)
    graph.set_heuristic("A", 10)
    graph.set_heuristic("B", 6)
    graph.set_heuristic("C", 5)
    graph.set_heuristic("D", 2)
    graph.set_heuristic("E", 0)

    # Find path from A to E
    path, total_distance = graph.best_first_search("A", "E")

    if path:
        print("Best-First Search path:")
        print(" → ".join(path))
        print(f"Total distance: {total_distance} km")
    else:
        print("No path found")