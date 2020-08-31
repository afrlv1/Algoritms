# Евлампия стала подозревать, что Кондратий отец пытается читать её сообщения и письма. 
# Она приказала разработать новую систему шифрования. Дано зашифрованное слово и список слов. 
# Для того, чтобы узнать, какое слово зашифровано, нужно в списке найти самое длинное слово, 
# которое является подсловом (подпоследовательностью) зашифрованного слова. 
# Если таких слов более одного, нужно вывести лексикографически минимальное из них.

# Формат ввода
# В первой строке записано зашифрованное слово. Оно состоит из строчных латинских букв. 
# Его длина не превосходит 1000 символов. 
# В следующей строке задана дина словаря n, она не превосходит 1000. 
# В следующих n строках записаны слова из словаря. Длина каждого из них не превосходит 1000.

# Формат вывода
# Нужно вывести зашифрованное слово, или пустую строку, если такого слова нет в словаре.

# Пример 1
# Ввод	
# abpcplea
# 4
# ale
# apple
# monkey
# plea
# Вывод
# apple


with open('input.txt') as f:
    s = str(f.readline())
    m = int(f.readline())
    d = [line.rstrip('\n') for line in f]


def findLongestWord(string,dictionary):
    longest_word = ""
    for word in sorted(dictionary, key=len, reverse=True):
        if len(word) < len(longest_word):
            break

        source = iter(string)
        for w in word:
            for s in source:
                if s == w:
                    break
            else:
                break
        else:
            n = len(word)
            m = len(longest_word)
            if n > m or (n == m and word < longest_word):
                longest_word = word
                
    return longest_word
print(findLongestWord(s,d))