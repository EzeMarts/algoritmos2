class Trie:
  root = None

class TrieNode:
  parent = None
  children = None
  key = None
  isEndOfWord = False

# https://docs.python.org/3/tutorial/datastructures.html
def insert(T, element):
  if element == "":
    return None
  element = element.upper() # Hacer mayuscula
  if T.root == None:
    rootNode = TrieNode()
    T.root = rootNode
    newNode = TrieNode()
    newNode.key = element[0:1] # Darle de key la 1ra letra
    element = element[1: len(element)] # Cortar la cadena
    newList = []
    newList.append(newNode)
    rootNode.isEndOfWord = True
    rootNode.children = newList
    newNode.parent = rootNode
    if element == "":
      newNode.isEndOfWord = True
      return
    lowerList = []
    newNode.children = lowerList
    insertR(lowerList, element, newNode)
  else:
    insertR(T.root.children, element, T.root.children[0])
def insertR(L, element, parentNode):
  i = 0
  while i < len(L) and L[i].key != element[0]:
    i =+ 1
  if i == len(L):
    newNode = TrieNode()
    newNode.parent = parentNode # Darle el nodo superior como parent
    newNode.key = element[0:1] # Darle de key la 1ra letra
    L.append(newNode)
    lowerList = []
    newNode.children = lowerList
    element = element[1: len(element)] # Cortar la cadena
    if element == "":
      newNode.isEndOfWord = True
      return
    else:
      insertR(lowerList, element, newNode)
  else:
    element = element[1: len(element)] # Cortar la cadena
    if element == "":
      L[i].isEndOfWord = True
      return
    else:
      insertR(L[i].children, element, L[i])

def search(T, element):
  if T.root == None or element == "":
    return None
  else:
    element = element.upper()
    return searchR(T.root.children, element)
def searchR(L, element):
  i = 0
  while i < len(L) and L[i].key != element[0]:
    i =+ 1
  if i == len(L):
    return False
  else:
    element = element[1: len(element)] # Cortar la cadena
    if element == "" and L[i].isEndOfWord:
      return True
    elif element == "" and L[i].isEndOfWord == False:
      return False
    else:
      return searchR(L[i].children, element)

def delete(T, element):
  element = element.upper()
  wordExist = search(T, element)
  if wordExist:
    print("entre a existe")########################
    return deleteR(T.root.children, element)
  else:
    print("entre a NO existe")##############
    return False
def deleteR(L, element):
  i = 0
  while L[i].key != element[0]:
    i =+ 1
  element = element[1: len(element)] # Cortar la cadena
  if element == "":
    if len(L[i].children) == 0:
      upNode = L[i].parent
      letter = L[i].key
      while upNode.isEndOfWord != True and len(upNode.children) == 1:
        upNode = upNode.parent
        letter = upNode.key
      print(letter)
      print(upNode.key)
      print(upNode.parent.children[0].key)
      upNode.parent.children.remove(letter)
      return True
    else:
      L[i].isEndOfWord = False
      return True
  return deleteR(L[i].children, element)