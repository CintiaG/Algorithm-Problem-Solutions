#!/usr/bin/env python3
class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data; self.prev = prev; self.next = next
    def __del__(self):
        del self.data; self.prev = None; self.next = None
    def __str__(self):
        return "(%s)" % str(self.data)
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def get_prev(self):
        return self.prev
    def set_data(self, data):
        self.data = data
    def set_next(self, next):
        self.next = next
    def set_prev(self, prev):
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.size = 0; self.front = None; self.back = None; self.iter_curr = None
    def __del__(self):
        self.clear()
    def __len__(self):
        return self.size
    def __str__(self):
        if self.empty():
            return ""
        curr = self.front; out = str(curr)
        for _ in range(self.size-1):
            curr = curr.get_next(); out += "->%s" % str(curr)
        return out
    def __iter__(self):
        return self
    def __next__(self):
        if self.iter_curr is None:
            self.iter_curr = self.front; raise StopIteration
        else:
            tmp = self.iter_curr.get_data(); self.iter_curr = self.iter_curr.get_next(); return tmp
    def clear(self):
        self.size = 0; self.front = None; self.back = None; self.iter_curr = None
    def empty(self):
        return self.size == 0
    def get_back(self):
        if self.back is None:
            return None
        else:
            return self.back.get_data()
    def get_front(self):
        if self.front is None:
            return None
        else:
            return self.front.get_data()
    def insert_back(self, data):
        self.back = Node(data, prev = self.back)
        if self.back.get_prev() is not None:
            self.back.get_prev().set_next(self.back)
        else:
            self.front = self.back; self.iter_curr = self.front
        self.size += 1
    def insert_front(self, data):
        self.front = Node(data, next = self.front); self.iter_curr = self.front
        if self.front.get_next() is not None:
            self.front.get_next().set_prev(self.front)
        else:
            self.back = self.front
        self.size += 1
    def remove_back(self):
        if self.empty():
            return False
        tmp = self.back.get_prev(); del self.back; self.back = tmp; self.size -= 1
        if self.empty():
            self.front = None; self.iter_curr = None
        return True
    def remove_front(self):
        if self.empty():
            return False
        tmp = self.front.get_next(); del self.front; self.front = tmp; self.iter_curr = tmp; self.size -= 1
        if self.empty():
            self.back = None
        return True
    def remove(self, data):
        curr = self.front
        while curr is not None:
            if data == curr.get_data():
                if curr == self.front:
                    self.remove_front()
                elif curr == self.back:
                    self.remove_back()
                else:
                    curr.get_prev().set_next(curr.get_next())
                    curr.get_next().set_prev(curr.get_prev())
                    del curr; self.size -= 1; return True
            else:
                curr = curr.get_next()
        return False
    def __delitem__(self, index):
        if index < 0:
            raise IndexError("Index must be at least 0")
        elif self.size == 0:
            raise IndexError("Removing from empty list")
        elif index >= self.size:
            raise IndexError("Index is too large")
        if index == 0:
            self.remove_front()
        elif index == self.size-1:
            self.remove_back()
        else:
            curr = self.front
            for _ in range(index):
                curr = curr.get_next()
            curr.get_prev().set_next(curr.get_next())
            curr.get_next().set_prev(curr.get_prev())
            del curr; self.size -= 1
    def __getitem__(self, index):
        if index < 0:
            raise IndexError("Index must be at least 0")
        elif index >= self.size:
            raise IndexError("Index is too large")
        curr = self.front
        for _ in range(index):
            curr = curr.get_next()
        return curr.get_data()
    def __setitem__(self, index, data):
        if index < 0:
            raise IndexError("Index must be at least 0")
        elif index > self.size:
            raise IndexError("Index is too large")
        if index == 0:
            self.insert_front(data)
        elif index == self.size:
            self.insert_back(data)
        else:
            curr = self.front
            for _ in range(index):
                curr = curr.get_next()
            curr = Node(data, prev = curr.get_prev(), next = curr)
            curr.get_prev().set_next(curr)
            curr.get_next().set_prev(curr)
            self.size += 1
    def get(self, data):
        curr = self.front
        while curr is not None:
            if data == curr.get_data():
                return curr.get_data()
            curr = curr.get_next()
        return None
    def __contains__(self, data):
        return self.get(data) is not None

class DoubleEndedQueue:
    def __init__(self):
        self.LL = LinkedList()
    def __len__(self):
        return len(self.LL)
    def clear(self):
        self.LL.clear()
    def empty(self):
        return self.LL.empty()
    def check_back(self):
        return self.LL.get_back()
    def check_front(self):
        return self.LL.get_front()
    def dequeue_back(self):
        tmp = self.LL.get_back(); self.LL.remove_back(); return tmp
    def dequeue_front(self):
        tmp = self.LL.get_front(); self.LL.remove_front(); return tmp
    def enqueue_back(self, data):
        self.LL.insert_back(data)
    def enqueue_front(self, data):
        self.LL.insert_front(data)

class Queue:
    def __init__(self):
        self.DEQ = DoubleEndedQueue()
    def __len__(self):
        return len(self.DEQ)
    def clear(self):
        self.DEQ.clear()
    def empty(self):
        return self.DEQ.empty()
    def check(self):
        return self.DEQ.check_front()
    def dequeue(self):
        return self.DEQ.dequeue_front()
    def enqueue(self, data):
        return self.DEQ.enqueue_back(data)

class Stack:
    def __init__(self):
        self.DEQ = DoubleEndedQueue()
    def __len__(self):
        return len(self.DEQ)
    def clear(self):
        self.DEQ.clear()
    def empty(self):
        return self.DEQ.empty()
    def pop(self):
        return self.DEQ.dequeue_back()
    def push(self, data):
        return self.DEQ.enqueue_back(data)
    def top(self):
        return self.DEQ.check_back()