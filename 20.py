class Node:
    def __init__(self,data):
        self.prev=None #new add
        self.data = data
        self.next = None
class DBCLinkedList:
    def __init__(self):
        self.head = None
    def create(self):
        ptr = None
        count = 0
        while True:
            count += 1
            data = int(input(f"Enter node{count} data: "))
            cur = Node(data)
            cur.prev=cur
            cur.next=cur
            if self.head is None:
                self.head = cur
            else:
                cur.prev=ptr #new add
                ptr.next = cur
                self.head.prev=cur
                cur.next=self.head
            ptr = cur
            ch = input("Do you want to continue another node? Press y or Y: ")
            if ch.lower() != 'y':
                break
    def displayf(self):
        temp = self.head
        print("Elements are forward:")
        while temp.next is not self.head:
            print(temp.data)
            temp = temp.next
        print(temp.data)
    def displayb(self):
        temp = self.head.prev
        print("Elements are backward:")
        while temp.prev is not self.head.prev :
            print(temp.data)
            temp = temp.prev
        print(temp.data)
    def insbeg(self):
        ele = int(input("enter data \n"))
        curr = Node(ele)
        curr.prev=curr
        curr.next=curr
        if self.head is None:
            self.head=curr
            return
        curr.next = self.head
        curr.prev= self.head.prev
        self.head.prev.next = curr
        self.head.prev = curr
        self.head=curr
ll =DBCLinkedList()
ll.create()
ll.displayf()
ll.displayb()
ll.insbeg()
ll.displayf()
ll.displayb()