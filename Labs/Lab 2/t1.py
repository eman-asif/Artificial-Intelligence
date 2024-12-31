from collections import deque
# from stack import Stack
def dfs(graph , node, visited = None):
    if visited is None:
        visited= set()
    visited.add(node)
    print(node, end = ' ')
    for  i in graph[node]:
        if i not in visited:
            
            dfs(graph , i, visited)

    
def bfs(graph , node):
    visited = set()
    q = deque()
    q.append(node)
    while q:
        n = q.popleft()
        print(n, end = ' ')
        for i in graph[n]:
                if i not in visited:
                    q.append(i)
                    visited.add(i)
def iddfs1(graph, start, goal):
    depth_limit = 0
    while True:
        result = dfs1(graph, start, goal, depth_limit)
        if result is not None:
            return result , depth_limit
        depth_limit += 1

def dfs1(graph, node, goal, depth_limit):
    if node == goal:
        return node
    if depth_limit == 0:
        return None
    for neighbor in graph[node]:
        result = dfs1(graph, neighbor, goal, depth_limit - 1)
        if result is not None:
            return result
    return None
def dls(graph, node, depth, visited):
    if depth == 0:
        print(node, end=' ')
        return True
    if node not in visited:
        visited.add(node)
        for neighbor in graph[node]:
            if dls(graph, neighbor, depth - 1, visited):
                return True
        visited.remove(node)
    return False


def iddfs(graph, start, max_depth):
    for depth in range(max_depth):
        visited = set()
        if dls(graph, start, depth, visited):
            return

def main():
    g = [[2,1,3], [1,7],[],[],[3,1,3,6], [2,0,3], [1,4], [1,5]]
    bfs(g, 0)
    print()
    dfs(g , 0)
    print()
    graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

    start_node = 'A'
    goal_node = 'B'

    path, lecel = iddfs1(graph, start_node, goal_node)
    print(path, lecel)
    # path = iddfs(graph, start_node)
    # print(path)      
main()