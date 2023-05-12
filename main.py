def get_list_of_words(filename):
    with open(filename, encoding="utf-8") as file:
        text = file.read()
    text = text.replace("\t", "")
    text = text.lower()
    list_of_words = text.split("\n")
    return list_of_words


def main():
    print(get_list_of_words('dictionary.txt'))


if __name__ == '__main__':
    main()