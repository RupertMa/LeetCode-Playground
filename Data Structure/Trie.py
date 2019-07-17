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

	def search(self, string):
		return self.find(self.root,string)


	def find(self, node, string):
		now = node
		if string =='':
			return now.isString
		if string[0]=='.':
			for i in now.subtree.keys():
				if not self.find(now.subtree[i],string[1:]):
					continue
				else:
					return True
			return False
		else:
			if string[0] not in now.subtree:
				return False
			else:
				return self.find(now.subtree[string[0]], string[1:])