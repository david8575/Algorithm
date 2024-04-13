class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singleLinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode
    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


myList = singleLinkedList()
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)
myList.append(5)

myList.printList()