def start_with_a(word):
    if (word[0]) == "A":
        return "does"
    else:
        return "doesn't"


# main
word_to_check = input("Enter the word: ").title()
print(f"the word {word_to_check} {start_with_a(word_to_check)} start with 'A'!")
