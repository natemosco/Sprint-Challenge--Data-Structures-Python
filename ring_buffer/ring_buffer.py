from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == self.capacity:
            if self.current == None:
                self.current = self.storage.head
            if self.current == self.storage.tail:
                self.current.value = item  # swap item at current index
                self.current = self.storage.head  # increment index by wrapping around to front
            else:
                self.current.value = item
                self.current = self.current.next
        else:
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        if self.storage.length == 0:
            return list_buffer_contents
        else:
            list_buffer_contents = [0] * self.storage.length
            temp_var = self.current
            self.current = self.storage.head
            for i in range(0, self.storage.length):
                list_buffer_contents[i] = self.current.value
                self.current = self.current.next
            self.current = temp_var
            return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
