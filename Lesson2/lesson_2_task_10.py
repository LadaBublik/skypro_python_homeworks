# x - начальная сумма вклада
# y - срок вклада в годах

def bank(x, y):
    for i in range(y):
        x = x + (x / 10)
    print(x)


bank(1000, 10)
