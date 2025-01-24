from collections import deque

def bfs(graph, root):
	visited_node =[]
	queue = deque()
	
	queue.append(root)
	
	while queue:
		node = queue.popleft()
		visited_node.append(node)
		queue.extend(graph[node])
		
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