


import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main() # Calling from the command line invokes all test.
# ======================================================================
# ERROR: test_average (__main__.TestStatisticalFunctions)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/Users/ddang/learning-python/practice-python/tutorial/10_standard_library/10_standard_library_examples/standard_library_exam16.py", line 9, in test_average
#     self.assertEqual(average([20, 30, 70]), 40.0)
# NameError: name 'average' is not defined

# ----------------------------------------------------------------------
# Ran 1 test in 0.001s

# FAILED (errors=1)