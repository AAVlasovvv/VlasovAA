with open('text1.txt', 'r', encoding="utf8") as file:
    text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace(":", "").replace(";", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()

print(words)
letter = []
for i in range(len(words)):
    letter.append(list(words[i]))

# print(letter)

result = []

for sublist in letter:
    result.extend(sublist)

print(result)

alphabet = ['я', 'ю', 'э', 'ь', 'ы', 'ъ', 'щ', 'ш', 'ч', 'ц', 'х', 'ф', 'у', 'т', 'с', 'р', 'п', 'о', 'н', 'м', 'л',
            'к', 'й', 'и', 'з', 'ж', 'ё', 'е', 'д', 'г', 'в', 'б', 'а']
number = []
for i in range(len(alphabet)):
    number.append(alphabet[-i - 1])
    number.append(result.count(alphabet[-i - 1]))
for i in range(len(alphabet)):
    number[i * 2 + 1] /= len(result)
    number[i * 2 + 1] *= 100
print(number)