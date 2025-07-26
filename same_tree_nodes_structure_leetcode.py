# you have given 2 trees head p and q you check the structure and the nodes binary number in this place is same or not if same structure of p and q and in this structure their p and q values are same
#  then return the True if there structure and the values in the structure is not same then returns the false 

# for example p = [1,2,3] , q = [1,3,2]
# false 

# p = [3,2,1] , q = [3,2,1]
# true 


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left 
        self.right = right 



def solution( p : TreeNode, q : TreeNode):
    if not p and not q:
        return True 
    
    if not p or not q:
        return False 
    
    if p.val != q.val:
        return False 
    
    return solution(p.left, q.left) and solution(p.right , q.right)



tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)


tree2 = TreeNode(1)
tree2.left  = TreeNode(2)
tree2.right = TreeNode(2)



s = solution(tree1 , tree2)
print(s)