def roman_recursive(num, sr = ''):
    if num >= 1000 :
        sr = roman_recursive(num-1000, sr+'m')
    elif num >= 900 :
        sr = roman_recursive(num-900, sr+'cm')
    elif num >= 500 :
        sr = roman_recursive(num-500, sr+'d')
    elif num >= 400 :
        sr = roman_recursive(num-400, sr+'cd')
    elif num >= 100 :
        sr = roman_recursive(num-100, sr+'c')
    elif num >= 90 :
        sr = roman_recursive(num-90, sr+'xc')
    elif num >= 50 :
        sr = roman_recursive(num-50, sr+'l')
    elif num >= 40 :
        sr = roman_recursive(num-40, sr+'xl')
    elif num >= 10 :
        sr = roman_recursive(num-10, sr+'x')
    elif num >= 9 :
        sr = roman_recursive(num-9, sr+'ix')
    elif num >= 5 :
        sr = roman_recursive(num-5, sr+'v')
    elif num >= 4 :
        sr = roman_recursive(num-4, sr+'iv')
    elif num >= 1 :
        sr = roman_recursive(num-1, sr+'i')
    return sr


print("Convert Decimal to Roman number",end='')
num = int(input("Enter Decimal number : "))
# print("Roman number Iterative : ",roman_iterative(num),sep = '')
print("Roman number Recursive : ",roman_recursive(num),sep = '')