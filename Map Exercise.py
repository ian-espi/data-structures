# Ian Espinosa
# IanEspinosaBiz@gmail.com
# CS 22 Spring 2017 LBCC

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [list() for i in range(self.size)]
        self.data = [list() for i in range(self.size)]

    def put(self, key, data):
        hashIndex = self.hashfunction(key, self.size)
        if key in self.slots[hashIndex]:
            keyIndex = self.slots[hashIndex].index(key)
            self.data[hashIndex][keyIndex] = data
        else:
            self.slots[hashIndex].append(key)
            self.data[hashIndex].append(data)

    def get(self, key):
        hashKey = self.hashfunction(key, self.size)
        if key in self.slots[hashKey]:
            usedIndex = self.slots[hashKey].index(key)
            return self.data[hashKey][usedIndex]
        else:
            return None

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


## TEST FOR HashTable
h = HashTable()  # create new hash table

nums = [1, 3, 5, 50, 1000]  # some keys
nums = nums + [len(h.slots) * i for i in range(20)]  # some keys that have same hash
vals = vals = [chr(x) for x in range(ord('A'), ord('Z'))]  # list of single letters from A to Z

# add key/values
for i in range(len(nums)):
    # print("adding (%d, %s)"%(nums[i],vals[i]),end=" ")
    h[nums[i]] = vals[i]

for i in range(len(nums)):
    key = nums[i]
    value = vals[i]
    gotValue = h[key]
    assert gotValue == value, "expected key: %d to lookup value: %s but got value %s instead " % (key, value, gotValue)

# add new same key with different data, it should replace value for key
key = 5
value = 'dog'
h[key] = value
gotValue = h[key]
assert gotValue == value, "expected key: %d to lookup value: %s but got value %s instead " % (key, value, gotValue)

# try getting none existent key
assert h[
           199] == None, "expected h[199] to return None since there is no data stored under key 199, it returned %s end" % (
h[199])

print("\nAll TESTS PASSED")