vowel_list = ['a','e','i','o','u','A','E','I','O','U']
string = ["interesting", "aardvark", "aaa", "aeiouAEIOU", "a b c d e f g h i j k l m n o p q r s t u v w x y z", '']

class StringUtility:
    def __init__(self, string):
        self.string = string
    def __str__(self):
        return f"{self.string}"


    # def vowels(self, vowel):
    #     count = 0
    #     self.vowel = vowel
    #     for alphabet in string:
    #         if alphabet in vowel:
    #             count = count + 1
    #     print("No. of vowels :", count)

    def vowels(self):
        num_vowels=0
        for char in self:
            if char in "aeiouAEIOU":
                num_vowels = num_vowels+1
        if num_vowels < 5:
            return str(num_vowels)
        else:
           return "many"
        
    
    def bothEnds(self):
        if len(self) < 3:
            return ""
        else:
            return self[0] + self[1] + self[-2] + self[-1]

    def fixStart(self):
        if len(self) <=1:
            return self
        else:
            first_char = self[0]
            other_half = self[1:]
            return first_char + other_half.replace(first_char, "*")
  







    
