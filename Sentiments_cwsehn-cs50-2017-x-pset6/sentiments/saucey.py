import os
import sys

from analyzer import Analyzer



# absolute paths to lists
positives = os.path.join(sys.path[0], "positive-words.txt")
negatives = os.path.join(sys.path[0], "negative-words.txt")

# instantiate analyzer
analyzer = Analyzer(positives, negatives)

print(analyzer.positives)
print(analyzer.negatives)