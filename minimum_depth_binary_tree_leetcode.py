# given a binary tree return its minimum length (shortest path from the head not) 
# note leaf is a node with no children 

# for example 
# input = [3,9,20,null,null,15,7] 
# output = 2  because (3 and 9 are the shortest length or root which make shortest length 2)

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 


def solution(tree : TreeNode):
    def minimum_tree_length(tree : TreeNode):
        if tree == None:
            return 0 
        
        elif tree.left == None and tree.right == None:
            return 1 
         
        elif tree.left == None and tree.right != None:
            return minimum_tree_length(tree.right) + 1
        
        elif tree.left != None and tree.right == None:
            return minimum_tree_length(tree.left) + 1 
        
        else:
            m = min(minimum_tree_length(tree.left), minimum_tree_length(tree.right))
            return m + 1


    return minimum_tree_length(tree)





tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)

tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7) 


s = solution(tree)
print(s)

