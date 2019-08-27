#!/usr/bin/env python3

from classes.bitarray import BitArray
from classes.tree import Tree

class Huffman:
  @staticmethod
  def compress(string):
    tree = Tree(string)
    treedict = tree.as_dict()
    compressed = []

    for c in string:
      compressed += treedict[c]

    return (tree.as_bytes(), BitArray.to_bytes(compressed))

  @staticmethod
  def uncompress(tree, compressed):
    compressed = BitArray.from_bytes(compressed)
    treeobj = Tree(None, tree)

if __name__ == "__main__":
  # Compress string and get the tree and the compressed binary
  (tree, compressed) = Huffman.compress('Hello')

  # Feed the tree and the string to the uncompress algorithm
  uncompressed = Huffman.uncompress(tree, compressed)

  print(uncompressed)
