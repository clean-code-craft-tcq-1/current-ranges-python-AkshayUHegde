import math
import unittest
import current_ranges


class CurrentRangesTest(unittest.TestCase):
    def test_empty_input(self):
        expected_output = 'ERR_EMPTY_INPUT'
        test_input = []
        actual_output = current_ranges.get_current_ranges(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_non_int_input(self):
        test_input = [5, 8, 10, math.nan]
        expected_output = 'ERR_NON_INTEGER'
        actual_output = current_ranges.get_current_ranges(test_input)
        self.assertEqual(expected_output, actual_output)

unittest.main()
