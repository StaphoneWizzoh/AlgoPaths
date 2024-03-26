import config
import heapq
import utilities as helpers
from collections import deque


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def dfs(board, start, goal):
    stack = [start]
    visited = set()
    full_path = []

    while stack:
        current = stack.pop()
        full_path.append(current)
        if current == goal:
            return full_path
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = config.offsets[direction]
            neighbour = (current[0] + row_offset, current[1] + col_offset)
            if helpers.is_legal_pos(board, neighbour) and neighbour not in visited:
                stack.append(neighbour)
                visited.add(neighbour)


def bfs(board, start, goal):
    queue = deque()
    queue.append(start)
    visited = set()
    full_path = []

    while queue:
        current = queue.popleft()
        full_path.append(current)
        if current == goal:
            return full_path
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = config.offsets[direction]
            neighbour = (current[0] + row_offset, current[1] + col_offset)
            if helpers.is_legal_pos(board, neighbour) and neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)


def heuristic(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(board, start_pos, goal_pos):
    pq = PriorityQueue()
    pq.put(start_pos, 0)
    g_values = {}
    g_values[start_pos] = 0
    full_path = []

    while not pq.is_empty():
        current_cell_pos = pq.get()
        full_path.append(current_cell_pos)
        if current_cell_pos == goal_pos:
            return full_path
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = config.offsets[direction]
            neighbour = (current_cell_pos[0] + row_offset, current_cell_pos[1] + col_offset)
            new_cost = g_values[current_cell_pos] + 1  # this would be the edge weight in a weighted graph
            if helpers.is_legal_pos(board, neighbour):
                # this check only applies to weighted graphs
                if neighbour not in g_values or new_cost < g_values[neighbour]:
                    g_values[neighbour] = new_cost
                    f_value = new_cost + heuristic(goal_pos, neighbour)
                    pq.put(neighbour, f_value)


def dijkstra(board, start, goal):
    pq = PriorityQueue()
    pq.put(start, 0)
    g_values = {}
    g_values[start] = 0
    full_path = []

    while not pq.is_empty():
        current_cell_pos = pq.get()
        full_path.append(current_cell_pos)
        if current_cell_pos == goal:
            return full_path
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = config.offsets[direction]
            neighbour = (current_cell_pos[0] + row_offset, current_cell_pos[1] + col_offset)
            new_cost = g_values[current_cell_pos] + 1  # this would be the edge weight in a weighted graph
            if helpers.is_legal_pos(board, neighbour):
                # this check only applies to weighted graphs
                if neighbour not in g_values or new_cost < g_values[neighbour]:
                    g_values[neighbour] = new_cost
                    f_value = new_cost
                    pq.put(neighbour, f_value)


def bellman_ford(board, start, goal):
    distance = {}
    predecessor = {}
    for vertex in board:
        distance[vertex] = float('inf')
        predecessor[vertex] = None
    distance[start] = 0
    full_path = []

    for _ in range(len(board) - 1):
        for u in board:
            for direction in ["up", "right", "down", "left"]:
                row_offset, col_offset = config.offsets[direction]
                v = (u[0] + row_offset, u[1] + col_offset)
                if helpers.is_legal_pos(board, v):
                    weight = 1  # assuming unweighted graph
                    if distance[u] + weight < distance[v]:
                        distance[v] = distance[u] + weight
                        predecessor[v] = u

    # check for negative cycles
    for u in board:
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = config.offsets[direction]
            v = (u[0] + row_offset, u[1] + col_offset)
            if helpers.is_legal_pos(board, v):
                weight = 1  # assuming unweighted graph
                if distance[u] + weight < distance[v]:
                    raise ValueError("Graph contains a negative cycle")

    # construct path
    current = goal
    while current != start:
        full_path.insert(0, current)
        current = predecessor[current]
    full_path.insert(0, start)
    return full_path


def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    next_vertex = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != float('inf'):
                dist[i][j] = graph[i][j]
                next_vertex[i][j] = j

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_vertex[i][j] = next_vertex[i][k]

    # Construct path
    full_path = []
    for i in range(n):
        for j in range(n):
            if i != j and next_vertex[i][j] != -1:
                path = [i]
                while path[-1] != j:
                    path.append(next_vertex[path[-1]][j])
                full_path.append(path)
    return full_path
