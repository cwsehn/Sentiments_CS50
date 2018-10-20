import nltk
from nltk.tokenize import TweetTokenizer

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""

        with open(positives) as file:
            lines = file.readlines()
            self.positives = []
            for s in lines:
                s.strip()
                if s[0].isalpha():
                    self.positives.append(s.strip('\n'))
                    
        with open(negatives) as file:
            lines = file.readlines()
            self.negatives = []
            for s in lines:
                s.strip()
                if s[0].isalpha():
                    self.negatives.append(s.strip('\n'))



    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        # assign each word in text a value (-1, 0, or 1)
        score = 0
        tknzr = TweetTokenizer()
        tokens = tknzr.tokenize(text)
        
        # print(tokens) ...testing purposes only...
        for token in tokens:
            if token.lower() in self.positives:
                score += 1
                continue
            elif token.lower() in self.negatives:
                score -= 1
                continue
            
        return score
