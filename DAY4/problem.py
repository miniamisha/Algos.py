#'''Implement Linear Search using python.'''
class linearsearch:
    def __init__(self):
        self.x = [23,2,98,28,83,22,0,90,48,84]
        return

    def search(self,y):
        for i in self.x:
            if i == y:
                return i
            else:
                i += 1
            

obj = linearsearch()
y = int(input('enter number you are searching for: '))
print(obj.search(y))
