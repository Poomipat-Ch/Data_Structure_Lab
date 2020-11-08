
def selection_sort(n):
    for i in range(len(n)):
        min_index = i
        for j in range(i+1, len(n)):
            if n[min_index] > n[j]:
                min_index = j
        n[i], n[min_index] = n[min_index], n[i]
    return n


def drome(n):
    n_sorted = selection_sort(n.copy())
    n_set = list(set(n_sorted))
    duplicate = n_set != n_sorted
    # print(n,n_sorted,n_set,duplicate) #debug
    if len(n_set) == 1:
        return "Repdrome"
    if n_sorted == n and not duplicate:
        return "Metadrome"    
    if n_sorted == n and duplicate:
        return "Plaindrome"
    if n_sorted[::-1] == n and not duplicate:
        return "Katadrome"
    if n_sorted[::-1] == n and duplicate:
        return "Nialpdrome"
    return "Nondrome"



n = list(map(int, [x for x in input("Enter Input : ")]))
print(drome(n))