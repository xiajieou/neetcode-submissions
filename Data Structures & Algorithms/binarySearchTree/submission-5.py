class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if not self.root:
            self.root = newNode
            return 
        
        curr = self.root
        while True:
            if newNode.key < curr.key:
                if not curr.left:
                    curr.left = newNode
                    return 
                curr = curr.left
            elif newNode.key > curr.key:
                if not curr.right:
                    curr.right = newNode
                    return 
                curr = curr.right
            else:
                curr.val = newNode.val
                return

    def get(self, key: int) -> int:
        curr = self.root 

        while curr:
            if key < curr.key:
                curr = curr.left
            
            elif key > curr.key:
                curr = curr.right
            
            else:
                return curr.val

        return -1 


    def getMin(self) -> int:
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr.val if curr else -1

    def findMin(self, node):
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    #remove the node with key, return the new root of the subtree
    def removeHelper(self, curr, key) -> TreeNode:
        if curr == None:
            return None 
        
        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        
        else:
            if curr.left == None:
                return curr.right
            elif curr.right == None:
                return curr.left
            else:
                #swap curr with inorder successor
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)
            return curr 

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result

    def inorderTraversal(self, root, result):
        if root:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)


