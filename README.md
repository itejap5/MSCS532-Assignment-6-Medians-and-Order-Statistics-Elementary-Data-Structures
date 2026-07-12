# MSCS532 Assignment 6: Medians, Order Statistics, and Elementary Data Structures

This repository contains my work for Assignment 6 in MSCS 532 Algorithms and Data Structures.

## Project Overview

This assignment is divided into two parts.

### Part 1: Selection Algorithms

Part 1 implements two algorithms for finding the kth smallest element in an array:

* Deterministic Selection using Median of Medians
* Randomized Quickselect

Both implementations support:

* Random input
* Sorted input
* Reverse-sorted input
* Repeated values
* Single-element arrays
* Input validation for k

The program also compares each result with Python's built-in sorted function to confirm correctness.

### Part 2: Elementary Data Structures

Part 2 implements the following data structures from scratch:

* Dynamic array
* Matrix
* Stack using an array
* Queue using an array
* Singly linked list

Each Python file contains comments and docstrings explaining the logic, operations, and time complexity.

## Files Included

```text
MSCS532_Assignment6/
│
├── selection_algorithms.py
├── selection_performance.py
├── elementary_data_structures.py
├── README.md
└── report.md
```

## File Descriptions

### `selection_algorithms.py`

Contains:

* Insertion sort helper function
* Median helper function
* Deterministic Median of Medians algorithm
* Randomized Quickselect algorithm
* Correctness tests

### `selection_performance.py`

Measures the average execution time of both selection algorithms.

The tests use:

* Dataset sizes of 1,000, 5,000, and 10,000
* Random arrays
* Sorted arrays
* Reverse-sorted arrays
* Arrays with repeated elements
* Five trials for each test

### `elementary_data_structures.py`

Contains implementations of:

* DynamicArray
* Matrix
* ArrayStack
* ArrayQueue
* SinglyLinkedList

The file also includes demonstrations of the main operations.

### `report.md`

Contains:

* Problem description
* Algorithm explanations
* Time and space complexity analysis
* Actual test results
* Discussion of performance
* Data structure operation analysis
* Practical applications
* Conclusion

## Requirements

* Python 3.8 or higher
* No external libraries are required

The program only uses Python's standard library.

## How to Run

Open a terminal inside the project folder.

### Run the selection algorithm tests

```bash
python selection_algorithms.py
```

Expected final message:

```text
All selection algorithm tests passed.
```

### Run the selection performance comparison

```bash
python selection_performance.py
```

This displays average execution times for both algorithms across different input sizes and distributions.

### Run the elementary data structure demonstrations

```bash
python elementary_data_structures.py
```

This displays the results of array, matrix, stack, queue, and linked list operations.

## Summary of Findings

Both selection algorithms returned the correct kth smallest values for every test.

Randomized Quickselect was faster than the deterministic Median of Medians algorithm in all measured datasets.

For example, on 10,000 random elements:

* Deterministic Selection: 0.011182 seconds
* Randomized Selection: 0.002060 seconds

On 10,000 reverse-sorted elements:

* Deterministic Selection: 0.022974 seconds
* Randomized Selection: 0.001546 seconds

The deterministic algorithm provides O(n) worst-case performance, but it has more practical overhead. Randomized Quickselect provides expected O(n) performance and was faster in these tests.

All elementary data structure demonstrations also completed successfully.

## Main Operation Complexities

| Data Structure | Operation            |     Complexity |
| -------------- | -------------------- | -------------: |
| Dynamic Array  | Access               |           O(1) |
| Dynamic Array  | Insert/Delete        |           O(n) |
| Matrix         | Access/Update        |           O(1) |
| Stack          | Push/Pop             |           O(1) |
| Queue          | Enqueue              |   O(1) average |
| Queue          | Dequeue              | O(1) amortized |
| Linked List    | Insert at Beginning  |           O(1) |
| Linked List    | Search/Access/Delete |           O(n) |

## Author

Teja Durga Pavan Kumar Ponneboyina
