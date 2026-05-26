def outer_func(num):
    def inner_func():
        print("hey inner function this side:::=>>")
        y=num()
        y=y.upper()
        return y
    return inner_func
#outer_func
def test():
    return"my name is tushar"
print(test())
test=outer_func(test)
print(test())


