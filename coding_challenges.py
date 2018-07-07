from itertools import groupby
from collections import defaultdict
from random import randint

def most_active_period(data):
    """Given list of authors and years during which they were active, returns
    start and end dates of periods in which the most authors were active"""
    active_yrs = []
    for author in data:
        yrs = [yr for yr in range(author[1], author[2]+1)]
        active_yrs.extend(yrs)
    active_yrs = sorted(active_yrs)
    yrs_grouped = groupby(active_yrs)
    count_authors = defaultdict(list)
    for yr, group in yrs_grouped:
        k = sum(1 for _ in group)
        count_authors[k].append(yr)
    print count_authors 
    max_authors = max(count_authors)
    lst_yrs = count_authors[max_authors]
    for i in range(len(lst_yrs)-1):
        # If more than one period had max number of authors,
        # return first period
        if lst_yrs[i]+1 < lst_yrs[i+1]:
            return (lst_yrs[0], lst_yrs[i])
    return (lst_yrs[0], lst_yrs[-1])

    
data = [
('Alice', 1901, 1950),
('Bob',   1920, 1960),
('Carol', 1908, 1945),
('Dave',  1951, 1960),
('Eve',   1955, 1985),
]

# print most_active_period(data)

def check(king, queen):
    """ 
    >>> check("D6", "H6")
    True
    
    >>> check("E6", "E4")
    True
    
    >>> check("B7", "D5")
    True
    
    >>> check("A1", "H8")
    True
    
    >>> check("A8", "H1")
    True
    
    >>> check("D6", "H7")
    False
    
    >>> check("E6", "F4")
    False
    """
    return (king[1] == queen[1]) or (king[0] == queen[0]) or (abs(ord(king[1])-ord(queen[1])) == abs(ord(king[0])-ord(queen[0])))

# class Node(object):
#     """Class in a linked list."""

#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

#     def as_string(self):
#         """Represent data for this node and its successors as a string.

#         >>> Node(3).as_string()
#         '3'

#         >>> Node(3, Node(2, Node(1))).as_string()
#         '321'
#         """

#         out = []
#         n = self

#         while n:
#             out.append(str(n.data))
#             n = n.next

#         return "".join(out)


# def remove_node(node):
#     """Given a node in a linked list, remove it.

#     Remove this node from a linked list. Note that we do not have access to
#     any other nodes of the linked list, like the head or the tail.

#     Does not return anything; changes list in place.
    
#     >>> four_node = Node(4)
#     >>> three_node = Node(3, four_node)
#     >>> two_node = Node(2, three_node)
#     >>> one_node = Node(1, two_node)

#     >>> remove_node(three_node)
#     >>> one_node.as_string()
#     '124'

#     """

#     node.data = node.next.data
#     node.next = node.next.next

def recursive_index(needle, haystack, i=0):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.

    >>> lst = ["hey", "there", "you"] 
    >>> recursive_index("hey", lst)
    0
    >>> recursive_index("you", lst)
    2
    >>> recursive_index("porcupine", lst)
    Item not found

    """

    if i == len(haystack):
        print "Item not found"
        return
    elif haystack[i] == needle:
        return i
    else:
        return recursive_index(needle, haystack, i+1)

def sum_list_recursively(arr):
    """
    Calculate sum of list of integers recursively

    >>> sum_list_recursively([5, 5])
    10

    >>> sum_list_recursively([-5, 10, 4])
    9

    >>> sum_list_recursively([20])
    20
    """
    if arr == []:
        return 0
    else:
        return arr[0] + sum_list_recursively(arr[1:])


class Node(object):
    """
    >>> node1 = Node(1)
    >>> node2 = Node(2)
    >>> node3 = Node(3)
    >>> node4 = Node(4)
    >>> node5 = Node(5)
    >>> node1.children = [node2, node3]
    >>> node3.children = [node4, node5]

    >>> node1.node_found(6)
    False
    >>> node1.node_found(5)
    True
    """
    
    def __init__(self, data, children=None):
        self.data = data
        self.children = children or []
        

    def node_found(self, data):
        if self.data == data:
            return True
        else:
            for child in self.children:
                n = child.node_found(data)
                if n:
                    return True
            return False


def prime_generator(n):
    """Generates first n primes
    
    >>> prime_generator(9)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]

    """
    if n == 1:
        return [2]
    elif n == 2:
        return [2, 3]
    else:
        count_primes = 2
        list_primes = [2, 3]
        to_test = 5
        while count_primes < n:
            if any(divisor for divisor in range(3, int(to_test**.5)+1, 2) if to_test%divisor==0):
                to_test+=2
                continue
            else:
                count_primes+=1
                list_primes.append(to_test)
                to_test+=2
    return list_primes


vocab = {'i', 'a', 'ten', 'oodles', 'ford', 'inner', 'to', 'night', 'ate', 'noodles', 
            'for', 'dinner', 'tonight'}

def parse(phrase, length, result="", combinations=[]):
    """
    >>> phrase = "iatenoodlesfordinnertonight"
    >>> length = len(phrase)
    >>> parse(phrase, length)
    ['i a ten oodles for dinner to night', 'i a ten oodles for dinner tonight', 'i a ten oodles ford inner to night', 'i a ten oodles ford inner tonight', 'i ate noodles for dinner to night', 'i ate noodles for dinner tonight', 'i ate noodles ford inner to night', 'i ate noodles ford inner tonight']
    """

    for i in range(1, length+1):
        prefix = phrase[:i]
        if prefix in vocab:
            if i == length:
                result+=prefix
                combinations.append(result)
            parse(phrase[i:], length-i, result+prefix+" ", combinations)
    return combinations


class PersonNode(object):
    """A node in a graph representing a person.

    This is created with a name and, optionally, a list of adjacent nodes.
    """

    def __init__(self, name, adjacent=[]):
        self.name = name
        self.adjacent = set(adjacent)

    def __repr__(self):
        return "<PersonNode %s>" % self.name

class FriendGraph(object):
    """Graph to keep track of social connections."""

    def __init__(self):
        """Create an empty graph.

        We keep a dictionary to map people's names -> nodes.
        """

        self.nodes = {}

    def add_person(self, name):
        """Add a person to our graph."""

        if name not in self.nodes:
            # Be careful not to just add them a second time -- otherwise,
            # if we accidentally added someone twice, we'd clear our their list
            # of friends!
            self.nodes[name] = PersonNode(name)

    def set_friends(self, name, friend_names):
        """Set two people as friends."""
        person = self.nodes[name]

        for friend_name in friend_names:
            friend = self.nodes[friend_name]

            # Since adjacent is a set, we don't care if we're adding duplicates ---
            # it will only keep track of each relationship once. We do want to
            # make sure that we're adding both directions for the relationship.
            person.adjacent.add(friend)
            friend.adjacent.add(person)

    def are_connected(self, name1, name2):
        """Is this name1 friends with name2?
        >>> f = FriendGraph()
        >>> f.add_person("Frodo")
        >>> f.add_person("Sam")
        >>> f.add_person("Gandalf")
        >>> f.add_person("Merry")
        >>> f.add_person("Pippin")
        >>> f.add_person("Treebeard")
        >>> f.add_person("Sauron")
        >>> f.add_person("Dick Cheney")
        >>> f.set_friends("Frodo", ["Sam", "Gandalf", "Merry", "Pippin"])
        >>> f.set_friends("Sam", ["Merry", "Pippin", "Gandalf"])
        >>> f.set_friends("Merry", ["Pippin", "Treebeard"])
        >>> f.set_friends("Pippin", ["Treebeard"])
        >>> f.set_friends("Sauron", ["Dick Cheney"])
        >>> f.are_connected("Sam", "Treebeard")
        True
        >>> f.are_connected("Frodo", "Sauron")
        False
        """       
        seen = set()
        seen.add(self.nodes[name1])
        to_visit = [self.nodes[name1]]
        
        while to_visit:
            current = to_visit.pop()
            if current.name == name2:
                return True
            else:
                for friend in current.adjacent - seen:
                    to_visit.append(self.nodes[friend.name])
                    seen.add(self.nodes[friend.name])
                    
        return False



def guess_num(num):
    """
    >>> guess_num(85)
    (85, 6)

    """
    num_guesses = 1
    floor = 0
    ceiling = 100
    guess = 50
    while guess != num:
        if guess < num:
            num_guesses += 1
            floor = guess
            guess = (floor+ceiling)/2
        elif guess > num:
            num_guesses += 1
            ceiling = guess
            guess = (floor+ceiling)/2
    return (guess, num_guesses)

def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive)"""
    lucky_nums = set()
    while len(lucky_nums) < n:
        lucky_nums.add(randint(1,10))
        return sorted(list(lucky_nums))

class Node(object):
    """Linked list node."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_rev_string(self):
        """Represent data for this node and its successors as a string.

        >>> l1 = Node(3)
        >>> l1.as_rev_string()
        '3'

        >>> l1 = Node(3, Node(2, Node(1)))
        >>> l1.as_rev_string()
        '123'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(reversed(out))
        
def add_linked_lists(l1, l2):
    """Given two linked lists representing numbers with digits reversed,
    add the numbers and return sum as another linked list with digits 
    reversed.
    >>> l1 = Node(3, Node(2, Node(1)))
    >>> l2 = Node(6, Node(5, Node(4)))
    >>> test = add_linked_lists(l1, l2)
    >>> test.as_rev_string()
    '579'
    """
    num1 = int(l1.as_rev_string())
    num2 = int(l2.as_rev_string())
    sum_nums = num1 + num2
    sum_as_string = str(sum_nums)[::-1]
    if len(sum_as_string) == 1:
        return Node(sum_as_string[0])
    else:
        node = Node(int(sum_as_string[0]))
        head = node
        rest_of_string = sum_as_string[1:]
        while rest_of_string:
            next = Node(int(rest_of_string[0]))
            node.next = next
            node = next
            rest_of_string = rest_of_string[1:]
        return head
        


if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print