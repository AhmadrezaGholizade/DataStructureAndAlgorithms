class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.size = 0
        self.top = None

    def __str__(self):
        string = "]"
        node = self.top
        for i in range(self.size):
            string = str(node.value) + string
            if i != self.size - 1:
                string = ", " + string
                node = node.next  
        string = "[" + string       
        del node
        return string
    
    def Size(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def Top(self):
        if self.isEmpty():
            raise IndexError("STACK IS EMPTY")
        return self.top.value
    
    def Push(self, x):
        node = Node(x)
        node.next = self.top
        self.top = node
        self.size += 1
        del node
    
    def Pop(self):
        if self.isEmpty():
            raise IndexError("STACK IS EMPTY")
        self.size -= 1
        node = self.top
        temp = node.value
        self.top = node.next
        del node
        return temp


        

        

    

