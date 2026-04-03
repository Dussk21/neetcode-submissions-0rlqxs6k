class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if index == i:
                return curr.val
            curr = curr.next
            i += 1
        return -1
        

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode
        if self.tail == self.head:
            self.tail = self.head.next

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = newNode
        

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0
        while i < index and curr.next:
            curr = curr.next
            i += 1
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        ans = []
        while curr:
            ans.append(curr.val)
            curr = curr.next
        return ans

