def Fib(n):
    a = b = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            lf = a + b
            a, b = b, lf
            yield lf


fibs = list(Fib(10))
print(fibs)

n = 1
for i in fibs:
    print(f'Wyrażenie {n} wynosi {i}')
    n += 1
