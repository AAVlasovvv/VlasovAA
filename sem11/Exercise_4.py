class Caesar:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    
    def __init__(self, key):
        key = key
        assert isinstance(key, int), 'the entered key is incorrect'
        self._encode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i + key) % len(self.alphabet)]
            self._encode[letter] = encoded
            self._encode[letter.upper()] = encoded.upper()
        self._decode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            decoded = self.alphabet[(i - key) % len(self.alphabet)]
            self._decode[letter] = decoded
            self._decode[letter.upper()] = decoded.upper()
    
    def encode(self, text):
        assert isinstance(text, str), 'the entered data is incorrect'
        return ''.join([self._encode.get(char, char) for char in text])
    
    def decode(self, line):
        assert isinstance(line, str), 'the entered data is incorrect'
        return ''.join([self._decode.get(char, char) for char in line])


# key = int(input('Введите ключ:'))
# cipher = Caesar(key)
# cipher = Caesar(27)
# line = input()
# while line:
#     print(cipher.encode(line))
#     line = input()

#Бобрик вышел погулять

import unittest
class TestEnShiftTo5(unittest.TestCase):
    def test_quicksort(self):
        cipher = Caesar(5)
        self.assertEqual(cipher.encode('Бобрик вышел погулять'), 'Ёуёхнп жаэйр фузшрдчб' 'it should be: Ёуёхнп жаэйр фузшрдчб')
        
class TestDeShiftTo5(unittest.TestCase):
    def test_quicksort(self):
        cipher = Caesar(5)
        self.assertEqual(cipher.decode('Ёуёхнп жаэйр фузшрдчб'),
                         'Бобрик вышел погулять' 'it should be: Бобрик вышел погулять')


class TestEnShiftTo14(unittest.TestCase):
    def test_quicksort(self):
        cipher = Caesar(14)
        self.assertEqual(cipher.encode('Бобрик вышел погулять'),
                         'Оьоюцш пиётщ эьрбщмай' 'it should be: Оьоюцш пиётщ эьрбщмай')


class TestDeShiftTo14(unittest.TestCase):
    def test_quicksort(self):
        cipher = Caesar(14)
        self.assertEqual(cipher.decode('Оьоюцш пиётщ эьрбщмай'),
                         'Бобрик вышел погулять' 'it should be: Бобрик вышел погулять')


class TestEnShiftTo33(unittest.TestCase):
    def test_quicksort(self):
        cipher = Caesar(33)
        self.assertEqual(cipher.encode('Бобрик вышел погулять'),
                         'Бобрик вышел погулять' 'it should be: Бобрик вышел погулять')


class TestDeShiftTo33(unittest.TestCase):
    def test_quicksort(self):
        cipher = Caesar(33)
        self.assertEqual(cipher.decode('Бобрик вышел погулять'),
                         'Бобрик вышел погулять' 'it should be: Бобрик вышел погулять')
        

class TestIncorrectData(unittest.TestCase):
    
    def test_quicksort(self):
        cipher = Caesar(3)
        with self.assertRaises(AssertionError):
            cipher.decode(123)
            
            
class TestIncorrectData2(unittest.TestCase):
    
    def test_quicksort(self):
        cipher = Caesar(3)
        with self.assertRaises(AssertionError):
            cipher.decode(['chomik'])
            
            
class TestIncorrectKey(unittest.TestCase):
    def test_quicksort(self):
        cipher = Caesar('chomik')
        with self.assertRaises(AssertionError):
            cipher.decode('Ыиыкге ьхтяё йиэнёщмц')
            

        
            
class TestAllLetters(unittest.TestCase):
    def test_quicksort(self):
        cipher = Caesar(1)
        self.assertEqual(cipher.decode('бвгдеёжзийклмнопрстуфхцчшщъыьэюяa'),
                         'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' 'it should be: абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        

class TestAllLetters(unittest.TestCase):
    def test_quicksort(self):
        cipher = Caesar(14)
        deline = cipher.decode('Оьоюцш пиётщ эьрбщмай').split()
        line = ('Оьоюцш пиётщ эьрбщмай').split()
        for i in range(len(line)):
            self.assertEqual(len(deline[i]), len(line[i]), 'the number of characters in the string does not match')
        
        
            
            
        
        

        
