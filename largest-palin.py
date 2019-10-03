# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

ran = 999

def ispalin(x):
    # print(x,x[::-1] )
    x = str(x)
    if x == x[::-1]:
        return True
    return False
temp = 0
for i in range(100,ran+1):
    for j in range(100,ran+1):
        tem = i*j
        # print(i,j,tem,ispalin(str(tem)))
        if(ispalin(str(tem))==True):
            # print(tem)
            if tem>temp:
                temp = tem

print(temp)

print(ispalin(9009))
