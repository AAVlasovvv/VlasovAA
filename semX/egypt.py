class Monoalphabet:
    alphabet = 'эьормщднйгычясюцажшбтпвёлееъзхкфи'  # TODO
    keytable = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    def init(self, keytable):
        lowercase_code = {x: y for x, y in zip(self.alphabet, keytable)}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, keytable)}
        self._encode = lowercase_code
        self._encode.update(uppercase_code)
        self._decode = {}  # TODO
    
    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])


key = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
cipher = Monoalphabet()
line = input()
while line:
    print(cipher.encode(line))
    line = input()