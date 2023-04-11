# https://docs.google.com/document/d/16boitAloCwJJm6kn3cQIBsmgspC9eiQCJ4Q7ATpqOSg/edit
# https://docs.python.org/3/tutorial/datastructures.html
class Trie:
  root = None

class TrieNode:
  parent = None
  children = None
  key = None
  isEndOfWord = False

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
    
def delete(T, element): # Optimizar
  if T.root == None or element == "":
    return None
  else:
    element = element.upper()
    if searchR(T.root.children, element):
      deleteR(T.root.children, element)
      return True
    else:
      return False
def deleteR(L, element): # Optimizar
  i = 0
  while i < len(L) and L[i].key != element[0]:
    i =+ 1
  if i == len(L):
    return False
  else:
    element = element[1: len(element)] # Cortar la cadena
    if element == "" and L[i].isEndOfWord:
      if len(L[i].children) > 0:
        L[i].isEndOfWord = False
        return True
      return deleteUnlink(L[i].parent, L[i])
    elif element == "" and L[i].isEndOfWord == False:
      return False
    else:
      return deleteR(L[i].children, element)

def deleteUnlink(node, lowNode):
  if node.isEndOfWord:
    if len(node.children) > 1:
      node.children.remove(lowNode)
      return True
    else:
      node.children = None
      return True
  elif len(node.children) > 1:
    node.children.remove(lowNode)
    return True
  else:
    return deleteUnlink(node.parent, node)