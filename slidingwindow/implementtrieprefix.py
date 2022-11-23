class TrieNode:
    def __init__(self):
        #creating  TRIE CLASS NODE AND ISEND VALUE TO BE FAlsse
        self.isEnd = False
        #children array with None value for length of alphabets value
        self.children = [None]*26 

class Trie(object):
    def __init__(self):
        # creating trienode with root values
        self.root = TrieNode() 
        

    def insert(self, word: str) -> None:
        #current value will be the root
        curr = self.root 
        #for every character in word
        for char in word:
            #key value is calculated by subtracting the ascii value of char with 'a'
            key = ord(char) - ord('a') 
            # if key is not None
            if curr.children[key]==None: 
                 #assign the trienode value to current value of chcildren
                curr.children[key]= TrieNode()
                 # assign the key value of children  to current 
            curr = curr.children[key]
             #current isend is valued to True
        
        curr.isEnd = True
        

    def search(self, word: str) -> bool:
        
        #current value will be the root
        curr = self.root
          #for every character in prefix    
        for char in word:
            #key value is calculated by subtracting the ascii value of char with 'a'
            key = ord(char)-ord('a')
            # if key is not None
            if curr.children[key]==None:
                return False
            #assign the curr to current children of key
            curr = curr.children[key] 
            #return the isend value
        return curr.isEnd 
        

    def startsWith(self, prefix: str) -> bool:
        #current value will be the root
        curr = self.root 
        #for every character in word
        for char in prefix:
            #key value is calculated by subtracting the ascii value of char with 'a'
            key = ord(char) - ord('a') 
             # if key is not None
            if curr.children[key]==None: 
                return False
             # assign the key value to current then return true
            curr = curr.children[key]
            #return True
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)