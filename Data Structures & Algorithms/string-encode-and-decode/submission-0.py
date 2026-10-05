class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        res = []
        for s in strs:
            # Format: <length> + <delimiter> + <string>
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Find the delimiter '#' to read the full length number
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            # Extract the actual string using the length
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # Move the pointer past the extracted string
            i = end
            
        return res
