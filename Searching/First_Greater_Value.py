
def first_greater(left, right):
    for i in range(len(right)):
        for j in range(len(left)):
            if right[i] <= left[j]:
                if j < len(left)-1:
                    print(left[j] if right[i] < left[j] else left[j+1])
                    break
            elif j == len(left)-1:
                print("No First Greater Value")
                break
left,right = list([list(map(int,x.split())) for x in input("Enter Input : ").split('/')])
first_greater(sorted(left), sorted(right))