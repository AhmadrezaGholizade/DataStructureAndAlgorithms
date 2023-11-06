class Node:
    def __init__(self, Value = None):
        self.left = None
        self.right = None
        self.key = Value
        self.parent = None

    def __str__(self):
        return f"{self.key:0.2f}"
    
class BST():
    def __init__(self):
        self.root = None
    
    def __str__(self):
        if self.root != None:
            li = [[self.root]]
            i = 0
            row = [0]
            while not all(item is None for item in row):
                del row
                row = []
                for item in li[i]:
                    if item == None:
                        row.append(None)
                        row.append(None)
                    else:
                        row.append(item.left)
                        row.append(item.right)
                li.append(row)
                i += 1

            string = ''
            height = len(li) - 1 
            i = 1
            for k in range(height):
                row = li[k]
                string += "     " * (2 ** (height - i) - 1)
                for item in row:
                    if item != None:
                        string += f"{item}" + "     " * (2 ** (height - i + 1) - 1)
                    else:
                        string += "     " + "     " * (2 ** (height - i + 1) - 1)
                i += 1
                string += "\n\n"
            return string[:-4]
        else:
            return 'This Tree Is Null'

    def R_Search(self, r, x):
        if r == None or x == r.key:
            return r
        
        if x < r.key:
            return self.R_Search(r.left, x)
        else:
            return self.R_Search(r.right, x)
        
    def NR_Search(self, x = None):
        r = self.root
        # While I havn't reached the goal or None:
        while r != None and x != r.key:
            if x < r.key:
                r = r.left
            else:
                r = r.right
        return r
    
    def R_Minimum(self, r):
        if r.left == None:
            return r
        return self.R_Minimum(r.left)
    
    def NR_Minimum(self, r = None):
        # if The tree is Null
        if self.root == None:
            return self.root
        
        # defualt Mode find the Mninmum of Whole the Tree
        if r == None:
            r = self.root

        while r.left != None:
            r = r.left
        return r
    
    def R_Maximum(self, r):
        if r.right == None:
            return r
        return self.R_Maximum(r.right)
    
    def NR_Maximum(self, r = None):
        # if The tree is Null
        if self.root == None:
            return self.root
        
        # defualt Mode find the Mninmum of Whole the Tree
        if r == None:
            r = self.root

        while r.right != None:
            r = r.right
        return r
    
    def Successor(self, r):
        if r.right != None:
            return self.NR_Minimum(r.right)
        y = r.parent
        while y != None and r == y.right:
            r = y
            y = y.parent
        return y
    
    def Predecessor(self, r):
        if r.left != None:
            return self.NR_Minimum(r.left)
        y = r.parent
        while y != None and r == y.left:
            r = y
            y = y.parent
        return y

    def R_Insert2(self, r, p, x, LeftorRight = None):
        if self.root == None:
            self.root = Node(x)
        elif r == None:
            r = Node(x)
            r.parent = p
            if LeftorRight == 1:
                p.left = r
            elif LeftorRight == 2: 
                p.right = r
        elif x < r.key:
            return self.R_Insert2(r.left, r, x, 1)
        else:
            return self.R_Insert2(r.right, r, x, 2)
        
    def NR_Insert(self, x):
        n = Node(x)
        prep = None
        p = self.root

        while p != None:
            prep = p
            if x < p.key:
                p = p.left
            else:
                p = p.right
        n.parent = prep
        
        if prep == None:
            self.root = n
        elif x < prep.key:
            prep.left = n
        else:
            prep.right = n

    def R_DeleteMin(self, r):
        if r == None:
            raise IndexError("Tree Is Empty")
        if r.left == None:
            x = r.key
            if r == self.root:
                self.root = r.right
            elif r == r.parent.left:
                r.parent.left = r.right
            elif r == r.parent.right:
                r.parent.right = r.right
            if r.right != None:
                r.right.parent = r.parent
            return x
        else:
            return self.R_DeleteMin(r.left)
        
    def R_Delete(self, r, x):
        if self.root == None:
            raise IndexError("Tree Is Empty")
        if r == None:
            raise IndexError("This Node dosn't exist")
        if x < r.key:
            return self.R_Delete(r.left, x)
        elif x > r.key:
            return self.R_Delete(r.right, x)
        if x == r.key:
            temp = r
            if r.left == None:
                r = r.right
                if r != None:
                    r.parent = temp.parent
                if temp == temp.parent.right:
                    temp.parent.right = r
                else:
                    temp.parent.left = r
                del temp
            elif r.right == None:
                r = r.left
                if r != None:
                    r.parent = temp.parent
                if temp == temp.parent.right:
                    temp.parent.right = r
                else:
                    temp.parent.left = r
                del temp
            else: 
                r.key = self.R_DeleteMin(r.right)

        
    def NR_Delete(self, z):
        if z.left == None or z.right == None:
            y = z
        else:
            # Two Children
            y = self.Successor(z)
        
        if y.left != None:
            x = y.left
        else:
            x = y.right
        
        if x != None:
            # at least One Children
            x.parent = y.parent
        if y.parent == None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        if y != z:
            z.key = y. key

    def Left_Rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def Right_Rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

            
    # def Left_Rotate(self, x):
    #     y = x.right
    #     x.right 
# bst = BST()
# bst.NR_Insert(12)
# bst.NR_Insert(11)
# bst.NR_Insert(10)
# print(bst)