class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;

class LinkedList:
    def __init__(self):
        self.head = None;

    def init(self, elems):
        elems.reverse();
        for i in range(len(elems)):
            node = Node(elems[i]);
            if self.head == None:
                self.head = node;
            else:
                tmp = self.head;
                node.next = tmp;
                self.head = node;

    # [1, 2, 3, 4]
    # [2, 1, 3, 4]
    # [3, 2, 1, 4]
    # [4, 3, 2, 1]
    def reverse(self, head):

        curr = head;
        prev = head;
        while True:
            if prev.next == None:
                break;
            next = prev.next;
            next_next = None;
            if next is not None:
                next_next = next.next;
            prev.next = next_next;
            next.next = curr;
            curr = next;
        self.head = curr;


    
    def printList(self):
        head = self.head;

        list = [];
        while head != None:
            list.append(head.data);
            head = head.next;
        print(list)

ls = LinkedList()
ls.printList();
ls.init([1, 2, 3, 4, 5, 6, 7, 8, 9]);
ls.printList();
ls.reverse(ls.head);
ls.printList();