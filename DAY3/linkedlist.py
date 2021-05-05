class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
            return 
        temp = self.head 
        while temp.next != None:
            temp = temp.next
        temp.next = new

    def display(self):
        if self.head == None:
            print("No node to display")
            return
        temp = self.head
        while temp.next != None:
            print(temp.data)
            temp = temp.next

li = LinkedList()
li.insertEnd(10)
li.insertEnd(3)
li.insertEnd(9)
li.display()

