from trie import *

def patronTrie(T, letter, long): # Esta planteado, error con el .index y .count
  if T.root == None or letter == "" or long == 0:
    return None
  L = []
  letter = letter.upper() # Hacer mayuscula
  if T.root.children.count(letter) > 0:
    i = T.root.children.index(letter)
    patronTrieR(T.root.children[i], L, letter, 2, long)
    print(L)
  else:
    return None
def patronTrieR(nodeL, L, word, level, longLevel):
  if level == longLevel:
    for i in range(0, len(nodeL)):
      if nodeL[i].isEndOfWord:
        wordTemp = word + nodeL[i].key
        L.append(wordTemp)
        return
  else:
    for i in range(0, len(nodeL)):
      wordTemp = word + nodeL[i].key
      if nodeL[i].children != None:
        patronTrieR(nodeL[i].children, L, wordTemp, level+1, longLevel)