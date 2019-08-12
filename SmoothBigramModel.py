import math, collections

class SmoothBigramModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # TODO your code here
    self.bigramCounts = collections.defaultdict(lambda:0)
    self.unigramCounts = collections.defaultdict(lambda:0)
    self.total = 0
    self.train(corpus)
    

  def train(self, corpus):
    """ 
    """  
    # TODO your code here
    start = '<s>'
    for sentence in corpus.corpus:
      for datum in sentence.data:
        token = datum.word
        bigram = (start, token)
        self.unigramCounts[token] = self.unigramCounts[token] + 1
        self.bigramCounts[bigram] = self.bigramCounts[bigram] + 1
        self.total += 1
        start = token
		
    pass

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    # TODO your code here
    score = 0.0
    start = '<s>'
    
    for token in sentence:
      bigram = (start, token)
      count = self.bigramCounts[bigram]
      length = len(self.bigramCounts)
      if count >= 0: 
        score += math.log(count+1)
        score -= math.log(self.unigramCounts[start] + length)
        start = token
      if start == '</s>':
        count = self.bigramCounts[bigram]
        length = len(self.bigramCounts)
        score += math.log(count+1)
        score -= math.log(self.unigramCounts[start] + length)

        
    
    return score

# unigram, plus bigram
