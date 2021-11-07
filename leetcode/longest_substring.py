# 7/11/2021

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Input: s = ""
# Output: 0


#     def lengthOfLongestSubstring(self, s: str) -> int:
my approach   will work for 3 usecases, will miss on 1 usecase.
#         count = 0
#         add_list = []
#         for i in range(len(s)):
#             if s[i] not in add_list:
#                 add_list.append(s[i])
#                 count+= 1
#         return count        
                # print("s[i]", s[i])
                
 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mem = {} # dictionary to keep last idx of 'char'
        last_idx, max_length = 0, 0
        for i in range(len(s)): 
            if s[i] in mem and mem[s[i]]>=last_idx:
                last_idx = mem[s[i]]+1
            mem[s[i]]=i
            max_length = max(max_length, i-last_idx+1)
        return max_length
      
      
# Start with having a dictionary to keep last_idx of 'char' occurance.
# Loop thorugh each char in string, and update the last_idx of char occurance.
# Max length found by taking the maximum substraction result of current index and last_idx occurance (+1 because length take base-1 form)      
