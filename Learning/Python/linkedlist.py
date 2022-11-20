class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def ins_at_beg(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print("Linked list is empty.")
            return
        
        itr = self.head
        llist = ''
        while itr:
            llist += str(itr.data) + '-->'
            itr = itr.next
            6
        print(llist)
    
if __name__ == '__main__':
    ll = LinkedList()
    ll.ins_at_beg(3)
    ll.ins_at_beg(4)
    ll.print()