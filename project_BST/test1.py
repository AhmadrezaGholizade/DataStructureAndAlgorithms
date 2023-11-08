from project_BST import BST

print("\n------------\nPrinting the Null Tree\n------------\n")
bst = BST()
print(bst)

print("\n------------\nPrinting After Inserting Item to the Tree\n------------\n")
bst.NR_Insert(15)
print(bst)

print("\n------------\nPrinting After more Inserting Item to the Tree\n------------\n")
bst.NR_Insert(16)
bst.NR_Insert(12)
bst.NR_Insert(13)
bst.NR_Insert(15.5)
bst.NR_Insert(16)
print(bst)

print("\n------------\nPrinting After more Inserting Item to the Tree\n------------\n")
bst.NR_Insert(11)
bst.NR_Insert(10)
bst.NR_Insert(13.5)
bst.NR_Insert(12.5)
print(bst)

print("\n------------\nPrinting Minimum(NR_Procedure)\n------------\n")
print("Minimum Is:", bst.NR_Minimum())

print("\n------------\nDelete Minimum for root\n------------\n")
print("Delete Min has Done:", bst.R_DeleteMin(bst.root))
print(bst)

print("\n------------\nDelete Minimum for 13.00\n------------\n")
print("Delete Min has Done:", bst.R_DeleteMin(bst.root.left.right))
print(bst)

print("\n------------\nDelete 15.50\n------------\n")
bst.NR_Delete(bst.root.right.left)
print(bst)

# print("\n------------\nDelete 12\n------------\n")
# bst.NR_BST_Delete(bst.root.left)
# print(bst)

print("\n")




# (---)(---)(---)(---)(---)(---)(---)15.25(---)(---)(---)(---)(---)(---)(---)
# (---)(---)(---)12.25(---)(---)(---)(---)(---)(---)(---)13.25(---)(---)(---)
# (---)14.25(---)(---)(---)15.32(---)(---)(---)15.35(---)(---)(---)15.25(---)
# 12.20(---)14.25(---)15.32(---)15.32(---)15.32(---)15.32(---)15.32(---)15.25

# (---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)15.25(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)
# (---)(---)(---)(---)(---)(---)(---)13.25(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)12.25(---)(---)(---)(---)(---)(---)(---)
# (---)(---)(---)14.25(---)(---)(---)(---)(---)(---)(---)14.25(---)(---)(---)(---)(---)(---)(---)14.25(---)(---)(---)(---)(---)(---)(---)15.35(---)(---)(---)
# (---)12.20(---)(---)(---)12.20(---)(---)(---)12.20(---)(---)(---)12.20(---)(---)(---)12.20(---)(---)(---)12.20(---)(---)(---)14.25(---)(---)(---)15.32(---)
# 12.20(---)14.25(---)15.32(---)15.32(---)15.32(---)15.32(---)15.32(---)15.25(---)12.20(---)14.25(---)15.32(---)15.32(---)15.32(---)15.32(---)15.32(---)15.25