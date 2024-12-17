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

# Test Linked List get
def test_get():
    # Case 1: Get from an empty list
    linked_list = LinkedList(10)
    linked_list.pop()  # Make the list empty

    # Trying to get from an empty list should return None
    assert linked_list.get(0) is None

    # Case 2: Get from a list with a single element
    linked_list.append(1)

    # Getting the first element should return the node with value 1
    node = linked_list.get(0)
    assert node is not None
    assert node.value == 1

    # Case 3: Get from a list with multiple elements
    linked_list.append(2)
    linked_list.append(3)

    # Get the first element
    node = linked_list.get(0)
    assert node is not None
    assert node.value == 1

    # Get the second element
    node = linked_list.get(1)
    assert node is not None
    assert node.value == 2

    # Get the third element
    node = linked_list.get(2)
    assert node is not None
    assert node.value == 3

    # Case 4: Index out of bounds
    assert linked_list.get(-1) is None  # Negative index
    assert linked_list.get(3) is None   # Index greater than length - 1

# Test Linked List set_value
def test_set_value():
    # Case 1: Set value on an empty list
    linked_list = LinkedList(10)
    linked_list.pop()  # Now the list is empty

    # Trying to set a value on an empty list should return False
    assert linked_list.set_value(0, 100) is False

    # Case 2: Set value on a valid index
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    # Set value at index 1 (should change 20 to 25)
    assert linked_list.set_value(1, 25) is True
    assert linked_list.get(1).value == 25  # Verify the value was updated

    # Set value at index 0 (should change 10 to 15)
    assert linked_list.set_value(0, 15) is True
    assert linked_list.get(0).value == 15  # Verify the value was updated

    # Set value at index 2 (should change 30 to 35)
    assert linked_list.set_value(2, 35) is True
    assert linked_list.get(2).value == 35  # Verify the value was updated

    # Case 3: Set value with an invalid index
    assert linked_list.set_value(3, 40) is False  # Index 3 is out of bounds

    # Case 4: Negative index
    assert linked_list.set_value(-1, 100) is False  # Negative index should return False

# Test Linked List insert
def test_insert():
    # Case 1: Insert into an empty list (should behave like prepend)
    linked_list = LinkedList(10)
    linked_list.pop()  # Make the list empty

    assert linked_list.insert(0, 5) is True
    assert linked_list.head.value == 5
    assert linked_list.tail.value == 5
    assert linked_list.length == 1

    # Case 2: Insert at the head (index 0)
    linked_list.insert(0, 1)  # Insert 1 at the head
    assert linked_list.head.value == 1
    assert linked_list.head.next.value == 5
    assert linked_list.length == 2

    # Case 3: Insert at the tail (index == length)
    linked_list.insert(2, 15)  # Insert 15 at the tail
    assert linked_list.tail.value == 15
    assert linked_list.length == 3

    # Case 4: Insert in the middle (index 1)
    linked_list.insert(1, 7)  # Insert 7 at index 1
    assert linked_list.get(1).value == 7
    assert linked_list.length == 4
    assert linked_list.get(1).value == 7
    assert linked_list.get(2).value == 5

    # Case 5: Insert at invalid index (out of bounds)
    assert linked_list.insert(5, 20) is False  # Index is out of bounds
    assert linked_list.length == 4  # Length should remain unchanged

    # Case 6: Insert at negative index (invalid)
    assert linked_list.insert(-1, 100) is False  # Negative index should return False
    assert linked_list.length == 4  # Length should remain unchanged

# Test Linked List remove
def test_remove():
    # Create a LinkedList with multiple values
    linked_list = LinkedList(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.append(40)

    # Case 1: Remove from the head (index 0)
    removed = linked_list.remove(0)
    assert removed.value == 10  # Check if the correct node was removed
    assert linked_list.head.value == 20  # Verify the head has been updated
    assert linked_list.length == 3  # Length should be reduced by 1

    # Case 2: Remove from the tail (last index)
    removed = linked_list.remove(2)  # Index 2 is the last element (40)
    assert removed.value == 40
    assert linked_list.tail.value == 30  # Tail should now be 30
    assert linked_list.length == 2  # Length should be reduced by 1

    # Case 3: Remove from the middle
    linked_list.append(50)  # Add a value to make the list [20, 30, 50]
    removed = linked_list.remove(1)  # Remove the element at index 1 (30)
    assert removed.value == 30
    assert linked_list.head.next.value == 50  # 20 -> 50 after removal
    assert linked_list.length == 2  # Length should be reduced by 1

    # Case 4: Remove at an invalid index (out of bounds)
    assert linked_list.remove(5) is None  # No node should be removed
    assert linked_list.length == 2  # Length should remain unchanged

    # Case 5: Negative index (invalid)
    assert linked_list.remove(-1) is None  # Negative index should return None
    assert linked_list.length == 2  # Length should remain unchanged

    # Case 6: Remove the last remaining elements
    linked_list.remove(0)  # Removes 20
    linked_list.remove(0)  # Removes 50 (list becomes empty)
    assert linked_list.head is None
    assert linked_list.tail is None
    assert linked_list.length == 0


