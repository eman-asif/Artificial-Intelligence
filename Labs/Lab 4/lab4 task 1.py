import heapq

goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


class PuzzleNode:
    def __init__(self, state, parent, move, g_cost, h_cost):
        self.state = state
        self.parent = parent
        self.move = move
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost

    def generate_state(self):
        grid = []
        for i in range(3):
            grid.append(self.state[i][:]) 
        return grid

    def __lt__(self, other):
        return self.f_cost < other.f_cost

    def generate_children(self):
        zeroi, zeroj = self.index_of_zero(self.state)
        children = []

        i, j = self.move_up(zeroi, zeroj)
        if i is not None and j is not None:
            grid = self.generate_state()
            self.swap(grid, zeroi, zeroj, i, j)
            child_node = PuzzleNode(grid, self, 'up', self.g_cost + 1, self.calculate_heuristic(grid))
            children.append(child_node)

        i, j = self.move_down(zeroi, zeroj)
        if i is not None and j is not None:
            grid = self.generate_state()
            self.swap(grid, zeroi, zeroj, i, j)
            child_node = PuzzleNode(grid, self, 'down', self.g_cost + 1, self.calculate_heuristic(grid))
            children.append(child_node)

        i, j = self.move_right(zeroi, zeroj)
        if i is not None and j is not None:
            grid = self.generate_state()
            self.swap(grid, zeroi, zeroj, i, j)
            child_node = PuzzleNode(grid, self, 'right', self.g_cost + 1, self.calculate_heuristic(grid))
            children.append(child_node)

        i, j = self.move_left(zeroi, zeroj)
        if i is not None and j is not None:
            grid = self.generate_state()
            self.swap(grid, zeroi, zeroj, i, j)
            child_node = PuzzleNode(grid, self, 'left', self.g_cost + 1, self.calculate_heuristic(grid))
            children.append(child_node)

        return children

    def index_of_zero(self, start):
        for i in range(3):
            for j in range(3):
                if start[i][j] == 0:
                    return i, j

    def swap(self, grid, a, b, c, d):
        grid[a][b], grid[c][d] = grid[c][d], grid[a][b]

    def move_up(self, zeroi, zeroj):
        i = zeroi - 1
        if i >= 0:
            return i, zeroj
        return None, None

    def move_down(self, zeroi, zeroj):
        i = zeroi + 1
        if i <= 2:
            return i, zeroj
        return None, None

    def move_right(self, zeroi, zeroj):
        j = zeroj + 1
        if j <= 2:
            return zeroi, j
        return None, None

    def move_left(self, zeroi, zeroj):
        j = zeroj - 1
        if j >= 0:
            return zeroi, j
        return None, None

    def calculate_heuristic(self, goal_state):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != goal_state[i][j] and self.state[i][j] != 0:
                    count += 1
        return count


class AStar:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state
        self.open_list = []
        self.closed_list = set()

    def solve(self):
        if not self.is_solvable(self.start_state):
            return None  
        
        start_node = PuzzleNode(self.start_state, None, None, 0, self.calculate_heuristic(self.start_state))
        heapq.heappush(self.open_list, (start_node.f_cost, start_node))

        while self.open_list:
            current_node = heapq.heappop(self.open_list)[1]

            if current_node.state == self.goal_state:
                return self.trace_solution(current_node)

            self.closed_list.add(tuple(tuple(row) for row in current_node.state))

            for child in current_node.generate_children():
                if tuple(tuple(row) for row in child.state) not in self.closed_list:
                    heapq.heappush(self.open_list, (child.f_cost, child))

        return None

    def trace_solution(self, node):
        solution = []
        while node.parent:
            solution.append(node.move)
            node = node.parent
        return solution[::-1]

    def calculate_heuristic(self, state):
        count = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != goal[i][j] and state[i][j] != 0:
                    count += 1
        return count

    def is_solvable(self, state):
        f_s = []
        for row in state:
            for num in row:
                if num != 0:
                    f_s.append(num)

        inv = 0
        for i in range(len(f_s)):
            for j in range(i + 1, len(f_s)):
                if f_s[i] > f_s[j]:
                    inv += 1
        return inv % 2 == 0


def main():
    start = [[1, 2, 3], [4, 5, 6], [0,7,8]]

    test1 = AStar(start, goal)
    solution = test1.solve()
    
    if solution is None:
        print("This puzzle is not solvable.")
    else:
        print("Solution:", solution)
    start = [[1, 2, 3], [4, 5, 6], [8,7,0]]
    test2 = AStar(start, goal)
    solution = test2.solve()
    
    if solution is None:
        print("This puzzle is not solvable.")
    else:
        print("Solution:", solution)


main()
