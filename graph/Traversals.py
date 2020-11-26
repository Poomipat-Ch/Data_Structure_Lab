

def depth_first_traversals(v,visited):
    visited.add(v)
    print(v, end=' ')
    for i in graph[key.index(v)]:
        if i not in visited:
            depth_first_traversals(i,visited)

def bredth_first_traversals(v,visited):
    if v not in visited:
        print(v, end=' ')
        visited.add(v)
        if len(graph[key.index(v)]) > 1:
            bredth_first_traversals(graph[key.index(v)][0],visited)
    for i in graph[key.index(v)]:
        if i not in visited:
            print(i, end=' ')
            visited.add(i)
    



arr = input('Enter : ').split(',')

node = dict()

for i in arr:
    i = i.split()
    node[i[0]] = node.get(i[0])
    node[i[1]] = node.get(i[1])
size = len(node)
key = sorted(list(node.keys()))
graph = [[] for _ in range(size)]
for j in arr:
    j = j.split()
    graph[key.index(j[0])].append(j[1])
    graph[key.index(j[1])].append(j[0])
print("Depth First Traversals : ",end='')
visited = set()
for vertex in key:
    if vertex not in visited:
        depth_first_traversals(vertex,visited)
        
print("\nBredth First Traversals : ",end='')
visited = set()
for vertex in key:
    if vertex not in visited:
        bredth_first_traversals(vertex,visited)