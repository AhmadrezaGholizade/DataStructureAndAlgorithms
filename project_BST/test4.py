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
print(bst)

print("\n------------\nDelete 5\n------------\n")
bst.NR_Delete(bst.root)
print(bst)

print("\n")