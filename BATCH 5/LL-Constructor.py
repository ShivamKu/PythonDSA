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
        return temp

    def prepend(self,value):
        #create new node
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
        return True
    
    def pop_first(self):
        if self.length==0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length-=1
        if self.length==0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index <0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        # create new node --> class create
        if index<0 or index > self.length:
            return False
        elif index==0:
            return self.prepend(value) # it returns true and false
        elif index==self.length:
            return self.append(value) # it returns true and false
        else:
            # insert Node
            new_node = Node(value)
            temp = self.get(index-1)
            new_node.next = temp.next
            temp.next = new_node
            self.length+=1
            return True
    
    def remove(self, index):
        if index<0 and index>=self.length:
            return None
        elif index ==0:
            return self.pop_first()
        elif index == self.length:
            return self.pop()
        else:
            prev = self.get(index -1)
            temp = prev.next
            prev.next = temp.next
            temp.next = None
            self.length-=1
            return temp
        
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


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
my_linked_list = LinkedList(2)
my_linked_list.append(3)


my_linked_list.print_list()
print("\n")
my_linked_list.prepend(1)
my_linked_list.print_list()
print("\n")
print(my_linked_list.pop_first())
print(my_linked_list.pop_first())

print(my_linked_list.pop_first())
print(my_linked_list.pop_first())

my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(4)
my_linked_list.append(5)
print(f"\n\nthe element at index 2 is: {my_linked_list.get(2)}")

my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)
print("\n\nthe linked list is:")
my_linked_list.print_list()
print("\nthe linkled list after update:")
my_linked_list.set_value(1,4)
my_linked_list.print_list()


my_linked_list = LinkedList(0)
my_linked_list.append(2)
print("\n\nthe linked list before insert:")
my_linked_list.print_list()
my_linked_list.insert(1,1)
print("\nThe linked list after insert",'\n')
my_linked_list.print_list()


my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)
print('\n\n')
my_linked_list.print_list()
print('\n',my_linked_list.remove(2),'\n')
my_linked_list.print_list()

print("\n\nReverse a Linked List")
my_linked_list=LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.print_list()
print("\n After reversal:")
my_linked_list.reverse()
my_linked_list.print_list()