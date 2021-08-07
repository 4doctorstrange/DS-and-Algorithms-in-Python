class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data, parent):
        if self.root == None:
            node = Node(data)
            self.root = node
            #print(self.root.data,"root of tree")
            return
        elif data == parent.data:
            return

        elif data < parent.data:
            if parent.left == None:  # if root ka left child does't exist
                node = Node(data)
                parent.left = node
                return
            else:
                self.insert(data, parent.left)

        elif data > parent.data:
            if parent.right == None:
                node = Node(data)
                parent.right = node
                return
            else:
                self.insert(data, parent.right)

    def inorder(self, parent):
        """ Left Parent Right"""
        if parent == None:
            return
        elif parent:  # if left child is there
            self.inorder(parent.left)
            print(parent.data, end=" ")

            self.inorder(parent.right)

    def preorder(self, parent):
        """ Parent Left Right"""
        if parent == None:
            return
        elif parent:
            print(parent.data, end=" ")
            self.preorder(parent.left)
            self.preorder(parent.right)

    def postorder(self, parent):
        """Left Right Parent """
        if parent == None:
            return
        elif parent:
            self.postorder(parent.left)
            self.postorder(parent.right)
            print(parent.data, end=" ")

    def levelorder(self, parent):
        """BFS"""
        q = []
        q.append(parent)

        while q:
            node = q.pop(0)
            print(node.data, end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def height(self, parent):
        if parent == None:
            return 0
        else:
            height_tree = 1 + max(self.height(parent.left),
                                  self.height(parent.right))
            return height_tree


    def min_max_element(self, parent):
        '''min element will be bottommost element of LST and max at the RST'''
        def get_min(parent):
            if parent.left:
                return get_min(parent.left)
            else:
                return parent

        def get_max(parent):
            if parent.right:
                return get_max(parent.right)
            else:
                return parent
        return (get_min(parent),get_max(parent))

    def find(self,parent,x):
        if parent:
            if parent.data==x:
                return parent  #returning node
            if x< parent.data:
                return self.find(parent.left,x)
            if x>parent.data:
                return self.find(parent.right,x)
            return None
        else:
            return None

    def get_distance(self,parent,x):
        ''' It is assumed that x exist in tree otherwise we will use find to check'''
        if parent:
            if parent.data==x:
                return 0
            if x<parent.data and parent.left:
                return 1+ self.get_distance(parent.left,x)
            if x>parent.data and parent.right:
                return 1+ self.get_distance(parent.right,x)
            return 0
        else:
            return 0

    def checkleaf(self,parent,x):
        node = self.find(parent,x)
        if node.left==None and node.right==None:
            return node
        else:
            return None

    def checkSingleChild(self,parent,x):
        node = self.find(parent,x)
        if (node.left and node.right==None) or (node.left==None and node.right):
            return node
        else:
            return None

    def checkTwoChild(self,parent,x):
        node = self.find(parent,x)
        if node.left and node.right:
            return node
        else:
            return None


    def get_parent(self,parent,node):  #here parent refers to current node
        ''' IT IS ASSUMED THAT NODE WILL EXIST IN TREE'''
        if parent.left==node or parent.right == node:  #checking left and right child of current node
            return parent
        if node.data<parent.data:
            return self.get_parent(parent.left,node)
        if node.data>parent.data:
            return self.get_parent(parent.right,node)
        
    def delete(self,parent,x):
        ''' checking if node is leaf node '''
        node = self.checkleaf(parent,x)
        if node:
            parent_node=self.get_parent(parent,node)
            if parent_node.left==node:
                parent_node.left=None
            else:
                parent_node.right=None
            return 
        ''' if it is not leaf node then we check if it is single child '''
        node = self.checkSingleChild(parent,x) #here node has either left child or right child
        if node:
            parent_node=self.get_parent(parent,node)
            if parent_node.right == node:   # if node is parent's right child then we will set parent's right with the child of node
                if node.left: 
                    parent_node.right = node.left
                elif node.right:
                    parent_node.right = node.right

            elif parent_node.left == node:
                if node.left: 
                    parent_node.left = node.left
                elif node.right:
                    parent_node.left = node.right
            return 
        ''' check if it is has 2  child '''
        node = self.checkTwoChild(parent,x)
        inorderSuccessor = self.min_max_element(node.right)[0]   #getting minimum value node in right sub tree
        #print(inorderSuccessor.data,"inorder daat")
        parent_node=self.get_parent(parent,node)
        parent_node.right.data = inorderSuccessor.data  #copying inorder's data to parent's right
        #finally deleting inordersuccessorS
        ''' NOT POSSIBLE IN THIS AS single function is handling all the 3 cases '''











array = [67, 34, 80, 12, 45, 78, 95, 10, 38, 60, 86]
tree = BST()
root=tree.root
for i in array:
    tree.insert(i, tree.root)

print("Inorder->", tree.inorder(tree.root))
'''
print("Preorder",tree.preorder(tree.root))
print("Postorder",tree.postorder(tree.root))
print("level Order",tree.levelorder(tree.root))
print("Height of tree", tree.height(tree.root))

min_max= tree.min_max_element(tree.root)
print("Minimum element:",min_max[0] ,"Maximum element:",min_max[1])

print("checking if 15 in tree:", tree.find(tree.root,15))

print("getting distance from root node", tree.get_distance(tree.root,60))
'''
tree.delete(tree.root,80)

print("Inorder->", tree.inorder(tree.root))
