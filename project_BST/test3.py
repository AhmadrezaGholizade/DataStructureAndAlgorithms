from project_BST import BST

print("\n------------\nPrinting the Null Tree\n------------\n")
bst = BST()
print(bst)

print("\n------------\nPrinting After Inserting Item to the Tree\n------------\n")
bst.NR_Insert(5)
print(bst)

print("\n------------\nDelete 5\n------------\n")
bst.NR_BST_Delete(bst.root)
print(bst)

print("\n------------\nPrinting After Inserting Items to the Tree\n------------\n")
bst.NR_Insert(7)
bst.NR_Insert(3)
bst.NR_Insert(4)
bst.NR_Insert(9)
bst.NR_Insert(1)
bst.NR_Insert(3.5)
bst.NR_Insert(3.7)
print(bst)

print("\n------------\nSuccessor: \n------------\n")
print("Successor for Minimum of Tree:", bst.Successor(bst.NR_Minimum()))
print("Successor for       4.00     :", bst.Successor(bst.root.left.right))
print("Successor for       7.00     :", bst.Successor(bst.root))
print("Successor for       9.00     :", bst.Successor(bst.root.right))


print("\n")