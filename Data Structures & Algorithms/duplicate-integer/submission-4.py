class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storage = set()
        for x in nums:
            if x in storage:
                return True
            storage.add(x)
        return False