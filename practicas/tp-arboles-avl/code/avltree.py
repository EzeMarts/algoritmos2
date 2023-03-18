class AVLTree:
  root = None

class AVLNode:
  parent = None
  leftnode = None
  rightnode = None
  key = None
  value = None
  bf = None

# Ejercicio 1
def rotateLeft(Tree, AVLnode):
  nodeA = AVLnode
  nodeB = nodeA.rightnode
  nodeA.rightnode = nodeB.leftnode
  if nodeB.leftnode != None:
    nodeB.leftnode.parent = nodeA
  nodeB.parent = nodeA.parent
  if nodeA.parent == None:
    Tree.root = nodeB
  elif nodeA == nodeA.parent.leftnode:
    nodeA.parent.leftnode = nodeB
  else:
    nodeA.parent.rightnode = nodeB
  nodeB.leftnode = nodeA
  nodeA.parent = nodeB
  return Tree.root
def rotateRight(Tree, AVLnode):
  nodeA = AVLnode
  nodeB = nodeA.leftnode
  nodeA.leftnode = nodeB.rightnode
  if nodeB.rightnode != None:
    nodeB.rightnode.parent = nodeA
  nodeB.parent = nodeA.parent
  if nodeA.parent == None:
    Tree.root = nodeB
  elif nodeA == nodeA.parent.rightnode:
    nodeA.parent.rightnode = nodeB
  else:
    nodeA.parent.leftnode = nodeB
  nodeB.rightnode = nodeA
  nodeA.parent = nodeB
  return Tree.root

# Ejercicio 2
def calculateBalance(AVLTree):
  if AVLTree.root == None:
    return None
  calculateBalanceR(AVLTree.root)
  return AVLTree
def calculateBalanceR(Node):
  if Node == None:
    return
  Node.bf = height(Node.leftnode) - height(Node.rightnode)
  calculateBalanceR(Node.leftnode)
  calculateBalanceR(Node.rightnode)
  return
# Ejercicio Opcional 1 - Es de O(log n) porque la altura se obtiene al dividir el árbol en dos hasta llegar al nodo hoja
def height(Node):
  if Node == None:
    return 0
  hleft = height(Node.leftnode)
  hright = height(Node.rightnode)
  h = max(hleft, hright) + 1
  return h
  
# Ejercicio 3
def reBalance(AVLTree):
  if AVLTree.root == None:
    return None
  calculateBalance(AVLTree)
  while AVLTree.root.bf < -1 or AVLTree.root.bf > 1:
    reBalanceR(AVLTree, AVLTree.root)
  return
def reBalanceR(AVLTree, Node):
  if Node.bf >= -1 and Node.bf <= 1:
    holdNode = Node.parent
    if Node.parent == None:
      return
    if holdNode.bf < 0:
      if holdNode.rightnode.bf > 0:
        rotateRight(AVLTree, holdNode.rightnode)
        rotateLeft(AVLTree, holdNode)
      else:
        rotateLeft(AVLTree, holdNode)
    elif holdNode.bf > 0:
      if holdNode.leftnode.bf < 0:
        rotateLeft(AVLTree, holdNode.leftnode)
        rotateRight(AVLTree, holdNode)
      else:
        rotateRight(AVLTree, holdNode)
    calculateBalance(AVLTree)
    return
  else:
    if Node.bf > 1:
      reBalanceR(AVLTree, Node.leftnode)
    else:
      reBalanceR(AVLTree, Node.rightnode)
  return

# Ejercicio 4-5
def insert(AVLTree, value, key):  # Inserta un nodo con value y key
  newNode = AVLNode()
  newNode.key = key
  newNode.value = value
  NodeA = None
  NodeB = AVLTree.root
  while NodeB != None:
    NodeA = NodeB
    if newNode.key < NodeB.key:
      NodeB = NodeB.leftnode
    else:
      NodeB = NodeB.rightnode
  newNode.parent = NodeA
  if NodeA == None:
    AVLTree.root = newNode
  elif newNode.key < NodeA.key:
    NodeA.leftnode = newNode
  else:
    NodeA.rightnode = newNode
  reBalance(AVLTree)
  return

def delete(AVLTree, value):  # Elimina un nodo por su value y devuelve
  Node = AVLTree.root
  if Node == None:
    return None
  while Node.value != value:
    if Node.value > value:
      Node = Node.leftnode
    else:
      Node = Node.rightnode
    if Node == None:
      return None
  if Node.leftnode == None:
    rearrangeTree(AVLTree, Node, Node.rightnode)
  elif Node.rightnode == None:
    rearrangeTree(AVLTree, Node, Node.leftnode)
  else:
    newNode = minNode(Node.rightnode)
    if newNode.parent != Node:
      rearrangeTree(AVLTree, newNode, newNode.rightnode)
      newNode.rightnode = Node.rightnode
      newNode.rightnode.parent = newNode
    rearrangeTree(AVLTree, Node, newNode)
    newNode.leftnode = Node.leftnode
    newNode.leftnode.parent = newNode
  reBalance(AVLTree)
  return Node.key
def rearrangeTree(AVLTree, NodeA, NodeB):
  if NodeA.parent == None:
    AVLTree.root = NodeB
  elif NodeA == NodeA.parent.leftnode:
    NodeA.parent.leftnode = NodeB
  else:
    NodeA.parent.rightnode = NodeB
  if NodeB != None:
    NodeB.parent = NodeA.parent
  return
def minNode(Node):
  while Node.leftnode != None:
    Node = Node.leftnode
  return Node
def maxNode(Node):
  while Node.rightnode != None:
    Node = Node.rightnode
  return Node

def search(AVLTree, value):  # Busca un nodo por su value y devuelve key
  if AVLTree.root == None:
    return None
  key = searchR(AVLTree.root, value)
  return key
def searchR(Node, value):
  if Node == None:
    return None
  if Node.value == value:
    return Node.key
  key = searchR(Node.leftnode, value)
  if key == None:
    key = searchR(Node.rightnode, value)
  return key

def access(AVLTree, key):  # Busca un nodo por su key y devuelve value
  Node = accessR(AVLTree.root, key)
  if Node == None:
    return None
  return Node.value
def accessR(Node, key):
  if Node == None or Node.key == key:
    return Node
  if Node.key < key:
    return accessR(Node.rightnode, key)
  return accessR(Node.leftnode, key)
def searchKey(AVLTree, key):  # Busca un nodo por su value y devuelve la dirección
  Node = accessR(AVLTree.root, key)
  if Node == None:
    return None
  return Node

def update(AVLTree, value, key):  # Edita el value de un nodo por su key
  Node = searchKey(AVLTree, key)
  if Node == None:
    return None
  Node.value = value
  return Node.key