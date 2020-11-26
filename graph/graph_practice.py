def graph(data_arr,matrix):
    for data in data_arr:
        data = data.split()
        matrix[key.index(data[0])][key.index(data[1])] = 1

def printMatrix():
    print("    "+'  '.join(key))
    for i,j in zip(matrix,key):
        print(f"{j} : " +', '.join(map(str,i)))


arr = input('Enter : ').split(',')

node = {}

for i in arr:
    i = i.split()
    node[i[0]] = node.get(i[0])
    node[i[1]] = node.get(i[1])
size = len(node)
key = sorted(list(node.keys()))
matrix = [[0]*size for _ in range(size)]
graph(arr,matrix)
printMatrix()