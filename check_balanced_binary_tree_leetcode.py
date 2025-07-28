# given a binary tree checks its length is equals from both from left and right node 
# (if its exceed from left or right side expamd just just 1 node then also return True else False if the height of both sides are mismatch)
# for example input = [0,1,5,2,5,None,8]
# output = True 

# input = [0, 3, 4, 5, 6, None, None, 4, 5]
# output = False 

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 

def solution(tree : TreeNode):
    def check_length_tree(tree : TreeNode):
        if tree == None:
            return 0 

        print(f"Visiting Node: {tree.val}")
    
        l = check_length_tree(tree.left)
        r = check_length_tree(tree.right)

        print(f"At Node {tree.val} → Left Height: {l}, Right Height: {r}")

        if (l == -1 or r == -1 or abs(l - r) > 1):
            print(f"Node {tree.val} is unbalanced")
            return -1 

        return 1 + max(l, r) 
    
    return check_length_tree(tree)
    

    
    



tree = TreeNode(0)
tree.left = TreeNode(1)
tree.right = TreeNode(5)


tree.left.left = TreeNode(2)
tree.left.right = TreeNode(5)

# tree.right.left(None)
tree.right.right = TreeNode(8)






cla = solution(tree)
print(cla)




