
with open('text.txt', 'r', encoding="utf8") as file:
    text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace(":", "").replace(";", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    
# print(words)
letter = []
for i in range(len(words)):
    letter.append(list(words[i]))
    
# print(letter)

result = []

for sublist in letter:
    result.extend(sublist)

# print(result)


alphabet = ['я','ю','э','ь','ы','ъ','щ','ш','ч','ц','х','ф','у','т','с','р','п','о','н','м','л','к','й','и','з','ж','ё','е','д','г','в','б','а']
number = []
for i in range(len(alphabet)):
    number.append(alphabet[-i-1])
    number.append(result.count(alphabet[-i-1]))
for i in range(len(alphabet)):
    
    number[i*2+1]/=len(result)
    number[i*2+1]*=100
# print(number)
file.close()


with open('text1.txt', 'r', encoding="utf8") as file1:
    text1 = file1.read()
    text1 = text1.replace("\n", " ")
    text1 = text1.replace(",", "").replace(".", "").replace(":", "").replace(";", "").replace("?", "").replace("!", "")
    text1 = text1.lower()
    words1 = text1.split()

# print(words1)
letter1 = []
for i in range(len(words1)):
    letter1.append(list(words1[i]))

# print(letter)

result1 = []

for sublist1 in letter1:
    result1.extend(sublist1)

# print(result1)

alphabet1 = ['я', 'ю', 'э', 'ь', 'ы', 'ъ', 'щ', 'ш', 'ч', 'ц', 'х', 'ф', 'у', 'т', 'с', 'р', 'п', 'о', 'н', 'м', 'л',
            'к', 'й', 'и', 'з', 'ж', 'ё', 'е', 'д', 'г', 'в', 'б', 'а']
number1 = []
for i in range(len(alphabet1)):
    number1.append(alphabet1[-i - 1])
    number1.append(result1.count(alphabet1[-i - 1]))
for i in range(len(alphabet1)):
    number1[i * 2 + 1] /= len(result1)
    number1[i * 2 + 1] *= 100
# print(number1)
file1.close()

dictionary = {}
for i in range(0, len(number), 2):
    if i + 1 < len(number):
        key = number[i]
        value = number[i + 1]
        dictionary[key] = value

print(dictionary)

dictionary1 = {}
for i in range(0, len(number1), 2):
    if i + 1 < len(number1):
        key1 = number1[i]
        value1 = number1[i + 1]
        dictionary1[key1] = value1

print(dictionary1)

my_dict = dictionary
sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

print(sorted_dict)

my_dict1 = dictionary1
sorted_dict1 = sorted(my_dict1.items(), key=lambda x: x[1], reverse=True)

print(sorted_dict1)