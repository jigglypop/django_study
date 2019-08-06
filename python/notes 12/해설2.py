class Word:
    def __init__(self):
        self.wordbook = {}
    def add(self, eng, kor):
        self.wordbook[eng] = kor
        
    def delefe(self, eng):
        if eng in self.wordbook:
