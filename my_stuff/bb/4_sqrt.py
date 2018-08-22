# 4.  Write an algorithm to calculate the square root of a number.

'''
maybe binary search?

do we need to handle imaginary numbers?
'''

def square_root(n, error=.0001):
    if n < -1:
        print("cannot handle imaginary numbers")
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1

    root = n

    while abs(root*root-n) > error:
        if root*root > n:
            root = (root)/2
        else:
            root = root * 1.5
        print(root)

    return root

print(square_root(25))

print(square_root(.25))

print(square_root(-25))
