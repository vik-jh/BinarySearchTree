"""Given a sorted integer array A of size n, which contains all unique elements. You need to construct a balanced BST from this input array. Return the root of constructed BST.
Note: If array size is even, take first mid as root.
Input format:
The first line of input contains an integer, which denotes the value of n. The following line contains n space separated integers, that denote the values of array.
Output Format:
The first and only line of output contains values of BST nodes, printed in pre order traversal."""

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''def constructBST(lst):
    n=len(lst)
    start=0
    end=(n-1)
    mid=(start+end)/2
    root=lst[mid]
    root.left=constructBST(lst[0:mid])
    root.right=constructBST(lst[mid+1:end])
    return root'''
def constructBST(lst):
    if len(lst)<=0:
        return None
    mid=len(lst)//2
    if len(lst)%2!=0:
        x=lst[mid]
    else:
        mid=mid-1
        x=lst[mid]
   
    root=BinaryTreeNode(x)
    leftBST = constructBST(lst[0:mid])
    rightBST = constructBST(lst[mid+1:])
    root.left=leftBST
    root.right=rightBST
    return root  
        
    
def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input())
if(n>0):
    lst=[int(i) for i in input().strip().split()]
else:
    lst=[]
root=constructBST(lst)
preOrder(root)