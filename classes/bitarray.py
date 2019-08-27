class BitArray:
  @staticmethod
  def from_int(num, width):
    return [(num >> k) & 1 for k in range(0, width)]

  @staticmethod
  def to_bytes(bitlist):
    bytelist = ''

    byte = 0
    count = 0
    for i in range(len(bitlist)):
      bit = bitlist[i]
      count += 1
      byte <<= 1
      byte += bit
      if count > 7 or i == len(bitlist) - 1:
        bytelist += chr(byte)
        byte = 0
        count = 0

    return bytelist

  @staticmethod
  def from_bytes(bytelist):
    bitlist = []

    for byte in bytelist:
      bitlist += [(ord(byte) >> k) & 1 for k in range(7, -1, -1)]

    return bitlist
