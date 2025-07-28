# given a root of a binary tre and the targert number check if the tree from its root (head) to the leaf node (means a node which have no childrens) when we sum this path
# and this path is equals to the target number , if by adding all the value of a single path in a tree are equals to the target value then return True if not find targtet value in any path
# then return False 


# for example 
# input = [1,9,5,7,8] , target = 9
# output = False 

# input = [1,2,4,5], target = 5
# ouytput = True (because trr.right side nodes are equals to the target value)

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left
        self.right = right 




def solution(tree : TreeNode, target):
    def sum_length_for_target(tree: TreeNode, target):
        if tree == None:
            return False

        if tree.val == target and tree.left == None and tree.right == None:
            return True 

        return sum_length_for_target(tree.left, target - tree.val) or sum_length_for_target(tree.right, target - tree.val) 


    return sum_length_for_target(tree , target) 
        
        

        

tree = TreeNode(1)
tree.left = TreeNode(9)
tree.right = TreeNode(5) 


tree.left.left = TreeNode(7)
tree.left.right = TreeNode(8)

target = 18


s = solution(tree , target)
print(s)