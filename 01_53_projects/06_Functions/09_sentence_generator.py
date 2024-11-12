def sentence_generator(word,part_of_speech):
    if part_of_speech == 0:
        print(f"I am excited to add this \033[1;3m{word}\033[0m to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"t's so nice outside today it makes me want to \033[1;3m{word}\033[0m!")
    elif part_of_speech == 2:
        print(f"Looking out my window, the sky is big and \033[1;3m{word}\033[0m!")
    else:
        print("Part of speech must be 0, 1, or 2! can,t make a sentence")


def main():
    word : str = input("\033[34mPlease type a noun, verb, or adjective : \033[0m")
    print("Is this a noun, verb , or adjective? ")
    part_of_speech  : int = int(input("\033[34mType 0 for noun, 1 for verb, 2 for adjective :\033[0m "))
    sentence_generator(word,part_of_speech)

if __name__ == "__main__":
    main()