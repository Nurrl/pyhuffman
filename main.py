#!/usr/bin/env python3

from classes.bitarray import BitArray
from classes.tree import Tree

class Huffman:
  @staticmethod
  def compress(string):
    if not string or not len(string):
      throw
    tree = Tree(string)
    treedict = tree.as_dict()
    compressed = []

    for c in string:
      compressed += treedict[c]

    return (tree.as_bytes(), BitArray.to_bytes(compressed))

  @staticmethod
  def uncompress(tree, compressed):
    string = BitArray.from_bytes(compressed)
    tree = Tree(None, tree)

    uncompressed = ''
    sel = tree.tree
    for bit in string:
      if bit == 0:
        sel = sel.left
      else:
        sel = sel.right
      if (sel.key):
        uncompressed += sel.key
        sel = tree.tree

    return uncompressed

if __name__ == "__main__":
  # Compress string and get the tree and the compressed binary
  try:
    (tree, compressed) = Huffman.compress('Hey')

    # Feed the tree and the string to the uncompress algorithm
    uncompressed = Huffman.uncompress(tree, compressed)

    print(uncompressed)
  except:
    print('Cannot compress 0 bytes')

