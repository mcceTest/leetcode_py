class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def constructFromList(lst):
        if not lst:
            return None

        head = cur = ListNode(lst[0])
        for i in range(1, len(lst)):
            cur.next = ListNode(lst[i])
            cur = cur.next

        return head    

    
    def equalToList(self, lst):
        if not lst:
            return False

        cur = self
        for _, n in enumerate(lst):
            if cur is None:
                return False

            if cur.val != n:
                return False

            cur = cur.next

        return cur is None    


    def __str__(self):
        cur = self
        values = []
        while cur is not None:
            values.append(cur.val)
            cur = cur.next
        return '->'.join(map(lambda x: str(x), values))

    
    def __lt__(self, other):
        return self.val < other.val