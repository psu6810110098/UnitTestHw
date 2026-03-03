# src/challenges.py

# --- EXTRA CREDIT STUB SETUP ---
class StringProvider:
    def fetch_data(self) -> str:
        raise NotImplementedError("Real implementation connects to API")

class CharacterService:
    def __init__(self, provider: StringProvider):
        self.provider = provider
        
    def process_alternating(self) -> int:
        s = self.provider.fetch_data()
        return alternatingCharacters(s)

# --- HACKERRANK LOGIC ---

def funnyString(s):
    r = s[::-1]
    for i in range(1, len(s)):
        diff1 = abs(ord(s[i]) - ord(s[i-1]))
        diff2 = abs(ord(r[i]) - ord(r[i-1]))
        if diff1 != diff2:
            return "Not Funny"
    return "Funny"

def alternatingCharacters(s):
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            deletions += 1
    return deletions

def caesarCipher(s, k):
    k = k % 26
    result = []
    for char in s:
        if char.islower():
            result.append(chr((ord(char) - ord('a') + k) % 26 + ord('a')))
        elif char.isupper():
            result.append(chr((ord(char) - ord('A') + k) % 26 + ord('A')))
        else:
            result.append(char)
    return "".join(result)

def alternate(s):
    chars = list(set(s))
    max_len = 0
    for i in range(len(chars)):
        for j in range(i + 1, len(chars)):
            c1, c2 = chars[i], chars[j]
            filtered = [c for c in s if c == c1 or c == c2]
            
            valid = True
            for k in range(1, len(filtered)):
                if filtered[k] == filtered[k-1]:
                    valid = False
                    break
                    
            if valid:
                max_len = max(max_len, len(filtered))
    return max_len

def gridChallenge(grid):
    sorted_grid = [sorted(list(row)) for row in grid]
    rows = len(sorted_grid)
    cols = len(sorted_grid[0])
    
    for c in range(cols):
        for r in range(1, rows):
            if sorted_grid[r][c] < sorted_grid[r-1][c]:
                return "NO"
    return "YES"