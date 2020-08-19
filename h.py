def isValidBst(root, floor=None, ceil=None):
    if floor is None and ceil is None:
        floor = float('-inf')
        ceil = float(inf)
    
    if not root:
        return True
    if floor >= root.val or ceil <= root.val:
        return False
    newFloor = max(floor, root.val)
    newCeil = min(ceil, root.val)

    if isValidBST(root.left, floor, newCeil) and isValidBST(root.right, newFloor, ceil):
        return True
    else:
        return False



var isValidBST = function(root, floor = -Infinity, ceil = Infinity) {
    if(!root){
        return true
    }
    if(floor >= root.val || root.val >= ceil){
        return false
    }
    const newFloor = Math.max(floor, root.val)
    const newCeil = Math.min(ceil, root.val)
    
    if(isValidBST(root.left, floor, newCeil) && isValidBST(root.right, newFloor, ceil)){
        return true
    } else {
        return false
    }
}

