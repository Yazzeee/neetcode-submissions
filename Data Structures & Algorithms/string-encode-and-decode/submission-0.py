class Solution:

    def encode(self, strs: List[str]) -> str:
        output_string = ""
        for string in strs:
            for char in string:
                output_string += str(ord(char)) + ","
            output_string += "!"
        return output_string

    def decode(self, s: str) -> List[str]:
        strs = []
        current_word = ""
        current_char = ""
        for i in range(len(s)):
            char = s[i]
            if char == "!":
                strs.append(current_word)
                current_word = ""
                current_char = ""
            elif char == ",":
                current_word += chr(int(current_char))
                current_char = ""
            else:
                current_char += char
        return strs
            

