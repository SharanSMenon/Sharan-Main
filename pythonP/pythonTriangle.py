x = 1
size = 16 # Size must be multiples of 8
for i in range(size):
  print((' ' * (size - i)) + bin(x)[2:]
  .replace('0', '  ').replace('1', ' *'))
  x ^= x << 1
ext = input("Press enter to exit.")
