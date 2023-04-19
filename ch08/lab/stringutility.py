vowel_list = ['a','e','i','o','u','A','E','I','O','U']
string = ["interesting", "aardvark", "aaa", "aeiouAEIOU", "a b c d e f g h i j k l m n o p q r s t u v w x y z", '']

class StringUtility:
    def __init__(self, string):
        self.string = string
    def __str__(self):
        return f"{self.string}"

    def vowels(self):
        count = 0
        vowel = set("aeiouAEIOU")
        for alphabet in string:
            if alphabet in vowel:
                count = count + 1
        print("No. of vowels :", count)






    
