# from collections import tack
# from stack import Stack
goal = [[1,2,3],[4,5,6],[7,8,0]]
# stack = Stack()
stack = []
def move_up(zeroi , zeroj):
    i =zeroi - 1
    if i >=0 :
        return i , zeroj
    return None , None
def move_down( zeroi , zeroj):
    i = zeroi + 1
    if i <= 2:
        return i , zeroj
    
    return None , None
def move_right(zeroi , zeroj):
    j =zeroj - 1
    if j >=0 :
        return zeroi , j
    return None, None
def move_left(zeroi , zeroj):
    j= zeroi + 1
    if j <= 2:
        return zeroi , j
def dfs1(grid, depth_limit):
    if check_if_it_is_goal(grid):
        return stack
    if depth_limit == 0:
        return None
    zeroi , zeroj = index_of_zero(grid)
    # print(grid)
    # print(zeroi,zeroj)
    i , j = move_up(zeroi , zeroj)
    if i!= None and j!= None:
        stack.append(grid)
        swap(grid , i , j , zeroi , zeroj)

        result = dfs1(grid , depth_limit - 1)
        if result is not None:
            return result
        
        grid = stack.pop(0)
    i , j = move_down(zeroi , zeroj)
    if i!= None and j!= None:
        stack.append(grid)
        swap(grid , i , j , zeroi , zeroj)

        result = dfs1(grid , depth_limit - 1)
        if result is not None:
            return result
        grid = stack.pop(0)
    i , j = move_right(zeroi , zeroj)
    if i!= None and j!= None:
        stack.append(grid)
        swap(grid , i , j , zeroi , zeroj)

        result = dfs1(grid , depth_limit - 1)
        if result is not None:
            return result
        grid = stack.pop(0)
    i , j = move_left(zeroi , zeroj)
    if i!= None and j!= None:
        stack.append(grid)
        swap(grid , i , j , zeroi , zeroj)

        result = dfs1(grid , depth_limit - 1)
        if result is not None:
            return result
        grid = stack.pop(0)
    
    return None
def swap(grid , a , b , c , d):
    grid[a][b] , grid[c][d] =  grid[c][d], grid[a][b]
def check_if_it_is_goal(start):
    count  = 0
    for i in range(3):
        for j in range(3):
            if start[i][j] != goal[i][j]:
                count += 1
    return count == 0

def index_of_zero(start):
    for i in range(3):
        for j in range(3):
            if start[i][j] == 0:
                return i , j
def iddfs1(grid):
    depth = 0
    lim = 20
    while depth <= lim:
        result = dfs1(grid, depth)
        if result is not None:
            return result 
        depth += 1  
def main():
    start = [[1,2,3],[4,5,6],[7,0,8]]
    # is_goal = check_if_it_is_goal(start)
    result = iddfs1(start)
    if result:
        print('Found')
        # n = len(stack)
        # for i in range(n):
        #     print(stack[i])
    else:
        print('Not found!')
main()