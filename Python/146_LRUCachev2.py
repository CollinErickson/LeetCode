
import heapq

class LRUCache:
    h = []
    nextind=0
    capacity=None
    d = None
    lastaccess = None

    def __init__(self, capacity: int):
        #self.d1 = [None for i in range(capacity)]
        #self.d2 = {}
        self.nextind = 0
        self.capacity = capacity
        self.h = []
        self.d2 = {}
        self.lastaccess = {}
        
        

    def get(self, key: int) -> int:
      if key in self.d2:
        # Update last access
        self.lastaccess[key] = self.nextind
        self.nextind += 1
        return self.d2[key]
      return -1
        

    def put(self, key: int, value: int) -> None:
      # If key is already in dict: update value, return
      if key in self.d2:
        self.lastaccess[key] = self.nextind
        self.nextind += 1
        self.d2[key] = value
        return # self.d2[key]
      # Otherwise need to add it
      # If at capacity, need to delete one first
      if len(self.h) >= self.capacity:
        popped = heapq.heappop(self.h)
        # Delete from d2, lastaccess
        poppedkey = popped[1]
        poppedind = popped[0]
        # Check if it has been accessed in meantime
        while poppedind != self.lastaccess[poppedkey]:
          heapq.heappush(self.h, (self.lastaccess[poppedkey], poppedkey))
          popped = heapq.heappop(self.h)
          poppedkey = popped[1]
          poppedind = popped[0]

        del self.d2[poppedkey]
        del self.lastaccess[poppedkey]
      # Add new key  
      ind = self.nextind
      self.nextind += 1
      # Add to heap
      heapq.heappush(self. h, (ind, key))
      # Add to d2 and lastaccess
      self.d2[key] = value
      self.lastaccess[key] = ind
      return
    
    def __repr__(self):
      return str(self.h)  + " >> " + str(self.d2)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

obj = LRUCache(5)
print(obj)
obj.put(0, 0)
print(obj)
print('get 0', obj.get(0))
print('get 1', obj.get(1))
for i in range(1,11):
  obj.put(i,i)
  print(obj)
print('get 0', obj.get(0))
print('get 10', obj.get(10))
# param_1 = obj.get(key)
# obj.put(key,value)



lRUCache = LRUCache(2);
print(0, lRUCache)
lRUCache.put(1, 1); # cache is {1=1}
print(1, lRUCache)
lRUCache.put(2, 2); # cache is {1=1, 2=2}
print(2, lRUCache)
lRUCache.get(1);    # return 1
print(3, lRUCache)
lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(4, lRUCache)
lRUCache.get(2);    # returns -1 (not found)
print(5, lRUCache)
lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(6, lRUCache)
print(lRUCache.get(1))    # return -1 (not found)
print(7, lRUCache)
print(lRUCache.get(3));    # return 3
print(8, lRUCache)
print(lRUCache.get(4));    # return 4
print(9, lRUCache)
