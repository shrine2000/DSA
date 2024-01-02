class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        words[0] = words[0].lower()  # Convert the first word to lowercase
        words.sort(key=len)  # Sort the words based on their lengths

        # Capitalize the first letter of the first word
        words[0] = words[0][0].upper() + words[0][1:]

        return " ".join(words)
