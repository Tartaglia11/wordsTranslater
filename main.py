import random


def get_list_of_words(filename):
    with open(filename, encoding="utf-8") as file:
        text = file.read()
    text = text.replace("\t", "")
    text = text.lower()
    list_of_words = text.split("\n")
    return list_of_words


def main():
    lst = get_list_of_words('dictionary.txt')
    index = random.randint(0, len(lst))
    random_word = lst[index]
    couple_of_words = random_word.split('-')
    first_word = couple_of_words[0].strip()
    second_word = couple_of_words[1].strip()


if __name__ == '__main__':
    main()
