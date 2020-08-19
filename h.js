function isValidBST(root, floor = -Infinity, ceil = Infinity) {
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



function solution(isBadVersion) {
    return function(n) {
      var left = 0;
      var right = n;
  
      while (right - left !== 1) {
        var mid = parseInt((left + right) / 2);
  
        if (isBadVersion(mid)) {
          right = mid;
        } else {
          left = mid;
        }
      }
      return right;
    };
}






function mergeSortedArrays(nums1, m, nums2, n) {
    while(n > 0){
        if(m <= 0 || nums2[n-1] >= nums1[m-1]){
            nums1[m+n-1] = nums2[n-1]
            n--
        } else {
            nums1[m+n-1] = nums1[m-1]
            m--
        }
    }
};




