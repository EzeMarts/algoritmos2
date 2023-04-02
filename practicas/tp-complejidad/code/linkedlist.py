# 14169 Massacesi Juan Ignacio - 14000 Martins Ezequiel 

class LinkedList:
  head = None
class Node:
  value = None
  nextNode = None

def add(L, element):
  addNode = Node()
  addNode.value = element
  if L.head == None:
    L.head = addNode
  else:
    addNode.nextNode = L.head
    L.head = addNode

def addlast(L, element):
  addNode = Node()
  addNode.value = element
  if L.head == None:
    L.head = addNode
  else:
    currentNode = L.head
    while currentNode.nextNode != None:
      currentNode = currentNode.nextNode
    currentNode.nextNode = addNode

def search(L, element):
  currentNode = L.head
  cont = 0
  while currentNode != None:
    if currentNode.value == element:
      return cont
    cont += 1
    currentNode = currentNode.nextNode
  return None

def insert(L, element, position):
  insertNode = Node()
  insertNode.value = element
  currentNode = L.head
  cont = 0
  if position >= 0 and position <= length(L):
    while cont < position:
      cont += 1
      antNode = currentNode
      currentNode = currentNode.nextNode
    if position == 0:
      add(L, element)
      L.head.nextNode = currentNode
    else:
      insertNode.nextNode = antNode.nextNode            
      antNode.nextNode = insertNode
    return position
  return None

def delete(L, element):
  currentNode = L.head
  cont = 0
  antNode = currentNode
  while currentNode != None:
    if currentNode.value == element and cont!=0: 
      antNode.nextNode = currentNode.nextNode
      currentNode = None
      return cont
    elif currentNode.value == element and cont==0: ##
      L.head = antNode.nextNode
      antNode = None
      return cont
    else:
      cont += 1
      antNode = currentNode
      currentNode = currentNode.nextNode
  return None

def deletedir(L, direction):
  currentNode = L.head
  antNode = currentNode
  while currentNode != None:
    if currentNode == direction and currentNode != L.head:
      antNode.nextNode = currentNode.nextNode
      currentNode = None
      return direction.value
    elif currentNode == direction and currentNode == L.head:
      L.head = currentNode.nextNode
      return direction.value
    else:
      antNode = currentNode
      currentNode = currentNode.nextNode
  return None

def length(L):
  currentNode = L.head
  cont = 0
  while currentNode != None:
    cont += 1
    currentNode = currentNode.nextNode
  return cont

def access(L, position):
  currentNode = L.head
  cont = 0
  while currentNode != None:
    if position == cont:
      return currentNode.value
    cont += 1
    currentNode = currentNode.nextNode
  return None

def update(L, element, position):
  currentNode = L.head
  cont = 0
  while currentNode != None:
    if cont == position:
      currentNode.value = element
      return position
    cont += 1
    currentNode = currentNode.nextNode
  return None

def printlist(L):
  if L.head != None:
    currentNode = L.head
    print("[",currentNode.value, end="")
    while currentNode.nextNode != None:
      currentNode = currentNode.nextNode
      print(", ",currentNode.value, end="")
    print(" ]")