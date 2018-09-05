import re


def calculate_bigrams(word_list):
    """Calculates, for each word in the list, the probability distribution
    over possible subsequent words.

    This function returns a dictionary that maps from words to
    dictionaries that represent probability distributions over
    subsequent words.

    Arguments:
       word_list - a list of strings corresponding to the
                   sequence of words in a document. Words must
                   be all lower-case with no punctuation.

    Example:

    >>> b = calculate_bigrams(['i', 'think', 'therefore', 'i', 'am',\
                               'i', 'think', 'i', 'think'])
    >>> print(b)
    {'i':  {'am': 0.25, 'think': 0.75},
     None: {'i': 1.0},
     'am': {'i': 1.0},
     'think': {'i': 0.5, 'therefore': 0.5},
     'therefore': {'i': 1.0}}

    Note that None stands in as the predecessor of the first word in
    the sequence.

    Once the bigram dictionary has been obtained it can be used to
    obtain distributions over subsequent words, or the probability of
    individual words:

    >>> print(b['i'])
    {'am': 0.25, 'think': 0.75}

    >>> print(b['i']['think'])
    0.75

    """

    current_word = None

    word_dictionary = {}

    for word in word_list:
        if current_word not in word_dictionary:
            word_dictionary[current_word] = [1, {word: 1}]
        else:
            word_dictionary[current_word][0] += 1
            if word in word_dictionary[current_word][1]:
                word_dictionary[current_word][1][word] += 1
            else:
                word_dictionary[current_word][1][word] = 1
        current_word = word

    return_dict = {}
    for word, values in word_dictionary.items():
        occurrences = values[0]
        following_words = values[1]
        return_dict[word] = {following_word: following_word_occurrences / occurrences
                             for following_word, following_word_occurrences in following_words.items()}
    return return_dict


def import_text_file(filename):
    text_file = open(filename, 'r')

    pattern = re.compile('[:alpha:]+')

    return_val = []
    for line in text_file:
        for word in line.split():
            word_to_add = pattern.sub('', word).lower()
            if word_to_add != 0 and word_to_add.isalpha():
                return_val.append(word.lower())

    return return_val


