import whois
import itertools
import string
# Все строчные буквы и цифры
symbols = string.ascii_lowercase + string.digits

# Получаем все возможные комбинации из трех символов
combinations = list(itertools.product(symbols, repeat=3))

# Преобразование каждой комбинации обратно в строку
strings = [''.join(combination) for combination in combinations]

# Печать всех возможных строк
for s in strings:
    s1 = s+".ru"
    try:
        m = whois.whois(s1)
    except:
        print("Дс -", s1)
