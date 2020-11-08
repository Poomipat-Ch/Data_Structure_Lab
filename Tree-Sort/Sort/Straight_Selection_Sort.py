def straight_selection_sort(lst, i=0):
    if len(lst)-1 == i:
        return
    
    if lst.index(max(lst[:len(lst)-i-1])) != len(lst) - i - 1:
        if lst[lst.index(max(lst[:len(lst)-i-1]))] > lst[len(lst) - i - 1]:
            print(f"swap {lst[len(lst) - i - 1]} <-> {lst[lst.index(max(lst[:len(lst)-i-1]))]} : ",end='')
            lst[lst.index(max(lst[:len(lst)-i-1]))], lst[len(lst) - i - 1] = lst[len(lst) - i - 1], lst[lst.index(max(lst[:len(lst)-i-1]))]
            print(lst)
            straight_selection_sort(lst,i+1)
        else:
            straight_selection_sort(lst,i+1)
    return lst

n = list(map(int, input("Enter Input : ").split()))
print(straight_selection_sort(n))