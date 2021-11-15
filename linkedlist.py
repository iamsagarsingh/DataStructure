class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class singlylinkedlist:
    def __init__(self):
        self.head = None

    def traverse(self):
        n = self.head
        while(n):
            print(n.data)
            n = n.next

    def insertatend(self,d):
        node = Node(d)
        if not self.head:   #if node is empty
            self.head = node
        else:   # traverse till the end
            n = self.head
            while(n.next != None):
                n = n.next
            n.next = node



    def insertatbeginning(self,d):
        node = Node(d)
        if not self.head:  # if self.head == None
            self.head = node
        else:
            temp = self.head
            self.head = node
            self.head.next = temp

sl = singlylinkedlist()
sl.insertatbeginning(12)
sl.insertatbeginning(13)
sl.insertatbeginning(14)

sl.insertatend(34)
sl.insertatend(35)
sl.insertatend(36)

sl.traverse()
