def pantip(k, n, arr, path):
    if n == len(arr):
        if k == sum(path):
            print(*path)
            return 1
        return 0
    return pantip(k,n+1,arr,path+[arr[n]]) + pantip(k,n+1,arr,path)
        

inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))