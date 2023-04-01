from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
  def __init__(self, size):
    self.array_size= size
    self.array= [LinkedList() for i in range(size)]

  # four hash map methods are:
  # .hash(), .compress(), .assign(), .retrieve()
  def hash(self, key):
    return sum(key.encode())

  def compress(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index= self.compress(self.hash(key))
    payload= Node([key, value])
    list_at_array= self.array[array_index]
    for item in list_at_array:
      if item[0] == key:
        item[1]= value
        return
    list_at_array.insert(payload)


  def retrieve(self, key):
    array_index= self.compress(self.hash(key))
    list_at_index= self.array[array_index]

    for item in list_at_index:
      if item[0] == key:
        return item[1]
      
      # would have to implement open addressing /
      # probing solution to account for collisions
      if item[0] != key:
        return None
    return None

blossom= HashMap(len(flower_definitions))
for item in flower_definitions:
  print(item)
  blossom.assign(item[0], item[1])

print(blossom.retrieve('daisy'))
print(blossom.retrieve('carnation'))
print(blossom.retrieve('rose'))
print("('rose' prints out None due to collision)")
print(blossom.retrieve('lavender'))
