x = list(input("문자열A: "))
y = list(input("문자열B: "))

print(x)
print(y)

for i in range(len(x)-1,-1,-1):
    if x[i] == y[0]:
        del y [0]
    else:
        break


def listJoin(index):
    result = ''.join(i for i in index)
    return result

print(listJoin(x)+listJoin(y))
