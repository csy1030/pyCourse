class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 1
        if not s:
            return 0
        substr = []
        part = []
        for item in s:
            if item not in part:
                part.append(item)
            else:
                substr.append(part)
                part = []
                part.append(item)
        if part:
            substr.append(part)

        max_len = 0
        for item in substr:
            if max_len < len(item):
                max_len = len(item)
        return max_len


s = Solution()
print(s.lengthOfLongestSubstring("c"))