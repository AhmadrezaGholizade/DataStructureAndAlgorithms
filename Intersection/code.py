class Segment():
    def __init__(self, ux, uy, lx, ly):
        self.upper = (ux, uy)
        self.lower = (lx, ly)

class Event():
    def __init__(self, xy, type, parent = None):
        self.parent = parent
        self.value = xy
        self.type = type
        self.left_child = None
        self.right_child = None
    def __gt__(self, other):
        return self.value[0] > other.value[0]
    def __lt__(self, other):
        return self.value[0] < other.value[0]
    # def __eq__(self, other):
    #     print(isinstance(other, Event))
    #     if type(other) != Event:
    #         return True
    #     return self.value[0] == other.value[1]

class BST():
    def __init__(self):
        self.root = None
    def is_empty(self):
        return self.root == None
    def add(self, node):
        if self.root == None:
            self.root = node
            return
        temp = self.root
        while temp != None:
            if node < temp:
                if temp.left_child == None:
                    temp.left_child = node
                    temp.left_child.parent = temp
                    return
                temp = temp.left_child
            if temp.right_child == None:
                temp.right_child = node
                temp.right_child.parent = temp
                return
            temp = temp.right_child
    def delete_max(self):
        temp = self.root
        while temp.right_child != None:
            temp = temp.right_child
        if temp == self.root:
            if temp.left_child == None:
                self.root = None
                return temp 
            self.root == temp.left_child
            self.root.parent = None
            return temp
        if temp.left_child != None:
            temp.left_child.parent = temp.parent
            temp.parent.right_child = temp.left_child
            return temp 
        temp.parent.right_child = None
        temp.parent = None
        return temp 
