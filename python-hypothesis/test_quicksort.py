"""Exploring hypothesis.target's ability to maximize run-time in naive quicksort.
"""
from hypothesis import given, target, settings, Phase, Verbosity, seed, example
import hypothesis.strategies as some
from timeit import default_timer as timer


def partition(arr, pivot_index):
    assert len(arr) > 0
    assert pivot_index < len(arr)
    assert pivot_index >= 0

    non_pivot_elements = [arr[i] for i in range(len(arr)) if i != pivot_index]
    pivot_element = arr[pivot_index]

    smaller = [elem for elem in non_pivot_elements if elem < pivot_element]
    bigger = [elem for elem in non_pivot_elements if elem >= pivot_element]

    return (smaller, bigger)


def quicksort_naive(arr):
    if len(arr) == 0:
        return arr

    pivot_index = 0

    smaller, bigger = partition(arr, pivot_index=0)

    return quicksort_naive(smaller) + [arr[pivot_index]] + quicksort_naive(bigger)


def test_quicksort():
    arr = [3, 1, 2, 1]

    as_sorted = quicksort_naive(arr)

    assert as_sorted == [1, 1, 2, 3]


@given(l=some.lists(some.integers()))
def test_quicksort_prop(l):
    as_sorted = quicksort_naive(l)

    assert set(as_sorted) == set(l)
    assert len(as_sorted) == len(l)
    for i in range(len(as_sorted) - 1):
        assert as_sorted[i] <= as_sorted[i + 1]


reversed_list = range(100, -1, -1)


@given(l=some.lists(some.integers()).filter(lambda arr: len(arr) <= 1000))
@settings(
    max_examples=10000,
    verbosity=Verbosity.verbose,
    phases=[
        # Phase.explicit,
        Phase.generate,
        Phase.target,
    ],  # Skip Phase.reuse to not run previous counter-examples
)
@example(l=reversed_list)
def test_quicksort_targeted(l):
    """Test runtime of naive quick-sort. Vulnerable to quadratic behaviour (and recursion depth failures?).
    """
    start = timer()
    quicksort_naive(l)
    elapsed = timer() - start

    assert elapsed <= 1e-3
    target(elapsed)


@given(l=some.lists(some.integers()).filter(lambda arr: len(arr) <= 10000))
@settings(
    max_examples=1000,
    verbosity=Verbosity.debug,
    phases=[
        Phase.explicit,
        Phase.generate,
        Phase.target,
    ],  # Skip Phase.reuse to not run previous counter-examples
)
@example(l=reversed_list)
def test_sorted(l):
    """Test regular sort. Not vulnerable to worst-case quadratic behaviour.
    """
    start = timer()
    sorted(l)
    elapsed = timer() - start

    assert elapsed <= 1e-3
    target(elapsed)
