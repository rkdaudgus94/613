import copy
x = list(map(list,input("정수를 입력하시오: ")))
y = copy.deepcopy(x)

x.reverse()
print(x[:])
print(y[:])
