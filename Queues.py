#I tried doing circular queue without classes and it didnt work so here
#is it with class

class MyQueue():
    def __init__(self):
        self.front = 0
        self.rear = -1
        self.size = 0
        self.maxSize = 5
        self.queue = ["","","","",""]
    #end procedure
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
        #endif
    #end function
    def isFull(self):
        if self.size == self.maxSize:
            return True
        else:
            return False
        #endif
    #endfunction
    def dequeue(self):
        if self.size == 0:
            print("Queue is empty")
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.maxSize
            self.size = self.size - 1
       #endif
    #end procedure
    def enqueue(self,item):
        if self.size == self.maxSize:
            print("Queue is full")
        else:
            self.rear = (self.rear + 1) % self.maxSize
            self.queue[self.rear] = item
            self.size = self.size + 1
       #endif
    #end procedure
    def printQ(self):
        print("size =",self.size)
        print(self.queue)
#end class
A = MyQueue()
A.enqueue("job1")
A.enqueue("job2")
A.enqueue("job3")
A.printQ()
A.enqueue("job4")
A.enqueue("job5")
A.printQ()
A.dequeue()
A.dequeue()
A.dequeue()
A.printQ()
A.enqueue("job6")
A.enqueue("job7")
A.printQ()
A.dequeue()
A.dequeue()
A.dequeue()
A.dequeue()
A.printQ()
A.dequeue()
