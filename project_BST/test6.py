from project_BST import BST

print("\n------------\nPrinting the Null Tree\n------------\n")
bst = BST()
print(bst)

print("\n------------\nPrinting After Inserting Item to the Tree\n------------\n")
bst.NR_Insert(5)
print(bst)

print("\n------------\nPrinting After Inserting Items to the Tree\n------------\n")
bst.NR_Insert(7)
bst.NR_Insert(9)
bst.NR_Insert(2)
bst.NR_Insert(3)
bst.NR_Insert(1)
bst.NR_Insert(3.4)
bst.NR_Insert(3.5)
bst.NR_Insert(2.5)
print(bst)

print("\n------------\nR_Search 3.50\n------------\n")
print(bst.R_Search(bst.root, 3.5))

print("\n------------\nR_Search 3.75\n------------\n")
print(bst.R_Search(bst.root, 3.75))

print("\n------------\nR_Minimum\n------------\n")
print(bst.R_Minimum(bst.root))

print("\n------------\nR_Maximum\n------------\n")
print(bst.R_Maximum(bst.root))

print("\n------------\nNR_Minimum\n------------\n")
print(bst.NR_Minimum(bst.root))

print("\n------------\nNR_Maximum\n------------\n")
print(bst.NR_Maximum(bst.root))

print("\n------------\nSuccessor 3.00\n------------\n")
print(bst.Successor(bst.R_Search(bst.root, 3)))
print("\n------------\nSuccessor 3.50\n------------\n")
print(bst.Successor(bst.R_Search(bst.root, 3.5)))

print("\n------------\nPredecessor 2.00\n------------\n")
print(bst.Predecessor(bst.R_Search(bst.root, 2)))
print("\n------------\nPredecessor 2.50\n------------\n")
print(bst.Predecessor(bst.R_Search(bst.root, 2.5)))

print("\n")