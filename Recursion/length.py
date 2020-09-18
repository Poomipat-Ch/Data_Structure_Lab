def length(txt):
    def loop(lst, acc):
        if not lst:
            return acc
        print(lst[:1] + ('*' if acc % 2 == 0 else '~'),end = '')
        return loop(lst[1:], acc + 1)
    return loop(txt,0)
print('\n'+str(length(input("Enter Input : "))))