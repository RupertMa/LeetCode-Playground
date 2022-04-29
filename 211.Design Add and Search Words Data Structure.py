class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()


    def addWord(self, word: str) -> None:
        now = self.root
        for i in range(len(word)):
            if word[i] not in now.subtree:
                now.subtree[word[i]] = TreeNode()
            now = now.subtree[word[i]]
        now.isString = True

    def search(self, word: str) -> bool:
        return self.find(self.root, word)

    def find(self, node, word):
        if word == '':
            return node.isString

        if word[0]=='.':
            for key in node.subtree.keys():
                if not self.find(node.subtree[key], word[1:]):
                    continue
                else:
                    return True
            return False

        if word[0] in node.subtree:
            return self.find(node.subtree[word[0]], word[1:])
        else:
            return False




class TreeNode:
    def __init__(self):
        self.subtree = {}
        self.isString = False
