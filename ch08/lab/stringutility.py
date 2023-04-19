class StringUtility:
    def __init__(self, string, vowels):
        self.string = string
        self.vowels = vowels
    def __str__(self):
        return f"{self.string}{self.vowels}"

    
