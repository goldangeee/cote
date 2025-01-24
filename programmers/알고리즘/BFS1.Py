from collections import deque

def bfs(graph, root):
    queue = deque(graph[root])

    while queue:
        node = queue.popleft()
        print(node,end=' ')

        # 이웃노드 추가
        queue.extend(graph[node])

graph = {
    1: [2, 3, 8],
    2: [7],
    3: [4],
    4: [5],
    5: [],
    6: [],
    7: [6],
    8: []
}

bfs(graph, 1)

# 출력
# 1 2 3 8 7 4 6 5