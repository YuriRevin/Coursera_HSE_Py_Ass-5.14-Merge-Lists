lista = list(map(int, input().split()))
listb = list(map(int, input().split()))


def merge(a: list, b: list):
    lena = len(a)
    lenb = len(b)
    if len(a) > lenb:
        a, b = b, a
        lena, lenb = lenb, lena
    i = 0
    j = 0
    listn = []
    while i <= lena:
        if i == lena:
            listn = listn + b[j:lenb]
            return listn
        elif j == lenb:
            listn = listn + a[i:lena]
            return listn
        if a[i] < b[j]:
            listn.append(a[i])
            i += 1
        elif a[i] == b[j]:
            listn.append(a[i])
            listn.append(b[j])
            i += 1
            j += 1
        else:
            listn.append(b[j])
            j += 1


print(*merge(lista, listb))
