class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, value):
        currentNode = self.root
        for i in value:
            ch = i
            node = currentNode.children.get(ch)
            if node is None:
                node = TrieNode()
                currentNode.children.update({ch: node})
            currentNode = node
        currentNode.endOfString = True
        print("successful")

    def searchString(self, value):
        currentNode = self.root
        for i in value:
            node = currentNode.children.get(i)
            if node is None:
                return False
            currentNode = node

        if currentNode.endOfString is True:
            return True
        else:
            return False
