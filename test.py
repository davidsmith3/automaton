from hypothesis import given
from hypothesis.strategies import integers, lists


@given(lists(integers()))
def test_get_slice(ls):
    pass

