"""
Assignment 6 - Part 1

This file contains two algorithms for finding the kth smallest
element in an array:

1. Deterministic Selection using Median of Medians
2. Randomized Quickselect

The value of k starts from 1.

For example:
k = 1 returns the smallest element.
k = 2 returns the second smallest element.
"""

import random


def insertion_sort(values):
    """
    Sort a small list using insertion sort.

    Median of Medians divides the input into small groups of five.
    Insertion sort works well for these small groups because it is
    simple and has very little overhead.

    Parameters: values: A list of numbers.

    Returns: A new sorted list.
    """

    # Make a copy so the original list is not changed.
    sorted_values = values.copy()

    # Start from the second element.
    for i in range(1, len(sorted_values)):
        current_value = sorted_values[i]
        j = i - 1

        # Move larger values one position to the right.
        while j >= 0 and sorted_values[j] > current_value:
            sorted_values[j + 1] = sorted_values[j]
            j -= 1

        # Insert the current value in its correct position.
        sorted_values[j + 1] = current_value

    return sorted_values


def find_median(values):
    """
    Find the median of a small list.

    The list is first sorted. The middle value is then returned.

    Parameters:
        values: A non-empty list of numbers.

    Returns:
        The median value.
    """

    sorted_values = insertion_sort(values)

    # Integer division gives the middle index.
    middle_index = len(sorted_values) // 2

    return sorted_values[middle_index]


def deterministic_select(values, k):
    """
    Find the kth smallest element using Median of Medians.

    This algorithm has worst-case O(n) time complexity.

    Parameters:
        values: A list of comparable values.
        k: The desired position, starting from 1.

    Returns:
        The kth smallest value.

    Raises:
        ValueError: If the list is empty or k is invalid.
    """

    # Check for invalid input.
    if not values:
        raise ValueError("The input array cannot be empty.")

    if k < 1 or k > len(values):
        raise ValueError("k must be between 1 and the array length.")

    # Small lists can be sorted directly.
    if len(values) <= 5:
        sorted_values = insertion_sort(values)
        return sorted_values[k - 1]

    # Divide the list into groups of five.
    groups = []

    for i in range(0, len(values), 5):
        group = values[i:i + 5]
        groups.append(group)

    # Find the median of each group.
    medians = []

    for group in groups:
        medians.append(find_median(group))

    # Recursively find the median of the medians.
    median_position = (len(medians) + 1) // 2
    pivot = deterministic_select(medians, median_position)

    # Partition values into three groups.
    smaller = []
    equal = []
    larger = []

    for value in values:
        if value < pivot:
            smaller.append(value)
        elif value == pivot:
            equal.append(value)
        else:
            larger.append(value)

    # Decide which partition contains the kth smallest element.
    if k <= len(smaller):
        return deterministic_select(smaller, k)

    if k <= len(smaller) + len(equal):
        return pivot

    # Adjust k because smaller and equal elements are skipped.
    new_k = k - len(smaller) - len(equal)

    return deterministic_select(larger, new_k)


def randomized_select(values, k):
    """
    Find the kth smallest element using Randomized Quickselect.

    A random pivot is selected during every recursive call.

    The expected time complexity is O(n), but the worst-case
    time complexity is O(n squared).

    Parameters:
        values: A list of comparable values.
        k: The desired position, starting from 1.

    Returns:
        The kth smallest value.

    Raises:
        ValueError: If the list is empty or k is invalid.
    """

    # Check for invalid input.
    if not values:
        raise ValueError("The input array cannot be empty.")

    if k < 1 or k > len(values):
        raise ValueError("k must be between 1 and the array length.")

    # A list with one item has only one possible answer.
    if len(values) == 1:
        return values[0]

    # Select a pivot randomly from the current list.
    pivot = random.choice(values)

    # Divide the values into three partitions.
    smaller = []
    equal = []
    larger = []

    for value in values:
        if value < pivot:
            smaller.append(value)
        elif value == pivot:
            equal.append(value)
        else:
            larger.append(value)

    # Search only the partition that contains the answer.
    if k <= len(smaller):
        return randomized_select(smaller, k)

    if k <= len(smaller) + len(equal):
        return pivot

    new_k = k - len(smaller) - len(equal)

    return randomized_select(larger, new_k)


def run_basic_tests():
    """
    Run simple tests to confirm that both algorithms work correctly.
    """

    test_cases = [
        [9, 4, 7, 1, 3, 6, 2, 8, 5],
        [10, 10, 5, 3, 5, 8, 8, 1],
        [1],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5]
    ]

    for values in test_cases:
        print("\nInput array:", values)

        # Test the first, middle, and last order statistics.
        positions = {
            1,
            (len(values) + 1) // 2,
            len(values)
        }

        for k in sorted(positions):
            deterministic_result = deterministic_select(values, k)
            randomized_result = randomized_select(values, k)
            expected_result = sorted(values)[k - 1]

            print(f"k = {k}")
            print("Deterministic result:", deterministic_result)
            print("Randomized result:", randomized_result)
            print("Expected result:", expected_result)

            # Confirm that the implementations return the correct answer.
            assert deterministic_result == expected_result
            assert randomized_result == expected_result

    print("\nAll selection algorithm tests passed.")


if __name__ == "__main__":
    run_basic_tests()