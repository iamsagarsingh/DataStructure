class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None

class Tree:
    def __init__(self):
        self.head = None
    
    def inorder(self,root):
        if root != None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
    
    def preorder(self,root):
        if root != None:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root != None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)    

    def insert(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
           
        else:
            trav =self.head
            while(trav):
                if data < trav.data:
                    if trav.left == None:
                        trav.left = node
                        trav = trav.left
                    
                    trav = trav.left
                else:
                    if trav.right == None:
                        trav.right = node
                        trav  = trav.right

                    trav = trav.right
                
    def findmax(self):
        ptr = self.head
        while(ptr.right):
            ptr = ptr.right
        print(ptr.data)

    def findmin(self):
        ptr = self.head
        while(ptr.left):
            ptr = ptr.left
        print(ptr.data)

    def height(self,root):
        if root == None:
            return -1
        else:
            return 1 + max(self.height(root.left),self.height(root.right))


t = Tree()

t.insert(20)
t.insert(15)
t.insert(11)
t.insert(18)
t.insert(25)
t.insert(22)

print("In-Order Traversal:")
t.inorder(t.head)

print("\n")
print("Pre-Order Traversal:")
t.preorder(t.head)

print("\n")
print("Post-Order Traversal:")
t.postorder(t.head)

print("\n")
print("Maximum element:")
t.findmax()

print("\n")
print("Minimum element:")
t.findmin()

print("\n")
print("Height of Tree:")
print(t.height(t.head))
