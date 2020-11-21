def bi_search(l, r, arr, x):
    if l == r:
        return False
    elif arr[l] == x:
        return True
    return bi_search(l+1,r,arr,x)
    

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))