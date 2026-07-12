"""
Assignment 6 - Part 1 Performance Testing

This file measures and compares the execution times of:

1. Deterministic Selection using Median of Medians
2. Randomized Quickselect

The tests use different dataset sizes and distributions.
"""

import random
import time

from selection_algorithms import deterministic_select, randomized_select


def measure_average_time(selection_function, values, k, trials=5):
    """
    Measure the average execution time of a selection algorithm.

    Running several trials gives a more reliable result than running
    the algorithm only one time.

    Parameters:
        selection_function: The algorithm being tested.
        values: The input list.
        k: The desired order statistic.
        trials: Number of times the test is repeated.

    Returns:
        The average execution time in seconds.
    """

    total_time = 0.0

    for _ in range(trials):
        # Copy the input to make every test independent.
        test_values = values.copy()

        start_time = time.perf_counter()

        selection_function(test_values, k)

        end_time = time.perf_counter()

        total_time += end_time - start_time

    return total_time / trials


def create_datasets(size):
    """
    Create four different datasets for a given size.

    Parameters:
        size: Number of elements in each dataset.

    Returns:
        A dictionary containing the datasets.
    """

    return {
        "Random": random.sample(range(size * 3), size),

        "Sorted": list(range(size)),

        "Reverse Sorted": list(range(size, 0, -1)),

        # Use a small number of possible values to create duplicates.
        "Repeated Elements": [
            random.choice([1, 2, 3, 4, 5])
            for _ in range(size)
        ]
    }


def run_performance_tests():
    """
    Run performance comparisons for several input sizes.
    """

    sizes = [1000, 5000, 10000]

    print("Selection Algorithm Performance Comparison")
    print("-" * 55)

    for size in sizes:
        print(f"\nDataset Size: {size}")

        datasets = create_datasets(size)

        # Find the median position.
        k = (size + 1) // 2

        for dataset_name, values in datasets.items():
            deterministic_time = measure_average_time(
                deterministic_select,
                values,
                k
            )

            randomized_time = measure_average_time(
                randomized_select,
                values,
                k
            )

            # Confirm correctness before displaying results.
            expected_result = sorted(values)[k - 1]

            deterministic_result = deterministic_select(values, k)
            randomized_result = randomized_select(values, k)

            assert deterministic_result == expected_result
            assert randomized_result == expected_result

            print(f"\nDataset Type: {dataset_name}")
            print(f"k Position: {k}")

            print(
                "Deterministic Selection Time: "
                f"{deterministic_time:.6f} seconds"
            )

            print(
                "Randomized Selection Time: "
                f"{randomized_time:.6f} seconds"
            )


if __name__ == "__main__":
    run_performance_tests()