with open('ps.txt') as file:
        lines = file.readlines()
        pos = []
        for s in lines:
            s.strip()
            if s[0].isalpha():
                pos.append(s.strip('\n'))
                
                
        # assign each word in text a value (-1, 0, or 1)
        score = 0
        tknzr = TweetTokenizer()
        tokens = tknzr.tokenize(text)
        
        for token in tokens:
            if token.lower() in self.positives:
                score += 1
                continue
            elif token.lower() in self.negatives:
                score -= 1
                continue
            
        return score
        
        
        if text.lower() in self.positives:
            score += 1
            return score
                
        elif text.lower() in self.negatives:
            score -= 1
            return score