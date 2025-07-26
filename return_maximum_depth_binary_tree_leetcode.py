# Given a binary tree , return its maximum depth from its head , means you have a head of binary tre try to catch the maximum length of last node in this tree 
# for example tree.left.right tree.left in this case tree.left.right have the maximum length 

# input = [1,2,null,2,3] 
# output = 4 

# input = [3,4,5,6,7]

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 


def solution(tree):
    def maximum_tree(tree : TreeNode):
        if not tree:
            return 0
        if tree.left == None and tree.right == None:
            return 1 
        elif tree.left == None and tree.right != None:
            mx = maximum_tree(tree.right) + 1 
            return mx 
        elif tree.left != None and tree.right == None:
            mx = maximum_tree(tree.left) + 1 
            return mx 
        
        else:
            mx = max(maximum_tree(tree.left) , maximum_tree(tree.right))
            mx += 1
            return mx 
        
    return maximum_tree(tree)
             

    



# making tree 
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)

tree.left.left = TreeNode(2)
tree.right.left = TreeNode(2)
tree.left.left.right = TreeNode(3)
tree.right.left.right = TreeNode(3)
tree.right.left.right.right = TreeNode(4)




mt = solution(tree)
print(mt)