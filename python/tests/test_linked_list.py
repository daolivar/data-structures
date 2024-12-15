# tests/test_linked_list.py
import pytest
from linked_list import LinkedList

# Test LinkedList constructor
def test_linked_list_initialization():
    # Initialize LinkedList with a value
    linked_list = LinkedList(10)

    # Check that head and tail are set to the same Node with the correct value
    assert linked_list.head.value == 10
    assert linked_list.tail.value == 10
    assert linked_list.head == linked_list.tail  # Since it's a single-node list

    # Check that length is correctly set
    assert linked_list.length == 1

# Test LinkedList print_list
def test_print_list(capsys):
    # Create a LinkedList with initial value
    linked_list = LinkedList(10)

    # Append a new value
    linked_list.append(20)

    # Append another value
    linked_list.append(30)

    # Call print_list method to print the linked list values
    linked_list.print_list()

    # Capture the output
    captured = capsys.readouterr()

    # Expected output is "10\n" since the list has only one node with value 10
    assert captured.out == "10\n20\n30\n"

# Test Linked List append
def test_append():
    # Create a LinkedList with initial value
    linked_list = LinkedList(10)

    # Append a new value and check the return value
    assert linked_list.append(20) is True

    # Check that the tail's value is updated correctly
    assert linked_list.tail.value == 20

    # Check that the list length is updated correctly
    assert linked_list.length == 2

    # Check that the appended node is linked correctly
    assert linked_list.head.next.value == 20

    # Append another value and check the return value
    assert linked_list.append(30) is True

    # Check tail and length after the second append
    assert linked_list.tail.value == 30
    assert linked_list.length == 3
    assert linked_list.head.next.next.value == 30

    # Use pop method to make the list empty
    linked_list.pop()  # Pops 30
    linked_list.pop()  # Pops 20
    linked_list.pop()  # Pops 10 (list is now empty)

    # Append a value to the empty list and check the return value
    assert linked_list.append(40) is True

    # Check that the head and tail point to the same node
    assert linked_list.head.value == 40
    assert linked_list.tail.value == 40

    # Check that the list length is updated to 1
    assert linked_list.length == 1

    # Append another value to the previously empty list and check the return value
    assert linked_list.append(50) is True

    # Verify the append after the list was empty
    assert linked_list.tail.value == 50
    assert linked_list.length == 2
    assert linked_list.head.next.value == 50


# Test Linked List pop
def test_pop():
    # Case 1: Popping from an empty list
    empty_list = LinkedList(10)
    empty_list.pop()  # Removes the only element
    assert empty_list.pop() is None  # Should return None, as list is now empty

    # Case 2: Popping from a single-node list
    single_node_list = LinkedList(10)
    popped_node = single_node_list.pop()
    assert popped_node.value == 10
    assert single_node_list.head is None
    assert single_node_list.tail is None
    assert single_node_list.length == 0

    # Case 3: Popping from a multi-node list
    multi_node_list = LinkedList(10)
    multi_node_list.append(20)
    multi_node_list.append(30)

    # Pop the last node (30)
    popped_node = multi_node_list.pop()
    assert popped_node.value == 30
    assert multi_node_list.tail.value == 20  # Tail should be updated to 20
    assert multi_node_list.length == 2       # Length should be updated to 2

    # Pop another node (20)
    popped_node = multi_node_list.pop()
    assert popped_node.value == 20
    assert multi_node_list.tail.value == 10  # Tail should now be 10
    assert multi_node_list.length == 1       # Length should be 1

    # Finally, pop the last node (10)
    popped_node = multi_node_list.pop()
    assert popped_node.value == 10
    assert multi_node_list.head is None
    assert multi_node_list.tail is None
    assert multi_node_list.length == 0

# Test Linked List prepend
def test_prepend():
    # Case 1: Prepend to an empty list
    linked_list = LinkedList(10)
    linked_list.pop()  # Now the list is empty

    # Prepend a value to the empty list and check the return value
    assert linked_list.prepend(5) is True

    # Check if head and tail both point to the new node
    assert linked_list.head.value == 5
    assert linked_list.tail.value == 5
    assert linked_list.length == 1

    # Case 2: Prepend to a non-empty list
    assert linked_list.prepend(3) is True  # Check the return value

    # Check if head is updated and points to the new node
    assert linked_list.head.value == 3
    assert linked_list.length == 2

    # Check if the new head's next node is the previous head
    assert linked_list.head.next.value == 5

    # Prepend another value and check the return value
    assert linked_list.prepend(1) is True

    # Verify the new head and the next pointers
    assert linked_list.head.value == 1
    assert linked_list.head.next.value == 3
    assert linked_list.length == 3

# Test Linked List pop_first
def test_pop_first():
    # Case 1: Pop from an empty list
    linked_list = LinkedList(10)
    linked_list.pop()  # Make the list empty

    # Popping from an empty list should return None
    assert linked_list.pop_first() is None
    assert linked_list.head is None
    assert linked_list.tail is None
    assert linked_list.length == 0

    # Case 2: Pop from a list with a single element
    linked_list.append(1)  # Add one element to the list

    # Popping the only element should return the node and make the list empty
    popped_node = linked_list.pop_first()
    assert popped_node.value == 1
    assert linked_list.head is None
    assert linked_list.tail is None
    assert linked_list.length == 0

    # Case 3: Pop from a list with multiple elements
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    # Popping the first element
    popped_node = linked_list.pop_first()
    assert popped_node.value == 1
    assert linked_list.head.value == 2  # Head should now be the second node
    assert linked_list.length == 2

    # Pop another element (which was the second)
    popped_node = linked_list.pop_first()
    assert popped_node.value == 2
    assert linked_list.head.value == 3  # Head should now be the third node
    assert linked_list.length == 1

    # Pop the last element
    popped_node = linked_list.pop_first()
    assert popped_node.value == 3
    assert linked_list.head is None
    assert linked_list.tail is None
    assert linked_list.length == 0
