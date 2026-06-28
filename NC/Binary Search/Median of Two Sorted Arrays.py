class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_a, len_b = len(nums1), len(nums2)

        # Always binary search the smaller array
        if len_b < len_a:
            return self.findMedianSortedArrays(nums2, nums1)

        nums_a, nums_b = nums1, nums2

        left, right = 0, len_a

        # Total number of elements that should be in the left partition
        left_elements = (len_a + len_b + 1) // 2

        total_elements = len_a + len_b

        while left <= right:

            # Number of elements taken from A into the left partition
            mid_a = (left + right) // 2

            # Remaining elements must come from B
            mid_b = left_elements - mid_a

            # Rightmost element of the LEFT partition in A
            a_right = float('-inf') if mid_a == 0 else nums_a[mid_a - 1] # If nothing is on the left, treat it as -∞

            # Rightmost element of the LEFT partition in B
            b_right = float('-inf') if mid_b == 0 else nums_b[mid_b - 1] # If nothing is on the left, treat it as -∞

            # Leftmost element of the RIGHT partition in A
            a_left = float('inf') if mid_a == len_a else nums_a[mid_a] # If nothing is on the right, treat it as +∞

            # Leftmost element of the RIGHT partition in B
            b_left = float('inf') if mid_b == len_b else nums_b[mid_b] # If nothing is on the right, treat it as +∞

            # B contributed too many elements to the left partition.
            # We need to take more elements from A.
            if b_right > a_left:
                left = mid_a + 1

            # A contributed too many elements to the left partition.
            # We need to take fewer elements from A.
            elif a_right > b_left:
                right = mid_a - 1

            # Perfect partition found
            else:
                if total_elements % 2 == 0:
                    # Even length:
                    # median = average of largest left and smallest right
                    return (max(a_right, b_right) + min(a_left, b_left)) / 2

                # Odd length:
                # median = largest element in the left partition
                return max(a_right, b_right)

        return 0
    
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_a,len_b=len(nums1),len(nums2)
        if len_b<len_a:
            return self.findMedianSortedArrays(nums2, nums1)
        
        left,right=0,len_a
        left_elements=(len_a+len_b+1)//2
        total_elements=len_a+len_b
        
        while left<=right:
            mid_a=(left+right)//2
            mid_b=left_elements-mid_a

            a_right = float('-inf') if mid_a==0 else nums1[mid_a-1]
            b_right = float('-inf') if mid_b==0 else nums2[mid_b-1]
            a_left = float('inf') if mid_a==len_a else nums1[mid_a]
            b_left = float('inf') if mid_b==len_b else nums2[mid_b]

            if b_right > a_left:
                left=mid_a+1
            elif a_right>b_left:
                right=mid_a-1
            else:
                if total_elements%2==0:
                    return (max(a_right,b_right)+min(a_left,b_left))/2
                else:
                    return max(a_right,b_right)
            
        return 0
            
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lenA, lenB=len(nums1), len(nums2)
        if lenB<lenA:
            return self.findMedianSortedArrays(nums2,nums1)
        
        num_left_elements=(lenA+lenB+1)//2
        total_elements=lenA+lenB

        l,r=0,lenA
        while l<=r:
            mA=(l+r)//2
            mB=num_left_elements-mA

            aR=float('-inf') if mA==0 else nums1[mA-1]
            bR=float('-inf') if mB==0 else nums2[mB-1]
            aL=float('+inf') if mA==lenA else nums1[mA]
            bL=float('+inf') if mB==lenB else nums2[mB]

            if bR>aL:
                l=mA+1
            elif aR>bL:
                r=mA-1
            else:
                if total_elements%2==0:
                    return (max(aR,bR)+min(aL,bL))/2
                else:
                    return max(aR,bR)

        return 0 