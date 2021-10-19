
import os


def RLE():

    numberOfRepetitions = 1
    massiveLetters = []
    massiveRepetitionsLetters = []
    peremennaya = None

    for i in range(len(text)):

        if peremennaya:
            if text[i] == peremennaya:
                numberOfRepetitions += 1

            else:
                massiveLetters.append(peremennaya)
                massiveRepetitionsLetters.append\
                    (numberOfRepetitions)
                peremennaya = text[i]
                numberOfRepetitions = 1
        else:
            peremennaya = text[i]
    text1 = ""
    RLEtext = open('file/124.txt', 'w')
    for i in range(len(massiveLetters)):
        text1 += f"{massiveRepetitionsLetters[i]}" \
                 f"{massiveLetters[i]}"
    RLEtext.write(text1)
    RLEtext.close()
    return os.stat('file/124.txt').st_size




text = open('file/123.txt', 'r').read()
size = os.stat('file/123.txt').st_size
print(f'исходный размер файла {size} байт\n')
try:
    a = int(input('каким алгоритмом сжатия вы хотите воспользоватся?\n'
                  'набирите 1, если хотите сжать алгоритмом RLE\n'
                  'набиирте 2,если хотите сжать Алгоритмом Лемпеля'
                  ' Зива\n Ваше число: '))
    if a == 1:
        RLEtext = RLE()
        print(f'получившийся после RLE размер файла {RLEtext}')
    elif a == 2:
        print('В разработке')
    else:
        print('Вы ввели не то число')
except ValueError:
    print('Error: Вы ввели не число')



