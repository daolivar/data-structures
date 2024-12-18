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
