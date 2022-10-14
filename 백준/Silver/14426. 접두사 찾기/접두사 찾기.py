class Node:
    def __init__(self, key):
        self.key = key
        self.data = None
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        current_node = self.head
        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string
        
    def find(self, string):
        current_node = self.head
        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        return True

N, M = map(int,input().split())
trie = Trie()
ans = 0
for i in range(N):
    trie.insert(input())
for i in range(M):
    k = trie.find(input())
    if k:
        ans += 1
print(ans)