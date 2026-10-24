class Node:
    def __init__(self,value):
        self.value=value
        self.next = None

class LinkedList:
    def __init__(self,value):
        # create new Node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        #create new node
        new_node = Node(value)
        # add node to end; if checks linked list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next=new_node
            self.tail = new_node
        self.length+=1
        # another method requires bool output from this method
        return True
    
    def pop(self):
        # empty linked list
        if self.length==0:
            return None
        # two pointer temp and pre; temp checks next is None i.e. temp.next=None if not None then inc pre
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp= temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    """def prepend(self,value):
        #create new node
        # add node in begining
    def insert(self,index,value):
        # create new node --> class create
        # insert Node"""
    


my_linked_list = LinkedList(1)
my_linked_list.append(2)
#my_linked_list.print_list()
#print(my_linked_list.tail.value)
# (2) items - return 2 Node
print(my_linked_list.pop())
# (1) item- returns 1 Node
print(my_linked_list.pop())
# (0) item - return None
print(my_linked_list.pop())