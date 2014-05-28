__author__ = 'gt'
from pprint import pprint

from gt.sbu.so.ft_extraction import get_features


def get_lemma_vn_unigram(sents):
  pass



def test_features():
  corpus = [
    'This is the first document. #BLOCK# Second sentence looks interesting',
    'This is the second second document.     #BLOCK# Testing',
    'And the third one.     #BLOCK# Does it work',
    'Is this the first document ?     #BLOCK# Yes it does',
  ]
  vec, X = get_features(corpus)

  print vec.get_params()
  print vec.get_feature_names()
  pprint(X.todense())

def main():
  test_features()


if __name__ == '__main__':
  main()
  print '#############'
