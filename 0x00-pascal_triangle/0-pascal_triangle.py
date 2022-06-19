'''
Pascal's Triangle
'''


def factorial(x):
    '''
    func: factorial
        returns the factorial of a given number
    args:
        <int: n> : the given number (> 0)
    return:
        <int>
    '''
    return (1) if (x == 0 or x == 1) else (x * factorial(x - 1))


def ncr(i, j):
    '''
    func: ncr
        returns a number resulting from Combinations
        that works out for any value at any place in Pascal's triangle
        formula: !n / !k * (n - k)!
    args:
        <int n, int n> : n and k from the formula above
    return:
        <int>
    '''
    return (int(factorial(i) / (factorial(j) * factorial(i - j))))


def pascal_triangle(n):
    '''
    func: pascal_triangle
        returns a list of lists of integers
        representing the Pascal’s triangle of n
    args:
        <int: n> : number of rows (> 0)
    return:
        <list <of list>>
    '''
    if type(n) is not int and n < 0:
        return ([])
    row, inner_row = [], []
    for i in range(0, n + 1):
        for j in range(0, i + 1):
            inner_row.append(ncr(i, j))
        row.append(inner_row)
        inner_row = []

    return (row)
