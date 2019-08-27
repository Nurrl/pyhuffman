class BitArray:
  @staticmethod
  def from_int(num, width):
    return [(num >> k) & 1 for k in range(0, width)]

  @staticmethod
  def to_bytes(bitlist):
    bytelist = ''

    byte = 0
    for i in range(len(bitlist)):
      if (i and i % 8 == 0):
        bytelist += chr(byte)
        byte = 0
      bit = bitlist[i]
      byte |= bit << 7 - (i % 8)

    if ((len(bitlist) % 7) != 0):
      bytelist += chr(byte)

    return bytelist

  @staticmethod
  def from_bytes(bytelist):
    bitlist = []

    for byte in bytelist:
      bitlist += [(ord(byte) >> k) & 1 for k in range(7, -1, -1)]

    return bitlist
