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
    linked_list = LinkedList(10) # TODO add more elements to print_list test when append is implemented

    # Call print_list method to print the linked list values
    linked_list.print_list()

    # Capture the output
    captured = capsys.readouterr()

    # Expected output is "10\n" since the list has only one node with value 10
    assert captured.out == "10\n"
