def shortest_path(v, target, path=[], dist=0, shortest=None):
    if v == target and (shortest == None or dist <= shortest[1]):
        shortest = [path,dist]
        return shortest

    for i in sorted(graph[key.index(v)]):
        if i[1] not in path:
            tmp = shortest_path(i[1],target,path+[i[1]],dist+int(i[0]),shortest)
            if tmp is not None:
                shortest = tmp    
    return shortest

set_graph, path_to_print = input('Enter : ').split('/')

key = set()
for i in set_graph.split(','):
    i = i.split()
    key.add(i[0])
    key.add(i[2])
for j in path_to_print.split(','):
    j = j.split()
    key.add(j[0])
    key.add(j[1])
key = list(key)
size = len(key)

graph = [[] for _ in range(size)]
for i in set_graph.split(','):
    i = i.split()
    graph[key.index(i[0])].append(i[1:])

for i in path_to_print.split(','):
    source, target = i.split()
    tmp = shortest_path(source, target, [source])
    if tmp:
        print(f"{source} to {target} : {'->'.join(tmp[0])}")
    else:
        print(f"Not have path : {source} to {target}")