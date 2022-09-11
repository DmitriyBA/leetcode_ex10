def lower_plus(str_word: str) -> str:
    """
    Функция, которая возвращает строку без
    пробелов и в нижнем регистре
    """
    str_word = str_word.lower()
    str_word = str_word.split(" ")
    new_str_word = ""
    for item in str_word:
        new_str_word += item
    return new_str_word


def palindrom_list(str_word: str) -> bool:
    """
    Функуия, которая возвращает true или false
    в зависимости от того является ли слово палиндромом
    """
    str_word_reverse = ""
    for item in range(len(str_word)-1, -1, -1):
        str_word_reverse += str_word[item]
    if str_word == str_word_reverse:
        return True
    else:
        return False


def main(word: str) -> bool:
    word = lower_plus(word)
    return palindrom_list(word)


while True:
    word = input("Введите слово: ")
    if word == "Exit":
        break
    else:
        print(main(word))