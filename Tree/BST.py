class BTSNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BTSNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BTSNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "successfully inserted"

newBST = BTSNode(None)
print(insertNode(newBST, 100))
print(insertNode(newBST, 50))
print(insertNode(newBST, 70))
print(newBST.rightChild.data)