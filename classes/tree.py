from classes.bintree import BinTree
from classes.bitarray import BitArray

class Tree:
  def __init__(self, string):
    self.weights = self._getweight(string)
    self.bytes = '';
    self.lookup = {}

    # Generate binary tree from weights
    while len(self.weights) > 1:
      left = self.weights.pop(-1)
      right = self.weights.pop(-1)

      self.weights = [(left[0] + right[0], BinTree(None, left, right))] + self.weights

    self.tree = self.weights[0]

  def as_dict(self, tree = None, recurse = False, path = None):
    if not recurse:
      tree = self.tree;
    tree = tree[1];
    path = path or []

    if tree.left:
      if type(tree.left[1]) is BinTree:
        self.as_dict(tree.left, True, path + [0])
      else:
        self.lookup[tree.left[1]] = path + [0]

    if tree.right:
      if type(tree.right[1]) is BinTree:
        self.as_dict(tree.right, True, path + [1])
      else:
        self.lookup[tree.right[1]] = path + [1]

    return self.lookup

  def as_bytes(self):
    bitlist = self.as_bitarray()

    # Make a byte string from a byte array
    return BitArray.to_bytes(bitlist)

  def as_bitarray(self, tree = None, recurse = False):
    if not recurse:
      self.bitlist = []
      tree = self.tree;
    tree = tree[1];

    if tree.left:
      self.bitlist += BitArray.from_int(0, 1)
      if type(tree.left[1]) is BinTree:
        self.as_bitarray(tree.left, True)
      else:
        self.bitlist += BitArray.from_int(1, 1)
        self.bitlist += BitArray.from_int(ord(tree.left[1]), 8)

    if tree.right:
      if type(tree.right[1]) is BinTree:
        self.as_bitarray(tree.right, True)
      else:
        self.bitlist += BitArray.from_int(1, 1)
        self.bitlist += BitArray.from_int(ord(tree.right[1]), 8)

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
      sortd.append((weights.pop(key), key))

    return sortd
