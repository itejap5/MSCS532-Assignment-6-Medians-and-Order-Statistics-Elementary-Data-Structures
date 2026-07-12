"""
Assignment 6 - Part 2

This file implements elementary data structures from scratch:

1. Dynamic Array
2. Matrix
3. Stack using an array
4. Queue using an array
5. Singly Linked List

Comments are included throughout the code to explain each step.
"""


class DynamicArray:
    """
    A simple dynamic array implementation using a Python list.

    The class supports:
    - Access
    - Insertion
    - Deletion
    - Display
    """

    def __init__(self):
        # Store array values in a Python list.
        self.data = []

    def access(self, index):
        """
        Return the value at a specific index.

        Time complexity: O(1)
        """

        if index < 0 or index >= len(self.data):
            raise IndexError("Array index is out of range.")

        return self.data[index]

    def insert(self, index, value):
        """
        Insert a value at a specific index.

        Time complexity: O(n) in the worst case because elements
        may need to shift to the right.
        """

        if index < 0 or index > len(self.data):
            raise IndexError("Array insertion index is out of range.")

        self.data.insert(index, value)

    def append(self, value):
        """
        Add a value at the end of the array.

        Average time complexity: O(1)
        """

        self.data.append(value)

    def delete(self, index):
        """
        Delete and return the value at a specific index.

        Time complexity: O(n) because later elements may need
        to shift to the left.
        """

        if index < 0 or index >= len(self.data):
            raise IndexError("Array deletion index is out of range.")

        return self.data.pop(index)

    def display(self):
        """
        Display the entire array.
        """

        print(self.data)


class Matrix:
    """
    A basic matrix implementation using a list of lists.
    """

    def __init__(self, rows, columns, default_value=0):
        """
        Create a matrix with the requested number of rows and columns.
        """

        if rows <= 0 or columns <= 0:
            raise ValueError("Rows and columns must be positive.")

        self.rows = rows
        self.columns = columns

        # Create a separate list for every row.
        self.data = [
            [default_value for _ in range(columns)]
            for _ in range(rows)
        ]

    def access(self, row, column):
        """
        Return the value at a given row and column.

        Time complexity: O(1)
        """

        self._validate_position(row, column)

        return self.data[row][column]

    def update(self, row, column, value):
        """
        Replace the value at a given row and column.

        Time complexity: O(1)
        """

        self._validate_position(row, column)

        self.data[row][column] = value

    def insert_row(self, index, row_values):
        """
        Insert an entire row into the matrix.

        Time complexity: O(r), where r is the number of rows,
        because existing rows may need to shift.
        """

        if index < 0 or index > self.rows:
            raise IndexError("Matrix row index is out of range.")

        if len(row_values) != self.columns:
            raise ValueError(
                "The new row must have the same number of columns."
            )

        self.data.insert(index, row_values.copy())
        self.rows += 1

    def delete_row(self, index):
        """
        Delete and return a row from the matrix.

        Time complexity: O(r) because remaining rows may shift.
        """

        if index < 0 or index >= self.rows:
            raise IndexError("Matrix row index is out of range.")

        deleted_row = self.data.pop(index)
        self.rows -= 1

        return deleted_row

    def _validate_position(self, row, column):
        """
        Check that a row and column are valid.
        """

        if row < 0 or row >= self.rows:
            raise IndexError("Matrix row index is out of range.")

        if column < 0 or column >= self.columns:
            raise IndexError("Matrix column index is out of range.")

    def display(self):
        """
        Display the matrix one row at a time.
        """

        for row in self.data:
            print(row)


class ArrayStack:
    """
    Stack implementation using a Python list.

    A stack follows Last In, First Out, also called LIFO.
    """

    def __init__(self):
        self.items = []

    def push(self, value):
        """
        Add a value to the top of the stack.

        Average time complexity: O(1)
        """

        self.items.append(value)

    def pop(self):
        """
        Remove and return the top value.

        Time complexity: O(1)
        """

        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")

        return self.items.pop()

    def peek(self):
        """
        Return the top value without removing it.

        Time complexity: O(1)
        """

        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack.")

        return self.items[-1]

    def is_empty(self):
        """
        Return True when the stack contains no items.

        Time complexity: O(1)
        """

        return len(self.items) == 0

    def size(self):
        """
        Return the number of stack items.

        Time complexity: O(1)
        """

        return len(self.items)

    def display(self):
        print(self.items)


class ArrayQueue:
    """
    Queue implementation using a Python list.

    A queue follows First In, First Out, also called FIFO.

    This version uses a front index to avoid removing from index 0
    during every dequeue operation.
    """

    def __init__(self):
        self.items = []
        self.front_index = 0

    def enqueue(self, value):
        """
        Add a value to the back of the queue.

        Average time complexity: O(1)
        """

        self.items.append(value)

    def dequeue(self):
        """
        Remove and return the oldest value.

        Amortized time complexity: O(1)
        """

        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")

        value = self.items[self.front_index]
        self.front_index += 1

        # Remove unused items when they become a large portion
        # of the underlying list.
        if (
            self.front_index > 50
            and self.front_index * 2 >= len(self.items)
        ):
            self.items = self.items[self.front_index:]
            self.front_index = 0

        return value

    def peek(self):
        """
        Return the next queue value without removing it.

        Time complexity: O(1)
        """

        if self.is_empty():
            raise IndexError("Cannot peek at an empty queue.")

        return self.items[self.front_index]

    def is_empty(self):
        """
        Check whether the queue has no active items.

        Time complexity: O(1)
        """

        return self.front_index >= len(self.items)

    def size(self):
        """
        Return the number of active items.

        Time complexity: O(1)
        """

        return len(self.items) - self.front_index

    def display(self):
        """
        Display active queue values.
        """

        print(self.items[self.front_index:])


class Node:
    """
    A node used by the singly linked list.
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    """
    Singly linked list implementation.

    Every node stores:
    - A value
    - A reference to the next node
    """

    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginning(self, value):
        """
        Insert a value at the beginning.

        Time complexity: O(1)
        """

        new_node = Node(value)

        # The new node points to the old head.
        new_node.next = self.head

        # The new node becomes the head.
        self.head = new_node

        self.length += 1

    def insert_at_end(self, value):
        """
        Insert a value at the end.

        Time complexity: O(n) because the list is traversed.
        """

        new_node = Node(value)

        # If the list is empty, the new node becomes the head.
        if self.head is None:
            self.head = new_node
            self.length += 1
            return

        current = self.head

        # Move to the last node.
        while current.next is not None:
            current = current.next

        current.next = new_node
        self.length += 1

    def insert_at_position(self, index, value):
        """
        Insert a value at a specific index.

        Time complexity: O(n)
        """

        if index < 0 or index > self.length:
            raise IndexError("Linked list insertion index is invalid.")

        if index == 0:
            self.insert_at_beginning(value)
            return

        new_node = Node(value)
        current = self.head

        # Stop at the node before the insertion position.
        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node

        self.length += 1

    def delete_value(self, value):
        """
        Delete the first node containing the requested value.

        Time complexity: O(n)

        Returns:
            True if a node was deleted.
            False if the value was not found.
        """

        if self.head is None:
            return False

        # Special case: the head contains the value.
        if self.head.value == value:
            self.head = self.head.next
            self.length -= 1
            return True

        previous = self.head
        current = self.head.next

        # Search for the value.
        while current is not None:
            if current.value == value:
                previous.next = current.next
                self.length -= 1
                return True

            previous = current
            current = current.next

        return False

    def access(self, index):
        """
        Return the value at a specific index.

        Time complexity: O(n)
        """

        if index < 0 or index >= self.length:
            raise IndexError("Linked list index is out of range.")

        current = self.head

        for _ in range(index):
            current = current.next

        return current.value

    def search(self, value):
        """
        Search for a value and return its index.

        Returns -1 when the value is not found.

        Time complexity: O(n)
        """

        current = self.head
        index = 0

        while current is not None:
            if current.value == value:
                return index

            current = current.next
            index += 1

        return -1

    def traverse(self):
        """
        Return all linked list values as a normal Python list.

        Time complexity: O(n)
        """

        values = []
        current = self.head

        while current is not None:
            values.append(current.value)
            current = current.next

        return values

    def display(self):
        """
        Display the list using arrows.
        """

        values = self.traverse()

        if not values:
            print("Empty linked list")
            return

        print(" -> ".join(str(value) for value in values) + " -> None")


def demonstrate_dynamic_array():
    """
    Demonstrate array operations.
    """

    print("\nDYNAMIC ARRAY DEMONSTRATION")

    array = DynamicArray()

    array.append(10)
    array.append(20)
    array.append(30)

    print("After appending values:")
    array.display()

    array.insert(1, 15)

    print("After inserting 15 at index 1:")
    array.display()

    print("Value at index 2:", array.access(2))

    deleted_value = array.delete(0)

    print("Deleted value:", deleted_value)
    print("Array after deletion:")
    array.display()


def demonstrate_matrix():
    """
    Demonstrate matrix operations.
    """

    print("\nMATRIX DEMONSTRATION")

    matrix = Matrix(2, 3)

    matrix.update(0, 0, 10)
    matrix.update(0, 1, 20)
    matrix.update(1, 2, 30)

    print("Matrix after updates:")
    matrix.display()

    matrix.insert_row(1, [40, 50, 60])

    print("Matrix after inserting a row:")
    matrix.display()

    deleted_row = matrix.delete_row(0)

    print("Deleted row:", deleted_row)
    print("Matrix after deleting a row:")
    matrix.display()


def demonstrate_stack():
    """
    Demonstrate stack operations.
    """

    print("\nSTACK DEMONSTRATION")

    stack = ArrayStack()

    stack.push("Task 1")
    stack.push("Task 2")
    stack.push("Task 3")

    print("Stack after pushes:")
    stack.display()

    print("Top item:", stack.peek())
    print("Popped item:", stack.pop())

    print("Stack after pop:")
    stack.display()


def demonstrate_queue():
    """
    Demonstrate queue operations.
    """

    print("\nQUEUE DEMONSTRATION")

    queue = ArrayQueue()

    queue.enqueue("Customer 1")
    queue.enqueue("Customer 2")
    queue.enqueue("Customer 3")

    print("Queue after enqueue operations:")
    queue.display()

    print("Next item:", queue.peek())
    print("Dequeued item:", queue.dequeue())

    print("Queue after dequeue:")
    queue.display()


def demonstrate_linked_list():
    """
    Demonstrate singly linked list operations.
    """

    print("\nLINKED LIST DEMONSTRATION")

    linked_list = SinglyLinkedList()

    linked_list.insert_at_beginning(20)
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_end(30)
    linked_list.insert_at_position(2, 25)

    print("Linked list after insertions:")
    linked_list.display()

    print("Value at index 2:", linked_list.access(2))
    print("Index of value 30:", linked_list.search(30))

    linked_list.delete_value(25)

    print("Linked list after deleting 25:")
    linked_list.display()


def main():
    """
    Run all demonstrations.
    """

    demonstrate_dynamic_array()
    demonstrate_matrix()
    demonstrate_stack()
    demonstrate_queue()
    demonstrate_linked_list()


if __name__ == "__main__":
    main()