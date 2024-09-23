class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        bws = set(bannedWords)
        count = 0
        for msg in message:
            if msg in bws:
                count += 1
                if count >= 2:
                    return True
        return False