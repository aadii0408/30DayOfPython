#Day29_Challenge

class TrieNode:
    def __init__(self):
        self.isLeaf = False        
        self.character = {}
 
def insert(head, str):
 
    curr = head
 
    for c in str:
        curr = curr.character.setdefault(c, TrieNode())
 
    curr.isLeaf = True
 
def findLCP(dict):
    head = TrieNode()
    for s in dict:
        insert(head, s)
 
    lcp = ""
    curr = head
 
    while curr and not curr.isLeaf and len(curr.character) == 1:
 
        for k, v in curr.character.items():
           
            lcp += k

            curr = v
 
    return lcp
 
 
if __name__ == '__main__':
 
    # given set of keys
    dict = ["AAditya","Aadi","AAjkal"]
 
    print("longest common prefix is:", findLCP(dict))
