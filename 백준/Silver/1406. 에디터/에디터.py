import sys
input = sys.stdin.readline


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.first = None
        self.last = None
    def Append(self, value):
        n = Node(value)
        if(self.last == None):
            self.first = n
            self.last = n
            return
        self.Insert(self.last, n)
    def Insert(self, cursor:Node, target:Node):
        if(cursor == None):
            if(self.first == None):
                self.first = target
                self.last = target
                return target
            target.next = self.first
            self.first.prev = target
            self.first = target
            return target
        
        if(cursor.next == None):
            cursor.next = target
            target.prev = cursor
            self.last = target
            return target

        target.next = cursor.next
        cursor.next.prev = target
        target.prev = cursor
        cursor.next = target
        return target
    
    def Remove(self, cursor:Node):
        if(cursor == None):
            return cursor
        
        if(cursor.next == None):
            if(cursor.prev == None):
                ret = None
                self.first = None
                self.last = None
                del cursor
                return ret
            
            cursor.prev.next = None
            ret = cursor.prev
            self.last = ret
            del cursor
            return ret
        
        if(cursor.prev == None):
            cursor.next.prev = None
            self.first = cursor.next
            del cursor
            return None
        
        cursor.prev.next = cursor.next
        cursor.next.prev = cursor.prev
        ret = cursor.prev
        del cursor
        return ret
    
    def PrintAll(self):
        cur = self.first
        while(cur != None):
            print(cur.value, end="")
            cur = cur.next
        
        

temp = input().rstrip()

ll = LinkedList()
for i in temp:
    ll.Append(i)

cursor = ll.last

N = int(input())

for _ in range(N):
    op = input()
    
    # 커서 왼쪽으로 한칸 옮김
    if(op[0] == 'L'):
        if(cursor != None):
            cursor = cursor.prev
    # 커서 오른쪽으로 한칸 옮김
    elif(op[0] == 'D'):
        if(cursor == None):
            cursor = ll.first
            continue
        if(cursor.next != None):
            cursor = cursor.next
    # 커서 왼쪽 문자 삭제함
    elif(op[0] == 'B'):
        cursor = ll.Remove(cursor)
    # 커서 위치에 문자 추가
    elif(op[0] == 'P'):
        cursor = ll.Insert(cursor, Node(op[2]))

ll.PrintAll()