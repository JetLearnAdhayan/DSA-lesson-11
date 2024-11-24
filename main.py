class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


def Inorder(root):
    if root is not None:
        if root.left is not None:
            Inorder(root.left)
        print(root.data)    

        if root.right is not None:
            Inorder(root.right)



def insert(root,x):
    if root == None:
        return Node(x)
    if x < root.data:
        root.left = insert(root.left,x)

    else:
        root.right = insert(root.right,x)    

    return root

def delete(root,key):
    if root is None:
        return root
    if key < root.data:
        root.left = delete(root.left,key)
    elif key > root.data:
        root.right = delete(root.right,key)
    else:
        if root.left is None and root.right is None:
            return None
        
        elif root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    return root
def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left

    return current    

element = int(input("Enter the number of elements you want: "))  
root = None 

for i in range(1,element+1):
    x = int(input(f"Enter the element {i}: "))
    
    root = insert(root,x)

print("BST before Deletion:")
Inorder(root)
key = int(input("Enter the number you want to delete: "))

root = delete(root,key)
print("BST after Deletion: ")
Inorder(root)