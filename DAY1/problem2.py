'''Write a Python program to print the numbers in the list which are divisible by 3.'''

def divby3():
    list1 = []
    for i in range(1,30):
        if i % 3 == 0:
            list1.append(i)
    return list1
result = divby3()
print(result)

            
