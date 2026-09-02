class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        for i, n in enumerate(nums):
            result = target - n
            if result in numbers:
                return [numbers[result], i]
            numbers[n] = i
        return
