import random


def get_list_of_words(filename):
    with open(filename, encoding="utf-8") as file:
        text = file.read()
    text = text.replace("\t", "")
    text = text.lower()
    list_of_words = text.split("\n")
    return list_of_words


def select_words(filename):
    lst = get_list_of_words(filename)
    index = random.randint(0, len(lst))
    random_word = lst[index]
    couple_of_words = random_word.split('-')

    return couple_of_words


def main():
    couple_of_words = select_words('dictionary.txt')
    first_word = couple_of_words[0].strip()
    second_word = couple_of_words[1].strip()

    print("Translated word: ", first_word)
    translate = input("Enter a translation: ")
    if translate == second_word:
        print("It's correct!")
    else:
        print("You were make a mistake!")


if __name__ == '__main__':
    main()
