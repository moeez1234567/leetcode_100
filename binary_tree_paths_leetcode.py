# given a binary tree , return its nodes values upto leaf node with the arrow in the path values 
# for example input = [1,2,3,None,5,None,None]
# output = [1->2->5, 1->3]


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 



def solution(tree : TreeNode, path):
    l = []
    def tree_path(tree : TreeNode, path):
        if not tree:
            return None 
        
        if path:
            path += "->" + str(tree.val)
        else: 
            path += str(tree.val)

        
        if not tree.left and not tree.right:
            l.append(path)
        
        tree_path(tree.left, path)
        tree_path(tree.right, path) 

        

        return l
        
    
    

    return tree_path(tree, path="")    


tree = TreeNode(4)
tree.left = TreeNode(8)
tree.right = TreeNode(12)


tree.left.left = TreeNode(16)
tree.left.right = TreeNode(13) 

path = ""
s = solution(tree, path)
print(s)



# another way to do that 
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right  



def salution(tree):
    lst = []

    if tree == None:
        return []
    
    if not tree.left and not tree.right:
        return [str(tree.val)] 
    
    for leftc in salution(tree.left):
        lst.append(str(tree.val) + '->' + leftc)

    for rightc in salution(tree.right):
        lst.append(str(tree.val) + '->' + rightc)

    return lst    
    


tree = TreeNode(4)
tree.left = TreeNode(8)
tree.right = TreeNode(12)


tree.left.left = TreeNode(16)
tree.left.right = TreeNode(13) 

s = salution(tree)