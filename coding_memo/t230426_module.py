def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def div(a,b):
    return a/b

class Calculator:
    def __init__(self):
        pass
    def mul(self, a, b):
        return a*b
    def div(self, a,b):
        return a/b


if __name__ == '__main__':
    print(add(1, 2))
    print(sub(1, 2))