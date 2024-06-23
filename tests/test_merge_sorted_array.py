import unittest
import pytest

from py_src import merge_sorted_array  

@pytest.mark.parametrize("nums1, nums2, m, n, expected_output", 
                         [
                            ([0], [1], 0, 1, [1]),
                            ([1,2,3,0,0,0], [2,5,6], 3, 3, [1,2,2,3,5,6]),
                            ([1], [], 1, 0, [1])
                         ]
)

# class Test_merge_sorted_array(unittest.TestCase):
def test_merge_empty_array(nums1, nums2, m, n, expected_output):
    assert merge_sorted_array.Solution.merge_sorted_arrays(nums1, nums2, m, n) == expected_output

# if __name__ == "__main__":
#     unittest.main()