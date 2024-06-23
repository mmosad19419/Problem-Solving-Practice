import unittest
import pytest

from py_src.remove_element_in_place import removeElement


@pytest.mark.parametrize("nums, val, expected_output",
                         [
                            ([0,1,2,2,3,0,4,2], 2, [0,0,1,3,4]),
                            ([3,2,2,3], 3, [2, 2])
                         ])


def test_removeElement(nums, val, expected_output):
    k, nums = removeElement(nums, val)
    expectedNums = expected_output
    nums = sorted(nums[:k])

    assert k == len(expectedNums)
    assert nums[:k] == expected_output

    for indx, val in enumerate(nums):
        assert val == expectedNums[indx]