import pytest
from doubly_linked_list import DoublyLinkedList

# Test DoublyLinkedList constructor
def test_linked_list_initialization():
    # Initialize LinkedList with a value
    doubly_linked_list = DoublyLinkedList(10)

    # Check that head and tail are set to the same Node with the correct value
    assert doubly_linked_list.head.value == 10
    assert doubly_linked_list.tail.value == 10
    assert doubly_linked_list.head == doubly_linked_list.tail  # Since it's a single-node list

    # Check that length is correctly set
    assert doubly_linked_list.length == 1

# Test DoublyLinkedList print_list
def test_print_list(capsys):
    # Test Case 1: Print list with a single element
    dll = DoublyLinkedList(10)
    dll.print_list()
    captured = capsys.readouterr()
    assert captured.out == "10\n"

    # Test Case 2: Print list with multiple elements
    dll.append(20)
    dll.append(30)
    dll.print_list()
    captured = capsys.readouterr()
    assert captured.out == "10\n20\n30\n"

    # Test Case 3: Print an empty list
    dll = DoublyLinkedList(10)
    dll.head = None  # Simulate an empty list
    dll.tail = None
    dll.length = 0
    dll.print_list()
    captured = capsys.readouterr()
    assert captured.out == ""

# Test DoublyLinkedList append
def test_append():
    dll = DoublyLinkedList(0)
    dll.pop()

    # Test appending to an empty list
    dll.append(1)
    assert dll.head.value == 1  # Head should be the first node
    assert dll.tail.value == 1  # Tail should also be the first node
    assert dll.head.next is None  # Head next should be None
    assert dll.head.prev is None  # Head prev should be None
    assert dll.tail.next is None  # Tail next should be None
    assert dll.tail.prev is None  # Tail prev should be None
    assert dll.length == 1  # Length should be 1

    # Test appending another element
    dll.append(2)
    assert dll.head.value == 1  # Head remains the first node
    assert dll.tail.value == 2  # Tail should be the new node
    assert dll.head.next == dll.tail  # Head's next should point to the new node
    assert dll.tail.prev == dll.head  # Tail's prev should point to the old head
    assert dll.tail.next is None  # Tail next should be None
    assert dll.length == 2  # Length should be 2

    # Test appending a third element
    dll.append(3)
    assert dll.head.value == 1  # Head remains the same
    assert dll.tail.value == 3  # Tail should be the latest node
    assert dll.head.next.value == 2  # Head's next should still be the second node
    assert dll.tail.prev.value == 2  # Tail's prev should be the second node
    assert dll.length == 3  # Length should be 3

# Test DoublyLinkedList append
def test_append_and_pop():
    # Initialize empty doubly linked list
    dll = DoublyLinkedList(10)

    # Test append method
    dll.append(20)
    dll.append(30)

    # Check if values were added correctly
    assert dll.head.value == 10  # First element
    assert dll.tail.value == 30  # Last element
    assert dll.length == 3  # Length check

    # Test pop method
    popped_node = dll.pop()
    assert popped_node.value == 30  # Check value of popped node
    assert dll.tail.value == 20  # Tail should now be 20
    assert dll.length == 2  # Length should decrease by 1

    popped_node = dll.pop()
    assert popped_node.value == 20  # Check value of popped node
    assert dll.tail.value == 10  # Tail should now be 10
    assert dll.length == 1  # Length should decrease by 1

    popped_node = dll.pop()
    assert popped_node.value == 10  # Check value of popped node
    assert dll.head is None  # List should now be empty
    assert dll.tail is None  # Tail should be None
    assert dll.length == 0  # Length should be zero

    # Test popping from an empty list
    popped_node = dll.pop()
    assert popped_node is None  # Should return None on empty list

# Test DoublyLinkedList prepend
def test_doubly_linked_list_prepend():
    # Setup Doubly Linked List instance
    dll = DoublyLinkedList(0)
    dll.pop()
    
    # Test prepending to an empty list
    assert dll.prepend(10) == True  # Prepend 10
    assert dll.head.value == 10     # Check head value is 10
    assert dll.tail.value == 10     # Check tail value is also 10
    assert dll.length == 1          # Check list length is 1

    # Test prepending to a non-empty list
    assert dll.prepend(20) == True  # Prepend 20
    assert dll.head.value == 20     # Check new head value is 20
    assert dll.tail.value == 10     # Tail should remain 10
    assert dll.head.next.value == 10  # Check head's next points to 10
    assert dll.tail.prev.value == 20  # Check tail's previous points to 20
    assert dll.length == 2          # Check list length is 2

    # Test prepending another value
    assert dll.prepend(30) == True  # Prepend 30
    assert dll.head.value == 30     # Check new head value is 30
    assert dll.tail.value == 10     # Tail should still be 10
    assert dll.head.next.value == 20  # Check head's next points to 20
    assert dll.length == 3          # Check list length is 3
