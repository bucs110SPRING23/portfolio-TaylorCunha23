#vowel_list = ['a','e','i','o','u','A','E','I','O','U']
#string = ["interesting", "aardvark", "aaa", "aeiouAEIOU", "a b c d e f g h i j k l m n o p q r s t u v w x y z", '']

class StringUtility:
    def __init__(self, string):
        self.string = string
    def __str__(self):
        return f"{self.string}"

    def vowels(self):
        num_vowels = 0
        for char in self.string:
            if char in "aeiouAEIOU":
                num_vowels = num_vowels+1
        if num_vowels < 5:
            return str(num_vowels)
        else:
           return "many"
        
    def bothEnds(self):
        if len(self.string) < 3:
            return ""
        else:
            return self.string[0] + self.string[1] + self.string[-2] + self.string[-1]

    def fixStart(self):
        if len(self.string) <=1:
            return self.string
        else:
            first_char = self.string[0]
            other_half = self.string[1:]
            return first_char + other_half.replace(first_char, "*")

    def asciiSum(self):
        total = 0
        for char in self.string:
            val = ord(char)
            total += val
        return total

    # def cipher(self):
    #     shift = len(self.string)
    #     cipherText = ""
    #     for char in self.string:
    #         letter = ord(char)
    #         if char.isalpha():
    #             alphabet = ord(char) + shift 
    #             alphabet %= 26
    #             # if alphabet > ord('z'):
    #             #     alphabet -= 26
    #             changed_letter = chr(alphabet)
    #             cipherText += changed_letter
    #     return cipherText

    # def cipher(self):
    #     lowercase = string.ascii_lowercase
    #     uppercase = string.ascii_uppercase
    #     result = ""
    #     for char in self.string:
    #         if char.islower():
    #             index = lowercase.index(char)
    #             result += lowercase[(index + shift) % 26]
    #         else:
    #             index = uppercase.index(char)
    #             result += uppercase[(index + shift) % 26]







  








    
