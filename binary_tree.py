class Node():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree():
    def __init__(self, value):
        self.root = Node(value)
    
    def add(self, value):
        '''
        Adding new Node to tree
        '''
        temp = self.root
        while True:
            if value == temp.value:
                print("Binary tree cant have two nodes with equal values")
                return

            if value > temp.value and temp.right != None:
                temp = temp.right
            elif value > temp.value and temp.right == None:
                temp.right = Node(value)
                break
            
            if value < temp.value and temp.left != None:
                temp = temp.left
            elif value < temp.value and temp.left == None:
                temp.left = Node(value)
                break
    

    def traverse(self):
        '''
        Returns all elements of binary tree
        '''
        elements = ''
        def rec_traverse(current):
            nonlocal elements

            if current.left is not None:
                rec_traverse(current.left)
            elements += str(current.value) + ' '
            
            if current.right is not None:
                rec_traverse(current.right)
            

        rec_traverse(self.root)
        return elements
    

    def find(self, value):
        '''
        Checking is the value in binary tree or not
        Return: bool
        '''
        temp = self.root
        while True:
            print(temp.value, value, sep='\t')
            if value == temp.value:
                return True 

            if value > temp.value and temp.right:
                temp = temp.right

            elif value > temp.value and not temp.right:
                return False

            if value < temp.value and temp.left:
                temp = temp.left

            elif value < temp.value and not temp.left:
                return False
        

    def find_extended(self, value):
        '''
        Finds the element with given value, and returns its node and previous node
        Return: Node
        '''
        temp = self.root
        while True:
            if temp.right and value == temp.right.value:
                return temp, temp.right
                    
            if temp.left and value == temp.left.value:
                return temp, temp.left
                    
            if temp.left and value == temp.left.value:
                return temp, temp.left
            ############################################


            if value == self.root.value:
                return None, self.root

            if value > temp.value and temp.right:
                temp = temp.right

            elif value > temp.value and not temp.right:
                return False

            elif value < temp.value and temp.left:
                temp = temp.left

            elif value < temp.value and not temp.left:
                return False
                    
            


    def delete(self, value):
        '''
        Deleting node with give value from binary tree
        Return: None
        '''
        temp = self.root
        # previous = self.root
        if not self.find(value):
            print("Value is not in the list")
            return
                    
                
        prev_node, current_node = self.find_extended(value)

        ####################################
        if value == self.root.value and (self.root.right is not None  and  self.root.left is not None):
            left_side_top = self.root.left
            self.root = self.root.right
            pointer = self.root
            while pointer.left:
                pointer = pointer.left
            pointer.left = left_side_top
            return
        
        elif value == self.root.value and (self.root.right is not None  and  self.root.left is None):
            self.root = self.root.right
            return
        
        elif value == self.root.value and (self.root.left is not None and self.root.right is None):
            self.root = self.root.left
            return
        ####################################
        if value < prev_node.value and (current_node.right is not None  and  current_node.left is not None):
            prev_node.left = current_node.right
            pointer = current_node.right
            while pointer.left:
                pointer = pointer.left
                print(f'this is {pointer}')
            pointer.left = current_node.left

        if value > prev_node.value and (current_node.right is not None  and current_node.left is not None):
            prev_node.right = current_node.right
            pointer = current_node.right
            while pointer.left:
                pointer = pointer.left
            pointer.left = current_node.left
        ####################################
        if value < prev_node.value and (current_node.left is not None  and  current_node.right is None):
            prev_node.left = current_node.left

        if value < prev_node.value and (current_node.right is not None  and  current_node.left is None):
            prev_node.left = current_node.right



        if value > prev_node.value and (current_node.right is not None  and  current_node.left is None):
            prev_node.right = current_node.right
            
        if value > prev_node.value and (current_node.left is not None and current_node.right is None):
            prev_node.right = current_node.left

        ####################################
        if value < prev_node.value and (current_node.right is None and current_node.left is None):
            prev_node.left = None
        
        
        if value > prev_node.value and (current_node.right is None and current_node.left is None):
            prev_node.right = None
        ####################################


            



#Testing Block

my_tree = BinaryTree(25)
# random_list = [13, 10, 8, 5, 6, 3, 1, 4, 9, 8.5, 9.5]
# random_list  = [1, 5, 10]
# random_list = [1, 5, 3, 4, 2]
# random_list = [1,9,6,45,20,31,60,92,2,5,7,84,21]
random_list = [15, 11, 8, 2, 10, 9, 1, 3, 13, 14, 12, 11.5, 12.5, 20, 21, 19, 17, 24]
for i in range(len(random_list)):
    my_tree.add(random_list[i])

print(my_tree.traverse())
my_tree.delete(25)
my_tree.delete(19)
my_tree.delete(12.5)
my_tree.delete(13)
my_tree.delete(8)
my_tree.delete(2)
print(my_tree.traverse())

my_tree = BinaryTree(12)
random_list = [13, 10, 8, 5, 6, 3, 1, 4, 9, 8.5, 9.5]
for i in range(len(random_list)):
    my_tree.add(random_list[i])
print(my_tree.traverse())
my_tree.delete(25)
my_tree.delete(9)
my_tree.delete(12)
my_tree.delete(5)
my_tree.delete(10)
print(my_tree.traverse())

my_tree = BinaryTree(35)
random_list = [1,9,6,45,20,31,60,92,2,5,7,84,21]

for i in range(len(random_list)):
    my_tree.add(random_list[i])
print(my_tree.traverse())
my_tree.delete(31)
my_tree.delete(92)
my_tree.delete(7)
my_tree.delete(5)
my_tree.delete(1)
print(my_tree.traverse())
