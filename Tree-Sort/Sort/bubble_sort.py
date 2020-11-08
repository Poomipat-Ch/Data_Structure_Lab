def bubble_sort(lst):
    step = 1
    for i in range(len(lst) - 1):
        cur = None
        printed = False
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1], lst[j]
                cur = lst[j+1]
        if j != 0 and cur != None:
            print(f"{step} step : {lst} move[{cur}]")
            step += 1
        elif j == 0:
            print(f"last step : {lst} move[{cur}]")

n = list(map(int, input("Enter Input : ").split()))

bubble_sort(n)
