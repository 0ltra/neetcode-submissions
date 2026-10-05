class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Loop through each character of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            # Check this character against all other strings
            for string in strs[1:]:
                # If the string is shorter or the character doesn't match
                if i >= len(string) or string[i] != char:
                    return strs[0][:i]
                    
        return strs[0]
