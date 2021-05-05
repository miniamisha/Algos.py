'''Write a python program that takes two numbers as the input such as X and Y and print the result
of X^Y(X to the power of Y).'''
#i/p = int
#o/p = int

def topower():
    X = int(input('First Number: '))
    Y = int(input('Second Number'))
    return X**Y

result = topower()
print('X to the power of Y',  result)
