def numberBit(n):
    def find( decimal_number ): 
        if decimal_number == 0: 
            return 0
        else: 
            return (decimal_number % 2 + 10 * 
                    find(int(decimal_number // 2)))
    t = '1'*n
    y = n
    n = int(t,2) if n > 0 else ""
    def loop(n, x = 0):
        print(f'{find(x):0{y}d}')
        if x < n:
            loop(n, x + 1)
    if y < 0:
        print( 'Only Positive & Zero Number ! ! !')
    else:
        if y == 0:
            print(0)
        else:
            loop(n)

numberBit(int(input('Enter Number : ')))