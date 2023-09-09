# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  

    def match(self, word_list):
        matches = []

        for test in word_list:
            test_lower = test.lower()

            if test_lower != self.word and sorted(test_lower) == sorted(self.word):
                matches.append(test)

        return matches

listen = Anagram("listen")
result = listen.match(['enlists', 'google', 'inlets', 'banana'])
print(result) 
