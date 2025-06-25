num = int(input())
yx = []
for _ in range(num):
    x,y = map(int,input().split(" "))
    my_list = []
    my_list.append(y)
    my_list.append(x)
    yx.append(my_list)
only_y = [i[0] for i in yx]
only_x = [i[1] for i in yx]
y_max = max(only_y)-1
x_max = max(only_x)-1
y_end = y_max+10
x_end = x_max+10
visited = [[False] * (x_end+1) for _ in range(y_end+1)]

def false_to_true(yx):
    y_start = yx[0]-1
    x_start = yx[1]-1
    for y in range(y_start,y_start+10):
        for x in range(x_start,x_start+10):
            if visited[y][x] == False:
                visited[y][x] = True

for i in yx:
    false_to_true(i)

result = 0
for v in visited:
    result += v.count(True)
print(result)