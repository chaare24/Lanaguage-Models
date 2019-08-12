import math, collections

class BackoffModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # TODO your code here
    self.unigramCounts = collections.defaultdict(lambda:0)
    self.bigramCounts = collections.defaultdict(lambda:0)
    self.total = 0
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    # TODO your code here
    # copied from SmoothBigramModel
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
    # SBM score function implemented with unigram
    score = 0.0
    start = '<s>'
    for token in sentence:
      bigram = (start, token)
      bi_count = self.bigramCounts[(start,token)]
      uni_length = len(self.unigramCounts)
      if bi_count > 0:
          score += math.log(bi_count)
          score -= math.log(self.unigramCounts[start])
          start = token
      else:
          score += math.log(self.unigramCounts[token]+1)
          score += math.log(0.4) 
          score -= math.log(self.total + uni_length)
          start = token


    return score
