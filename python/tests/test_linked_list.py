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
# TODO modify test for case on empty list when pop method is available
def test_append():
    # Create a LinkedList with initial value
    linked_list = LinkedList(10)

    # Append a new value
    linked_list.append(20)

    # Check that the tail's value is updated correctly
    assert linked_list.tail.value == 20

    # Check that the list length is updated correctly
    assert linked_list.length == 2

    # Check that the appended node is linked correctly
    assert linked_list.head.next.value == 20

    # Append another value
    linked_list.append(30)

    # Check tail and length after the second append
    assert linked_list.tail.value == 30
    assert linked_list.length == 3
    assert linked_list.head.next.next.value == 30
