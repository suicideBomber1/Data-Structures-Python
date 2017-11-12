class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, newdata):
        self.data = newdata

    def set_next(self, newnode):
        self.next = newnode


class Unordered_list:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add_item(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


mylist = Unordered_list()
mylist.add_item(31)
mylist.add_item(77)
mylist.add_item(17)
mylist.add_item(93)
mylist.add_item(26)
mylist.add_item(54)
print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))
mylist.add_item(100)
print(mylist.search(100))
print(mylist.size())
mylist.remove(93)
print(mylist.size())
