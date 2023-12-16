import unittest
def prostmn(num):
    assert isinstance(num, (int)) or float(num) % 1 == 0, 'a natural number is expected'
    num = int(float((num)))
    assert num > 0, 'a natural number is expected'
    results = list()
    divisor = 2
    # print(num, divisor)
    if num == 1:
        results.append(num)
        return results
    else:
        while divisor <= num:
            if num % divisor == 0:
                num = num // divisor
                results.append(divisor)
                continue
            divisor += 1
        return results
            
# print(prostmn(7))
class TestZero(unittest.TestCase):
    def test_prostmn(self):
        with self.assertRaises(AssertionError):
            prostmn(0)


class TestOne(unittest.TestCase):
    def test_prostmn(self):
        self.assertEqual(prostmn(1), [1], 'it should be 1')

class TestTwo(unittest.TestCase):
    def test_prostmn(self):
        self.assertEqual(prostmn(2), [2], 'it should be 2')

class TestNumbers(unittest.TestCase):
    def test_prostmn(self):
        self.assertEqual(prostmn(8), [2, 2, 2], 'it should be 2, 2, 2')

class TestNumbers2(unittest.TestCase):
    def test_prostmn(self):
        self.assertEqual(prostmn(7), [7], 'it should be 7')
        
class TestNumbers3(unittest.TestCase):
    def test_prostmn(self):
        self.assertEqual(prostmn(78), [2, 3, 13], 'it should be 2, 3, 13')
        
class TestANegativeNumber(unittest.TestCase):
    def test_prostmn(self):
        with self.assertRaises(AssertionError):
            prostmn(-5464549849)
        
class TestFractionalNumber(unittest.TestCase):
    def test_prostmn(self):
        with self.assertRaises(AssertionError):
            prostmn(65.23)
class TestFractionalNegativeNumber(unittest.TestCase):
    def test_prostmn(self):
        with self.assertRaises(AssertionError):
            prostmn(-65.23)

class TestNaturalNumberInTheFloatEntry(unittest.TestCase):
    def test_prostmn(self):
        self.assertEqual(prostmn(94.0), [2, 47], 'it should be 2, 47')