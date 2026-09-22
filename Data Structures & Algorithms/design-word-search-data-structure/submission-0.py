class TrieNode:
    def __init__(self):
        self.children={}
        self.word=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        
    def addWord(self, word: str) -> None:
        curr=self.root
        for x in word:
            if x not in curr.children:
                curr.children[x]=TrieNode()
            curr=curr.children[x]
        curr.word=True
        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)
