import random

def main():
    setting = input('Choose 1 for automatic parameters or 2 for choosing the parameters: ')
    if(setting == '1'):
        print(make_sentence(1, 'past'))
        print(make_sentence(1, 'present'))
        print(make_sentence(1, 'future'))
        print(make_sentence(2, 'past'))
        print(make_sentence(2, 'present'))
        print(make_sentence(2, 'future'))
    elif(setting == '2'):
        for i in range(6):
            print(make_sentence(get_quantity_for_user(), get_sentence_for_user()))
    else:
        print('Please enter a valid option')

def get_quantity_for_user():
    quantity = input('Please, input a number between 1 and 2: ')
    return quantity

def get_sentence_for_user():
    tense = input('Please, choose a tense between: past, present and future: ')
    return tense

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if (quantity == 1):
        words = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]
    
    word = random.choice(words)

    return word

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if(tense == 'past'):
        words = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    elif(tense == 'present' and quantity == 1):
        words = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
    elif(tense == 'present' and quantity != 1):
        words = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    elif(tense == 'future'):
        words = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    word = random.choice(words)

    return word


def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    determine = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)

    sentence = determine + ' ' + get_adjectives()  + ' ' + noun + " " + verb + " " + get_prepositional_phrase(quantity) + ' ' + get_prepositional_phrase(quantity) + '.'

    return sentence.capitalize()

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
    "about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"
    Return: a randomly chosen preposition.
    """
    preopositions = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]
    
    preposition = random.choice(preopositions)

    return preposition

def get_adjectives():
    """Return a randomly chosen adjective
    from this list of adjectives:
    "visible", "lowly", "bewildered", "brave", "additional", "erratic", "southern"
    Return: a randomly chosen preposition.
    """
    adjectives = ["visible", "lowly", "bewildered", "brave", "additional", "erratic", "southern"]
    
    adjective = random.choice(adjectives)

    return adjective

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    prepositionalPhrase = get_preposition() + ' ' + get_determiner(quantity) + ' ' + get_noun(quantity)

    return prepositionalPhrase.capitalize()
    

main()

