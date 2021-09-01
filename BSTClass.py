class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    def printTreeHelper(self, root):
        if root == None:
            return
        print(root.data, end = ":")
        if root.left != None:
            print("L:",end='')
            print(root.left.data,end=',')
        if root.right != None:
            print("R:",end='')
            print(root.right.data,end='')
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)
    
    def printTree(self):
        self.printTreeHelper(self.root)
    
    def searchHelper(self,root,data):
        if root==None:
            return False
        if root.data==data:
            return True
        if root.data>data:
            return self.searchHelper(root.left,data)
        else:
            return self.searchHelper(root.right,data)
    
    def search(self, data):
        return self.searchHelper(self.root,data)
    #Implement this function here
        
    def inserthelper(self,root,data):
        if root==None:
            node=BinaryTreeNode(data)
            return node
        if root.data>=data:
            root.left=self.inserthelper(root.left,data)
            return root
        else:
            root.right=self.inserthelper(root.right,data)
            return root
    
    def insert(self, data):
        self.numNodes=self.numNodes+1
        self.root=self.inserthelper(self.root, data)	
            
    #Implement this function here

    def min(self,root):
        if root==None:
            return 9999999
        if root.left==None:
            return root.data
        return self.min(root.left)
    
    def deleteHelper(self,root,data):
        if root==None:
            return False,None
        if root.data<data:
            deleted,newrightnode=self.deleteHelper(root.right,data)
            root.right=newrightnode
            return deleted, root
        if root.data>data:
            deleted,newleftnode=self.deleteHelper(root.left,data)
            root.left=newleftnode
            return deleted, root
        if root.left==None and root.right==None:
            return True, None
        if root.left==None:
            return True, root.right
        if root.right==None:
            return True, root.left
        
        replacement=self.min(root.right)
        root.data=replacement
        deleted, newrightnode = self.deleteHelper(root.right,replacement)
        root.right=newrightnode
        return True, root
    
    def delete(self, data):
        deleted, newroot=self.deleteHelper(self.root,data)
        if deleted:
            self.numNodes=self.numNodes-1
        self.root=newroot
        return deleted
    #Implement this function here
    
    def count(self):
        return self.numNodes
        
b = BST()
q = int(input())
while (q > 0) :
    li = [int(ele) for ele in input().strip().split()]
    choice = li[0]
    q-=1
    if choice == 1:
        data = li[1]
        b.insert(data)
    elif choice == 2:
        data = li[1]
        b.delete(data)
    elif choice == 3:
        data = li[1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
    else:
        b.printTree()