import unittest
class TestListOfIncorrectArgs(unittest.TestCase):
    def test_custom_sum(self):
        with self.assertRaises(TypeError):
            custom_sum(1, "abc", 3, "4")
            
def custom_sum(*args):
    for v in args:
        if not isinstance(v, (int, float)):
            raise TypeError(f"custom_sum does not support type {type(v)} in arguments")

    s = 0
    for v in args:
        s += v
    return s

custom_sum('1', 3, 5 , '2')

