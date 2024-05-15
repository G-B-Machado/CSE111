import random
import string

numbers = [16.2, 75.1, 52.3]
word_list = ['Hi']
ramdom_strings = []
def append_random_numbers(number_list, qnt = 1):
    for _ in range(qnt):
        random_number = round(random.uniform(0, 100),1)
        number_list.append(random_number)

def append_random_words(list, qnt = 1):
    for _ in range(qnt):
        ramdom_word = random.choice(list)
        word_list.append(ramdom_word)

def generate_random_word(length=5):
    """
    Generates a random word of the specified length.

    Args:
        length (int, optional): The desired length of the word (default: 5).

    Returns:
        str: The generated random word.
    """

    # Define the characters to choose from (letters and punctuation)
    characters = string.ascii_letters

    # Generate a random word using random choices from the characters
    random_word = "".join(random.choice(characters) for _ in range(length))

    return random_word

def main():
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers,5)
    print(numbers)
    append_random_numbers(numbers,11)
    print(numbers)

    for _ in range(5):
        ramdom_strings.append(generate_random_word(4))

    append_random_words(ramdom_strings,5)

    print(word_list)

if __name__ == "__main__":
    main()