class Vigenere:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    
    def __init__(self, keyword):
        self.alphaindex = {ch: index for index, ch in enumerate(self.alphabet)}
        self.key = [self.alphaindex[letter] for letter in keyword.lower()]
        # print('self.alphaindex', self.alphaindex,'self.key', self.key )
        
    
    def caesar(self, letter, shift):
        if letter in self.alphaindex:  # строчная буква
            index = (self.alphaindex[letter] + shift) % len(self.alphabet)
            # print('index',index)
            cipherletter = self.alphabet[index]
        elif letter.lower() in self.alphaindex:  # заглавная буква
            cipherletter = self.caesar(letter.lower(), shift).upper()
        else:
            cipherletter = letter
            # print('cipherletter', cipherletter)
        return cipherletter
    
    def encode(self, line):
        ciphertext = []
        for i, letter in enumerate(line):
            shift = self.key[i % len(self.key)]
            cipherletter = self.caesar(letter, shift)
            ciphertext.append(cipherletter)
            # print('shift', shift , 'letter', letter, 'cipherletter', cipherletter)
        
        return ''.join(ciphertext)
    
    def decode(self, line):
        deciphertext = []
        for i, letter in enumerate(line):
            deshift = -(self.key[i % len(self.key)])
            decipherletter = self.caesar(letter, deshift)
            deciphertext.append(decipherletter)
            # print('shift', deshift, 'letter', letter, 'cipherletter', decipherletter)
        
        return ''.join(deciphertext)
        
        
keyword = input('keyword=')
cipher = Vigenere(keyword)
line = input()
while line != '.':
    print(cipher.encode(line))
    line = input()
    
