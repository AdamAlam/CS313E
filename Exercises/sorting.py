def merge_sort(a):
    n = len(a)
    if n == 1:
        return a
    else:
        mid = (n//2)
        a1 = a[0:mid]
        a2 = a[mid:n]
        


def merge(a1, a2):
    c = []
    while len(a1) > 0 and len(a2) > 0:
        if a1[0] < a2[0]:
            c.append(a1[0])
            a1.pop(0)
        else:
            c.append(a2[0])
            a2.pop(0)
    while len(a1) > 0:
        c.append(a1[0])
        a1.pop(0)
    while len(a2) > 0:
        c.append(a2[0])
        a2.pop(0)

    return c



ex = [2,5,7,52,6,36,336,7,3,7,3,25,2]
print(merge_sort(ex))