class MyNode():
    def  __init__(self, value, next = None):
        self.value = value 
        self.next = next


class LinkedList():
    def __init__(self):
        self.root = MyNode(9)

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
             elements += str(temp.value) + ', '
        
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
            if temp.next != None:
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
        temp = self.root
        for _ in range(index - 1):
            temp = temp.next
        
        temp.next = temp.next.next
        

my_ll = LinkedList()
my_ll.add()