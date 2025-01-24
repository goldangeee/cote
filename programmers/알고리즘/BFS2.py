from collections import deque

def bfs(graph, root):
	queue = deque()
	queue.append(root)

	visited_node =[]
	while queue:
		node = queue.popleft()
		visited_node.append(node)
		for i in graph[node]:
			if i not in visited_node:
				queue.append(i)
		
	for i in visited_node:
		print(i,end=' ')
		

graph = {
    1 : [2, 3],
    2 : [1, 4],
    3 : [1],
    4 : [2]
}

bfs(graph, 1)

# 출력
# 1 2 3 4