from project_BST import BST, Node

print("\n------------\nPrinting the Null Tree\n------------\n")
bst = BST()
print(bst)

print("\n------------\nPrinting After Inserting Item to the Tree\n------------\n")
bst.R_Insert2(bst.root, None, 5)
bst.R_Insert2(bst.root, None, 7.5)
bst.R_Insert2(bst.root, None, 3)
bst.R_Insert2(bst.root, None, 2)
print(bst)

print("\n------------\nExplore in tree for cheking relations\n------------\n")
print(bst.root.left.left.parent.parent)

print("\n------------\nR_DelteMin\n------------\n")
bst.R_DeleteMin(bst.root)
print(bst)



print("\n------------\nPrinting After Inserting Items to the Tree\n------------\n")
bst.NR_Insert(7)
bst.NR_Insert(9)
bst.NR_Insert(2)
bst.NR_Insert(3.2)
bst.NR_Insert(1)
bst.NR_Insert(3.4)
bst.NR_Insert(3.5)
bst.NR_Insert(2.5)
print(bst)

print("\n------------\nR_Delete 3.50\n------------\n")
bst.R_Delete(bst.root, 3.5)
print(bst)

print("\n------------\nR_Delete 1\n------------\n")
bst.R_Delete(bst.root, 1)
print(bst)

print("\n------------\nR_DelteMin\n------------\n")
bst.R_DeleteMin(bst.root)
print(bst)

print("\n------------\nR_Delete 3\n------------\n")
bst.R_Delete(bst.root, 3)
print(bst)

print("\n------------\nR_Delete 3\n------------\n")
bst.R_Delete(bst.root, 5)
print(bst)

print("\n------------\nLeftRotate 3.2\n------------\n")
bst.Left_Rotate(bst.R_Search(bst.root, 3.2))
print(bst)

print("\n------------\nRightRotate 3.2\n------------\n")
bst.Right_Rotate(bst.R_Search(bst.root, 3.2))
print(bst)

print("\n------------\nRightRotate 3.4\n------------\n")
bst.Right_Rotate(bst.R_Search(bst.root, 3.4))
print(bst)

print("\n------------\nRightRotate 7\n------------\n")
bst.Right_Rotate(bst.R_Search(bst.root, 7))
print(bst)

# print("\n------------\nR_Search 3.75\n------------\n")
# print(bst.R_Search(bst.root, 3.75))

# print("\n------------\nR_Minimum\n------------\n")
# print(bst.R_Minimum(bst.root))

# print("\n------------\nR_Maximum\n------------\n")
# print(bst.R_Maximum(bst.root))

# print("\n------------\nNR_Minimum\n------------\n")
# print(bst.NR_Minimum(bst.root))

# print("\n------------\nNR_Maximum\n------------\n")
# print(bst.NR_Maximum(bst.root))

# print("\n------------\nSuccessor 3.00\n------------\n")
# print(bst.Successor(bst.R_Search(bst.root, 3)))
# print("\n------------\nSuccessor 3.50\n------------\n")
# print(bst.Successor(bst.R_Search(bst.root, 3.5)))

# print("\n------------\nPredecessor 2.00\n------------\n")
# print(bst.Predecessor(bst.R_Search(bst.root, 2)))
# print("\n------------\nPredecessor 2.50\n------------\n")
# print(bst.Predecessor(bst.R_Search(bst.root, 2.5)))

print("\n")