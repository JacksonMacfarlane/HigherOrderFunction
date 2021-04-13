def sum1(x):
    def sum2(y):
        return x + y

    return sum2


add9 = sum1(9)

print(10)
print(add9(10))
