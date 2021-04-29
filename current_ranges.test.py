import unittest
import current_ranges


class CurrentRangesTest(unittest.TestCase):
    def test_empty_input(self):
        expected_output = 'ERR_EMPTY_INPUT'
        test_input = []
        actual_output = current_ranges.get_current_ranges(test_input)
        self.assertEqual(expected_output, actual_output)


unittest.main()
