"""Standard example of targeted data generation. Generate 
lists of directions targeting maximum "x-y", i.e., endpoints that are
as much in the lower right quadrant as possible.
"""
from enum import Enum
from hypothesis import given, target, event, settings
import hypothesis.strategies as some


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


def some_paths():
    directions = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]
    return some.lists(some.sampled_from(directions))


def path_endpoint(path):
    """Compute the endpoint of given path.
    
    Returns:
        (int, int) -- (X, Y) tuple
    """
    x = 0
    y = 0
    for direction in path:
        if direction == Direction.RIGHT:
            x = x + 1
        elif direction == Direction.DOWN:
            y = y - 1
        elif direction == Direction.LEFT:
            x = x - 1
        elif direction == Direction.UP:
            y = y + 1
        else:
            raise Exception("Unknown direction {}".format(direction))
    return (x, y)


def to_range(val, base):
    div = val // base
    return (base * div, (div + 1) * base)


@given(path=some_paths())
@settings(max_examples=1000)
def test_paths_notarget(path):
    """Generate paths without any target.
    """
    x, y = path_endpoint(path)
    print(
        "No target: x={}, y={}, path=[{}]".format(
            x, y, ", ".join([str(p) for p in path])
        )
    )
    in_range = to_range(x - y, 10)
    event(str(in_range))


@given(path=some_paths().filter(lambda path: len(path) < 1000))
@settings(max_examples=250)
def test_paths_with_target(path):
    """Generate paths targeting lower right.
    """
    x, y = path_endpoint(path)
    print("With target: x={}, y={}, len={}".format(x, y, len(path)))

    in_range = to_range(x - y, 100)
    event(str(in_range))

    target_function = float(x - y)
    target(target_function)
