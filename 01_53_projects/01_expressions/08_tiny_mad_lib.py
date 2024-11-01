def tiny_mad_lib():
    adjective = input("\nPlease type an adjective and press enter : ")
    noun = input("\nPlease type a noun and press enter :  ")
    verb = input("\nPlease type a verb and press enter : ")

    Sentence_start = "Once Upon a time, there was a very "

    print(f"\n{Sentence_start}\033[1;3m{adjective}\033[0m \033[1;3m{noun}\033[0m that loved to \033[1;3m{verb}\033[0m!")

if __name__ == "__main__":
    tiny_mad_lib()