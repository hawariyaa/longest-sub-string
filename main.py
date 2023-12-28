# find the longest sub string from the given string with out repeating charagters
# remember a substring is contigous(side by side)
# for example: string = kebede   answer = bed
# SO for this we are going to use sets
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charset = set()
        l = 0
        result = 0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            result = max(result, r - l + 1)
        return result

string = "kebede"
answer = Solution()
outcome = answer.lengthOfLongestSubstring(string)
print(outcome)