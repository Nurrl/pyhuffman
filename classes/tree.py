from classes.bintree import BinTree
from classes.bitarray import BitArray

class Tree:
  def __init__(self, string, tree = None):
    self.bytes = '';

    # Recover tree from compressed tree binary
    if tree:
      treebin = BitArray.from_bytes(tree)
      self.tree = self.from_binary(treebin)[1]
    else:
      weights = self._getweight(string)

      # Generate binary tree from weights
      while len(weights) > 1:
        left = weights.pop(-1)
        right = weights.pop(-1)
        if type(left) is not BinTree:
          left = BinTree(left, None, None)
        if type(right) is not BinTree:
          right = BinTree(right, None, None)

        weights = [BinTree(None, left, right)] + weights

      self.tree = BinTree(None, BinTree('\0', None, None), weights[0])

  def from_binary(self, treebin):
    if not treebin:
      return (None, None)
    tree = BinTree(None, None, None)
    node = treebin.pop(0)

    if node == 0:
      (treebin, tree.left) = self.from_binary(treebin)
      (treebin, tree.right) = self.from_binary(treebin)
    if node == 1:
      tree.key = [treebin.pop(0) for _ in range(8)][::-1]
      tree.key = BitArray.to_bytes(tree.key)[0]

    return (treebin, tree)

  def as_dict(self, tree = None, recurse = False, path = None):
    if not recurse:
      tree = self.tree;
      self.lookup = {}
    path = path or []

    if tree and tree.left:
      if tree.left.key == None:
        self.as_dict(tree.left, True, path + [0])
      else:
        self.lookup[tree.left.key] = path + [0]

    if tree and tree.right:
      if tree.right.key == None:
        self.as_dict(tree.right, True, path + [1])
      else:
        self.lookup[tree.right.key] = path + [1]

    return self.lookup

  def as_bytes(self):
    bitlist = self.as_bitarray()

    # Make a byte string from a byte array
    return BitArray.to_bytes(bitlist)

  def as_bitarray(self, tree = None, recurse = False):
    if not recurse:
      self.bitlist = []
      tree = self.tree;

    if tree.left:
      self.bitlist += BitArray.from_int(0, 1)
      if tree.left.key == None:
        self.as_bitarray(tree.left, True)
      else:
        self.bitlist += BitArray.from_int(1, 1)
        self.bitlist += BitArray.from_int(ord(tree.left.key), 8)

    if tree.right:
      if tree.right.key == None:
        self.as_bitarray(tree.right, True)
      else:
        self.bitlist += BitArray.from_int(1, 1)
        self.bitlist += BitArray.from_int(ord(tree.right.key), 8)

    return self.bitlist

  @staticmethod
  def _getweight(string):
    weights = {}

    for c in string:
      if c in weights:
        weights[c] += 1
      else:
        weights[c] = 1

    # Sort this to generate tree
    def _sort(e):
      return weights[e]

    sortd = []
    while len(weights):
      key = max(weights, key=_sort)
      sortd.append(key)
      weights.pop(key)

    return sortd
