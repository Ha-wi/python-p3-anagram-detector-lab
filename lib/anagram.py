# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    def match(self, list):
        return [w for w in list if self.word != w and sorted(self.word) == sorted(w)]