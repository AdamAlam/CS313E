lol = [5,6,7,8,8,9,0,12,4,5,3,5,3,2,1,534,245]


# Returns the sum of a list using recursion
def list_sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + list_sum(arr[1:])

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

def sigma(n):
    if n == 1:
        return n
    else:
        return n + sigma(n-1)

