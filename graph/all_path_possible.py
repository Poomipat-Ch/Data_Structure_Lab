def shortest_path(v, target, path=[], shortest=None,all_path=[]):
    if v == target:
        shortest = path
        for i,data in enumerate(all_path):
            if len(path) < len(data):
                all_path.insert(i, path)
                return shortest
        all_path.append(shortest)
        return shortest

    for i in graph[key.index(v)]:
        if i not in path:
            tmp = shortest_path(i,target,path+[i],shortest)
            if tmp is not None:
                shortest = tmp    
    return all_path

set_graph, path_to_print = input('Enter Input : ').split('/')

key = set()
for i in set_graph.split(','):
    i = i.split()
    key.add(i[0])
    key.add(i[1])
key = list(key)
size = len(key)

graph = [[] for _ in range(size)]
for i in set_graph.split(','):
    i = i.split()
    graph[key.index(i[0])].append(i[1])
    graph[key.index(i[1])].append(i[0])

source, target = path_to_print.split()
tmp = shortest_path(source, target, [source])
if tmp:
    print(f'All possible path from {source} to {target} :')
    for i in tmp:
        print(" -> ".join(i))
else:
    print(f"{source} can't go to {target}")