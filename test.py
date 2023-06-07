def calc(numbers: dict):
    return numbers["q"] + numbers["b"]

data = {
    "q": 1,
    "b": 2
}
a = calc(data)


def test(a, b):
    return a - b


# a = calc(4, 5)
# print(a+5)
# print(calc(4, 5))
print(test(a, 4))
