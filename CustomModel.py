import math, collections
class CustomModel:

#Copied Backoff Model class and going to try and increase accuracy
#attempt for trigram
  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # TODO your code here
    self.unigramCounts = collections.defaultdict(lambda:0)
    self.bigramCounts = collections.defaultdict(lambda:0)
    self.trigramCounts = collections.defaultdict(lambda:0)
    self.total = 0
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    # TODO your code here
    # copied from SmoothBigramModel

    for sentence in corpus.corpus:
      tok = '@NaN'
      start = '<s>'
      token = '@NaN'
      self.unigramCounts[start] = self.unigramCounts[start] + 1
      self.total += 1
      for datum in sentence.data:
          token = datum.word
          bigram = (start, token)
          trigram = (start, token, tok)
          self.unigramCounts[token] = self.unigramCounts[token] + 1
          self.bigramCounts[bigram] = self.bigramCounts[bigram] + 1
          
          if tok != '@NaN':
             self.trigramCounts[trigram] = self.trigramCounts[trigram] + 1 
          self.total += 1
          tok = start
          start = token
		
    pass


  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    # TODO your code here
    # SBM score function implemented with unigram
    # trigram 
    score = 0.0
    tok = '@NaN'
    start = '<s>'
    nextchar = '@NaN'
    count = self.unigramCounts[nextchar]
    for token in sentence:
      bigram = (start, token)
      trigram = (start, token, tok)
      bi_count = self.bigramCounts[(start,token)]
      tri_count = self.trigramCounts[(start, token, tok)]
      uni_length = len(self.unigramCounts)
      if bi_count > 0: #bigram
          score += math.log(bi_count)
          score -= math.log(self.unigramCounts[start])
          tok = start
          start = token
      elif tri_count > 0: #trigram
          score += math.log(tri_count)
          score -= math.log(self.bigramCounts[bigram])
          tok = start
          start = token
      else:
          score += math.log(self.unigramCounts[token]+0.2)
          score += math.log(0.05) 
          score -= math.log(self.total + uni_length)
          tok = start
          start = token


    return score
