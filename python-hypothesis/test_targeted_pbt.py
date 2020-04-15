from hypothesis import given, target, settings, Phase, Verbosity, seed, example
import hypothesis.strategies as some
import math
import time
import re
import pytest


@pytest.mark.skip
@given(d=some.floats().filter(lambda x: abs(x) < 1000))
@settings(
    max_examples=1000,
    verbosity=Verbosity.debug,
    phases=[
        Phase.generate,
        Phase.target,
        Phase.shrink,
    ],  # Skip Phase.reuse to not run previous counter-examples
)
@seed(93962505385993024185959759429298090872)
def test_targeting_square_loss(d):
    """
    Contrived example of targeting properties.
    Disabling Phase.target or removing `target(-loss)` will most likely make the test pass.
    """
    # Assume this value triggers a bug
    target_value = 42.5

    should_fail = abs(d - target_value) < 0.5

    if should_fail:
        print("Failing with value {}".format(d))
        raise Exception("Critically close to {}, got {}".format(target_value, d))

    # Target the value
    loss = math.pow((d - target_value), 2.0)
    target(-loss)


regex = re.compile("(a+)+")


@given(chars=some.text(alphabet=some.characters(whitelist_categories=("Lu", "Ll"))))
@settings(
    max_examples=1000,
    verbosity=Verbosity.debug,
    phases=[
        Phase.generate,
        Phase.target,
        Phase.shrink,
    ],  # Skip Phase.reuse to not run previous counter-examples
)
def test_redos(chars):

    start = time.time()
    regex.match(chars)
    spent = time.time() - start
    target(spent)
