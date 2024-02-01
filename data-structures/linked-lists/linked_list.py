class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = node()
    
    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
        
    def length(self):
        cur = self.head
        count = 0
        while cur.next != None:
            count += 1
            cur = cur.next
        return count
        
    def display(self):
        temp = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            temp.append(cur.data)
        return temp
        
lst = linkedlist()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append("Hi")

print("The length of the linked list is: ",lst.length())
print("The node values are: ",lst.display())