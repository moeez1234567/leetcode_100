# given a sorted nums in array you return a binary tree with balanced by its height means that its left or the right side nodes dont expand to the 1  
# 
# for example input =  [-10, -2, 0, 5, 9]
# output = [0,-2,5,-10,9]

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 


def balanced_height(array : TreeNode):
    middle = len(array) // 2 
    tree = TreeNode(val = array[middle])
    tree.left = TreeNode(array[:middle])
    tree.right = TreeNode(array[middle + 1:])

    return tree 



b = balanced_height([-10,-2,0,5,9])
print(b)


print(b.val)
print(b.left.val)
print(b.right.val)











        
