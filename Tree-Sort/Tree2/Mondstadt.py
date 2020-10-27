lst , comp = input("Enter Input : ").split('/')
lst = list(map(int, lst.split()))
comp = comp.split(',')
comp = [list(map(int,x.split())) for x in comp]
print(sum(lst))
a,b = 0, 0
for i in comp:
    a = lst[i[0]] + (lst[2*i[0]+1] if 2*i[0]+1 < len(lst) else 0) + (lst[2*i[0]+2] if 2*i[0]+2 < len(lst)  else 0)
    b = lst[i[1]] + (lst[2*i[1]+1] if 2*i[1]+1 < len(lst) else 0) + (lst[2*i[1]+2] if 2*i[1]+2 < len(lst)  else 0)
    print(str(i[0])+("="if a == b else ">" if a > b else "<")+str(i[1]))