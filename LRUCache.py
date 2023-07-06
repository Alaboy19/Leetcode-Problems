'''
146. LRU Cache - Medium
Given:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
'''
'''
Solution:
0)  create hashmap to sve key-value pair, and add key 
1) to track teh history of the keys added, use head and tail of DoubleListNode(key, val, prev, next)
2) head and tail are dummy and head side is least recently used and tail side is most recenlty used
3) have a key in node as a implicit backward pointer when we need to pop some key from hashmap when eviction happens
4) get and put updates the recency, from current pos to tail side, if there is no get, put recency works as recency criteria 
5) so, head -><- put 1 -><- put 2 -><- put3 -><- tail 
6) defince 
'''

class DoubleListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

  def __init__(self, capacity: int):
      self.capacity = capacity
      self.hashmap = {}
      self.size = 0
      self.head = DoubleListNode()
      self.tail = DoubleListNode()

  def update(self, node: Optional[DoubleListNode])-> None:
      
      next_node = node.next
      prev_node = node.prev
      next_node.prev = prev_node
      prev_node.next = next_node

      node.prev = self.tail.prev
      self.tail.prev.next = node
      self.tail.prev = node
      node.next = self.tail

  def add_tail(self, new_node: Optional[DoubleListNode])-> None:
      new_node.prev = self.tail.prev
      self.tail.prev.next = new_node
      self.tail.prev = new_node
      new_node.next = self.tail



  def get(self, key: int) -> int:
      if key in self.hashmap:
          # prover if this key has prev
          node = self.hashmap[key]
          self.update(node)
          return self.hashmap[key].val
      return -1

  def put(self, key: int, value: int) -> None:
      if key in self.hashmap:
          self.hashmap[key].val = value
          node = self.hashmap[key]
          self.update(node)
      else:
          if self.size == 0:
              new_node = DoubleListNode(key, value, self.tail, self.head)
              self.hashmap[key] =new_node
              self.head.next = new_node
              self.tail.prev = new_node
              self.size += 1
          elif self.size < self.capacity:
              new_node = DoubleListNode(key, value)
              self.hashmap[key] =new_node
              self.add_tail(new_node)
              self.size += 1
          else:
              key_to_delete = self.head.next.key
              self.hashmap.pop(key_to_delete, None)

              next_node = self.head.next
              self.head.next = next_node.next
              next_node.next = None
              next_node.prev = None
              self.head.next.prev = self.head

              new_node = DoubleListNode(key, value)
              self.hashmap[key] =new_node
              self.add_tail(new_node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
