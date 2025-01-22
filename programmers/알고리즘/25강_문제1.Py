from collections import deque

def bfs(graph, root):
	if root == 1:
	    print(root)
	for g in graph(root):
		print(g)
	for g in graph(root):
		bfs(graph,g)
	

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