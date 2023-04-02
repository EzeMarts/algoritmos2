from linkedlist import *

def ContieneSuma(L, n):
  mainNode = L.head
  loopNode = mainNode.nextNode
  for i in range(0, length(L)-1):
    for j in range(i+1, length(L)):
      if mainNode.value + loopNode.value == n:
        return True
      loopNode = loopNode.nextNode
    mainNode = mainNode.nextNode
    loopNode = mainNode.nextNode
  return False