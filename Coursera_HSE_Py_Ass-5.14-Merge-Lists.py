

def merge(a, b):
    if len(a) == 0 and len(b) == 0:
        return
    elif len(a) == 0 and len(b) > 0:
        t = b
        m = min(t)
        k.append(m)
        b.remove(m)
        if len(b) > 0:
            merge(a, b)
    elif len(a) > 0 and len(b) == 0:
        t = a
        m = min(t)
        k.append(m)
        a.remove(m)
        if len(a) > 0:
            merge(a, b)
    else:
        t = a + b
        m = min(t)
        k.append(m)
        if m in a:
            a.remove(m)
        else:
            b.remove(m)
        if len(a) > 0 or len(b) > 0:
            merge(a, b)


a = list(map(int, input().split()))
b = list(map(int, input().split()))
k = []
merge(a, b)
print(' '.join(map(str, k)))
