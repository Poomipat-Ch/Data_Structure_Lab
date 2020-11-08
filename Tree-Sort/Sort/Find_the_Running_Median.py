def selection_sort(n):
    for i in range(len(n)):
        min_index = i
        for j in range(i+1, len(n)):
            if n[min_index] > n[j]:
                min_index = j
        n[i], n[min_index] = n[min_index], n[i]
    return n



l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "minHeap and maxHeap"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    lst = []
    for i in l:
        lst.append(i)
        lst_sorted = selection_sort(lst.copy())
        if len(lst_sorted) <= 1:
            print(f"list = {lst} : median = {lst_sorted[0]:.1f}")
        else: 
            print(f"list = {lst} : median = {lst_sorted[len(lst)//2] if len(lst)%2==1 else (lst_sorted[len(lst)//2-1]+lst_sorted[len(lst)//2])/2:.1f}")