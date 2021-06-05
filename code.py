class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        mid=(left+right)//2
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                if mid==len(nums)-1:
                    return mid+1
                elif nums[mid+1]>target:
                    return mid+1
                else:
                    left=mid+1
            else:
                if mid==0:
                    return 0
                elif nums[mid-1]<target:
                    return mid
                else:
                    right=mid-1
        return -1
