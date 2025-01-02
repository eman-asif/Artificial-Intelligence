from queue import PriorityQueue
import heapq
goal = [[1,2,3],[4,5,6],[7,8,0]]
class Node: 
    def __init__(self, state, parent, move, h_cost): 
# Initialize node with state, parent, move, and h_cost
        self.state = state
        self.parent = parent
        self.move = move
        self.h = h_cost
    def generate_state(self):
        grid = []
        for i in range(3):
            grid.append(self.state[i][:]) 
        return grid
    def generate_children(self): 
# Generate possible child nodes by moving in 4 directions left, right) 
        zeroi, zeroj = self.index_of_zero(self.state)
        children = []

        i, j = self.move_up(zeroi, zeroj)
        if i is not None and j is not None:
            grid = self.generate_state()
            self.swap(grid, zeroi, zeroj, i, j)
            child_node = Node(grid, self, 'up', self.calculate_heuristic(grid))
            children.append(child_node)

        i, j = self.move_down(zeroi, zeroj)
        if i is not None and j is not None:
            grid = self.generate_state()
            self.swap(grid, zeroi, zeroj, i, j)
            child_node = Node(grid, self, 'down', self.calculate_heuristic(grid))
            children.append(child_node)

        i, j = self.move_right(zeroi, zeroj)
        if i is not None and j is not None:
            grid = self.generate_state()
            self.swap(grid, zeroi, zeroj, i, j)
            child_node = Node(grid, self, 'right',self.calculate_heuristic(grid))
            children.append(child_node)

        i, j = self.move_left(zeroi, zeroj)
        if i is not None and j is not None:
            grid = self.generate_state()
            self.swap(grid, zeroi, zeroj, i, j)
            child_node = Node(grid, self, 'left', self.calculate_heuristic(grid))
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
    def calculate_heuristic(self,state):
        distance = 0
        for i in range(3):
            for j in range(3):
                tile = state[i][j]
                ii , jj = self.helper(tile)
                distance += abs(i-ii) + abs(j - jj)
        return distance


    def helper(self, tile):
        for i in range(3):
            for j in range(3):
                if goal[i][j] == tile:
                    return i , j
    def __lt__(self, other):
            return self.h < other.h
class GreedyBestFirstSearch: 
        def __init__(self, start_state, goal_state): 
            self.start_state = start_state
            self.goal_state = goal_state
            self.open_list = []
            self.closed_list = set()
         
        def solve(self): 
            if not self.is_solvable(self.start_state):
                return None  
        
            start_node = Node(self.start_state, None, None, self.calculate_heuristic(self.start_state))
            heapq.heappush(self.open_list, ( start_node))

            while self.open_list:
                current_node = heapq.heappop(self.open_list)

                if current_node.state == self.goal_state:
                    return self.trace_solution(current_node)

                self.closed_list.add(tuple(tuple(row) for row in current_node.state))

                for child in current_node.generate_children():
                    if tuple(tuple(row) for row in child.state) not in self.closed_list:
                        heapq.heappush(self.open_list, ( child))

            return None
            # if not self.is_solvable(state):
            #         print("The maze is not solveable")
            # pq = PriorityQueue()
            # pq.put(self.calculate_heuristic(self.state),self.state)
            # visited = set()
            # while not pq.empty():
            #     p , state = pq.get()
            #     if self.check_if_it_is_goal(state):
            #         print("Goal found")
            #         return self.trace_solution()


        def trace_solution(self, node): 
        # Trace back the solution path from goal to start 
            solution = []
            while node.parent:
                solution.append(node.move)
                node = node.parent
            return solution[::-1]

        def calculate_heuristic(self, state):
            distance = 0
            for i in range(3):
                for j in range(3):
                    tile = state[i][j]
                    ii , jj = self.helper(tile)
                    distance += abs(i-ii) + abs(j - jj)
            return distance


        def helper(self, tile):
            for i in range(3):
                for j in range(3):
                    if goal[i][j] == tile:
                        return i , j

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
        def check_if_it_is_goal(start):
            count  = 0
            for i in range(3):
                for j in range(3):
                    if start[i][j] != goal[i][j]:
                        count += 1
            return count == 0
        
def main():
    start = [[1, 2, 3], [4, 5, 6], [8,7,0]]

    test1 = GreedyBestFirstSearch(start, goal)
    solution = test1.solve()
    
    if solution is None:
        print("This puzzle is not solvable.")
    else:
        print("Solution:", solution)
    start = [[1, 2, 3], [4, 5, 6], [8,7,0]]
    test2 = GreedyBestFirstSearch(start, goal)
    solution = test2.solve()
    
    if solution is None:
        print("This puzzle is not solvable.")
    else:
        print("Solution:", solution)


main()