from trie import *

def capicuaTrie(T, word):
  wordCapicua = ""
  wordTemp = word
  while len(wordTemp) > 0:
    wordCapicua = wordTemp[0:1] + wordCapicua
    wordTemp = wordTemp[1:len(wordTemp)]
  print(wordCapicua)
  valid1 = search(T, word)
  valid2 = search(T, wordCapicua)
  if valid1 and valid2:
    return True
  else:
    return False