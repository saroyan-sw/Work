class MyNode():
    def  __init__(self, value, next = None):
        self.value = value 
        self.next = next


class LinkedList():
    def __init__(self, value):
        self.root = MyNode(value)

    def add(self, value:int):
        '''
        Adding new element to the end of LL

        Return: None
        '''
        temp = self.root
        while temp.next is not None:
            temp = temp.next

        temp.next = MyNode(value)


    def find(self, value:int):
        '''
        Finding the index of first element with that value

        Return: int

        '''
        temp = self.root
        index = 0
        while temp.value != value:
            if temp.next == None:
                print('Element is not on List')
                return -1
            temp = temp.next
            index += 1

        return index


    def get(self, index:int):
        '''
        Getting value of element with given index

        Return: int
        '''
        temp = self.root

        for i in range(index):
            if temp.next == None:
                print('Index out of range')
                return
            temp = temp.next

        return temp.value
        

    def traverse(self):
        '''
        Returning all elents in the LL

        Return: str
        '''
        temp = self.root
        elements = ''

        while temp.next != None:
             elements += str(temp.value) + ' '
             temp = temp.next
        
        return elements

    
    def insert(self, index:int, value:int):
        '''
        Adding element to LL in given index with given value 
        '''


        if index == 0:
            upcoming = self.root
            self.root = MyNode(value, upcoming)
            return

        temp = self.root

        for _ in range(index - 1):
            if temp.next.next != None:
                temp = temp.next
            else:
                print('Index out of range')
                return
                
        
        if temp.next != None:
            upcoming = temp.next
            temp.next = MyNode(value, upcoming)
        else:
            temp.next = MyNode(value, None)

        
    def delete(self, index:int):
        '''
        Deleting the elemnt of LL with given index

        Return: None
        '''

        if index == 0:
            self.root = self.root.next
            return
        
        temp = self.root
        for _ in range(index - 1):
            if temp.next.next != None:
                temp = temp.next
            else:
                temp = None
                print('Index out of range')
                return
        
        temp.next = temp.next.next
        
my_ll = LinkedList(8)
for i in range(5):
    my_ll.add(i)

print(my_ll.traverse())
my_ll.delete(5)
print(my_ll.traverse())
# print(my_ll.insert(5,88), my_ll.traverse())

