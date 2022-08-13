# O(1)
# O(log n)
# O(n)
# O(n log n)
# O(n2)
# O(2n)
# O(n!)

###############################################################################
# Dict
a = 'hello'
# print(hash(a))
# print(hash(a))
# print(hash(a))
# print(hash(a))

from collections import OrderedDict

d = OrderedDict([('one', 1), ('two', 2), ('three', 3)])

# print(d)

d['four'] = 4

# print(d)
#
# print(list(reversed(d)))
#
# d.move_to_end('one')
#
# print(d)
# print(d.popitem(last=False))

from collections import defaultdict

food = defaultdict(list)

print(food)

food['fruits']
print(food)
food['fruits'].append('apple')
food['fruits'].append('banana')

print(food)
food['meet'].append('beef')
food['meet'].append('pork')

print(food)
print(food.keys())

from collections import ChainMap

bikes = {
    'Harley Davidson': 40_000,
    'Kawasaki': 10_000,
    'Honda': 15_000,
    'BMW': 20_000
}

cars = {
    'Toyota': 30_000,
    'Tesla': 100_000,
    'BMW': 50_000,
}

chain = ChainMap(cars, bikes)

print(chain['BMW'])

from types import MappingProxyType

proxy = MappingProxyType(cars)

print(proxy['BMW'])
# proxy['BMW'] = 100_000
cars['BMW'] = 100_000
print(proxy['BMW'])

###############################################################################
# List and tuple
from collections import namedtuple

Point = namedtuple('Point', 'x y')
point = Point(1, 2)

print(point)
print(point.x)
print(point.y)
print(point[0])

print(point.x + point.y)

Developer = namedtuple(
    'Developer',
    ['name',  'experience',  'language'],
    defaults=['Junior', 'Python']
)

oleg = Developer('Oleg', 'Senior', 'C++')

print(oleg)

from array import array

my_array = array('I', (123, 345, 567))
my_array2 = array('B', (1, 2, 3))

print(my_array)
print(my_array2)

print(my_array[0])
my_array.append(234)
# my_array.append('a')

print(my_array)

# Numpy, Pandas
###############################################################################
# if elem in my_set:
#     ...
from collections import Counter

klass = Counter()
klass.update({'girls'})
klass.update({'girls'})
klass.update({'girls'})
klass.update({'boys'})
klass.update({'boys'})
print(klass)
print(klass['girls'])

###############################################################################
# Stack
from collections import deque

q = deque()
print('-' * 80)
q.append('Oleg')
q.append('Alex')
q.append('Vlad')
q.append('Lev')
q.appendleft('Tetiana')
print(q)
q.pop()
q.popleft()
print(q)

from queue import LifoQueue

lq = LifoQueue()
lq.put('Alex')
lq.put('Oleg')
lq.put('Vlad')
lq.put('Lev')
print(lq.queue)
print(lq.qsize())
name = lq.get()
print(name)
name = lq.get()
print(name)
lq.put('Tetiana')
print(lq.queue)
print(lq.get())
print(lq.get())
print(lq.get())
# print(lq.get_nowait())

# Priority Queue
priority = [(2, 'sql'), (1, 'python')]

priority.append((3, 'html'))

print(priority)
priority.sort(reverse=True)
print(priority)
print(priority.pop())

import bisect

priority = [(2, 'sql'), (1, 'python'), (3, 'html')]

bisect.insort(priority, (0.5, 'party'))

print(priority)

import heapq
# 0(log n)

q = []

heapq.heappush(q, (2, 'sql'))
heapq.heappush(q, (1, 'python'))
heapq.heappush(q, (3, 'html'))

print(q)
print(heapq.heappop(q))
print(heapq.heappop(q))

from queue import PriorityQueue

q = PriorityQueue()
q.put((2, 'sql'))
q.put((1, 'python'))
q.put((3, 'html'))

print(q.queue)
q.get()
print(q.queue)
###############################################################################
print('*' * 80)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next

        nodes.append("None")
        return ' -> '.join(nodes)


l_list = LinkedList()
print(l_list)

node_1 = Node('a')
node_2 = Node('b')
node_3 = Node('c')

l_list.head = node_1
node_1.next = node_2
node_2.next = node_3

print(l_list)


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def add_first(self, node: Node):
        node.next = self.head
        self.head = node

    def add_last(self, node: Node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass

        current_node.next = node

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next

        nodes.append("None")
        return ' -> '.join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


l_list = LinkedList(['a', 'b', 'c', 'd'])
print(l_list)

l_list.add_last(Node('e'))
l_list.add_last(Node('f'))
print(l_list)

l_list.add_first(Node('1'))
l_list.add_first(Node('2'))
print(l_list)
