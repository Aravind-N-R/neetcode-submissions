class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = len(nums)
        l1 = len(set(nums))
        if l != l1:
            return True
        return False