class TrieNode(object):
    
    def __init__(self):
        self.isString = False
        self.subtree = {}
        self.s = ''

class TrieTree(object):

	def __init__(self):
		self.root = TrieNode()

	def insert(self, string):
		now = self.root
		for i in range(len(string)):
			if string[i] not in now.subtree: 
				now.subtree[string[i]] = TrieNode()
			now = now.subtree[string[i]]
		now.s = string
		now.isString = True

	def find(self, string):
		now = self.root
		for i in range(len(string)):
			if string[i] not in now.subtree:
				return False
			now = now.subtree[string[i]]
		return now.isString