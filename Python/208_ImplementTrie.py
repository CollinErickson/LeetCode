class TrieNode:
  def __init__(self):
    self.children = {}
    self.isword = False

class Trie:
  def __init__(self):
      self.head = TrieNode()

  def insert(self, word: str) -> None:
    node = self.head
    for i in range(len(word)):
      if word[i] in node.children:
        node = node.children.get(word[i])
      else:
        node.children[word[i]] = TrieNode()
        node = node.children[word[i]]
    node.isword = True
    return

  def search(self, word: str) -> bool:
    node = self.head
    for i in range(len(word)):
      if word[i] in node.children:
        node = node.children.get(word[i])
      else:
        return False
    return node.isword

  def startsWith(self, prefix: str) -> bool:
    node = self.head
    for i in range(len(prefix)):
      if prefix[i] in node.children:
        node = node.children.get(prefix[i])
      else:
        return False
    return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

obj = Trie()
obj.insert("apple")
print(obj.search("apple"), "T")
# print(obj.head.children)
print(obj.search('app'), "F")
print(obj.startsWith("app"), "T")
obj.insert('app')
print(obj.search('app'), "T")
print(obj.search('p'), "F")
print(obj.startsWith('a'), "T")

