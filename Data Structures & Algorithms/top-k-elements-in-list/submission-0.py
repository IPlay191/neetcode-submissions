class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        thisdict = {}
        freq = [[]for i in range(len(nums) + 1)]

        for number in nums:
                thisdict[number] = 1 + thisdict.get(number, 0)
        for count, number in thisdict.items():
            freq[number].append(count)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res