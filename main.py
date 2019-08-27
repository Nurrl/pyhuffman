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

    print (compressed)
    return (tree.as_bytes(), BitArray.to_bytes(compressed))

  @staticmethod
  def uncompress(tree, compressed):
    tree = BitArray.from_bytes(tree)
    compressed = BitArray.from_bytes(compressed)

    print (compressed)

string = 'mmtbnl'
(tree, compressed) = Huffman.compress(string)
uncompressed = Huffman.uncompress(tree, compressed)
print(uncompressed)
