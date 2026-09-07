class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = defaultdict(list)
        for current in strs:
            count = [0] * 26

            for char in current:
                count[ord(char) - ord("a")] += 1

            hashtable[tuple(count)].append(current)
            
        return list(hashtable.values())
            