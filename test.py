from nltk.book import*
text1
len(text1)
def percent(text,word):
  fdist=FreqDist(text)
  FreQ=fdist.freq(word)*100
  return FreQ
