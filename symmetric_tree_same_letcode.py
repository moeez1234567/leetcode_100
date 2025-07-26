# given a binary tree checks that from the half of the tree means from the head the tree itself is symmetric means there left part is the mirror of its right part means same structure and 
# node value 

# for example 
# tree = [1,2,2,3,4,4,3]
# output = True 

# tree = [1,2,null,3 , 3 , null]
# output = False 


class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left= left 
        self.right = right


def solution(tree):
    def symmetric_tree(a, b):
        if a == None and b == None:
            return True 

        if a == None or b == None:
            return False 
        
        return (a.val == b.val) and  symmetric_tree(a.left , b.left) and symmetric_tree(a.right , b.right)

    # if a.right != b.right:
    #     return False

    return symmetric_tree(a , b)

        








# lavel 1 of tree
a = TreeNode(2)
b = TreeNode(2)

# lavel 2 of tree
a.left = TreeNode(3)
a.right = TreeNode(4)

# lavel 3 of tree
b.left = TreeNode(3)
b.right = TreeNode(4) 


tree = TreeNode(1, a , b)


st = solution(tree)
print(st)








    