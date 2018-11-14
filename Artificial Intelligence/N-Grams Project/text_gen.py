"""This program generates random text based on n-grams
calculated from sample text.

Author: Nathan Sprague, David Sykes, and [YOU]
Date: 8/24/14
Modified:
    9/3/18 by David Sykes
    - Updated to Python 3
    - Cleaned up code to comply with PEP-8
    - Reimplemented counts_to_probabilities()
    - Added some stubs and some docstring content
"""

# Honor code statement:
#   If you received help from an outside source, describe it here.
#
#

import random
import string
import sys
import textwrap


def text_to_list(file_name):
    """ Converts the provided plain-text file to a list of words.  All
    punctuation will be removed, and all words will be converted to
    lower-case.

    Argument:
        file_name - A string containing a file path.
    Returns
        A list containing the words from the file.
    """
    handle = open(file_name, 'r')
    text = handle.read().lower()
    text = text.translate(
        str.maketrans(string.punctuation,
                      " " * len(string.punctuation)))
    return text.split()


def select_random(distribution):
    """
    Select an item from the the probability distribution
    represented by the provided dictionary.
    :param distribution: a dictionary whose values are probabilities
    :return: A key chosen at random based on probabilities

    Example:
    >>> select_random({'a':.9, 'b':.1})
    'a'
    """

    # Make sure that the probability distribution has a sum close to 1.
    assert abs(sum(distribution.values()) - 1.0) < .000001, \
        "Probability distribution does not sum to 1!"

    r = random.random()
    total = 0
    for item in distribution:
        total += distribution[item]
        if r < total:
            return item

    assert False, "Error in select_random!"


def counts_to_probabilities(counts):
    """ Convert a dictionary of counts to probabilities.

    Argument:
       counts - a dictionary mapping from items to integers

    Returns:
       A new dictionary where each count has been divided by the sum
       of all entries in counts.

    Example:

    >>> counts_to_probabilities({'a':9, 'b':1})
    {'a': 0.9, 'b': 0.1}

    """
    total = float(sum(counts.values()))
    return {item: value / total for item, value in counts.items()}


def calculate_unigrams(word_list):
    """ Calculates the probability distribution over individual words.

    Arguments:
       word_list - a list of strings corresponding to the
                   sequence of words in a document. Words must
                   be all lower-case with no punctuation.
    Returns:
       A dictionary mapping from words to probabilities.

    Example:

    >>> u = calculate_unigrams(['i', 'think', 'therefore', 'i', 'am'])
    >>> print(u)
    {'i': 0.4, 'think': 0.2, 'therefore': 0.2, 'am': 0.2}

    """
    unigrams = {}
    for word in word_list:
        unigrams[word] = unigrams.get(word, 0) + 1
        # if word in unigrams:
        #     unigrams[word] += 1
        # else:
        #     unigrams[word] = 1
    return counts_to_probabilities(unigrams)


def random_unigram_text(unigrams, num_words):
    """Generate a random sequence according to the provided probabilities.

    Arguments:
       unigrams -   Probability distribution over words (as returned by the
                    calculate_unigrams function).
       num_words -  The number of words of random text to generate.

    Returns:
       The random string of words with each subsequent word separated by a
       single space.

    Example:

    >>> u = calculate_unigrams(['i', 'think', 'therefore', 'i', 'am'])
    >>> random_unigram_text(u, 5)
    'think i therefore i i'

    """
    result = []
    for i in range(num_words):
        next_word = select_random(unigrams)
        result.append(next_word)
    return ' '.join(result)


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
    .75

    """

    bigrams = {None: {word_list[0]: 1}}
    biprob = {None: {word_list[0]: 1.0}}
    for i in range(len(word_list) - 1):
        word1 = word_list[i]
        word2 = word_list[i + 1]
        if word1 not in bigrams:
            bigrams[word1] = {}
        if word2 not in bigrams[word1]:
            bigrams[word1][word2] = 1
        else:
            bigrams[word1][word2] = bigrams[word1][word2] + 1
        from_c2p = counts_to_probabilities(bigrams[word1])
        biprob[word1] = from_c2p
    return biprob


def calculate_trigrams(word_list):
    """Calculates, for each adjacent pair of words in the list, the
    probability distribution over possible subsequent words.

    The returned dictionary maps from two-word tuples to dictionaries
    that represent probability distributions over subsequent
    words.

    Example:

    >>> b = calculate_trigrams(['i', 'think', 'therefore', 'i', 'am',\
                                'i', 'think', 'i', 'think'])
    >>> print(b)
    {('think', 'i'): {'think': 1.0},
    ('i', 'am'): {'i': 1.0},
    (None, None): {'i': 1.0},
    ('therefore', 'i'): {'am': 1.0},
    ('think', 'therefore'): {'i': 1.0},
    ('i', 'think'): {'i': 0.5, 'therefore': 0.5},
    (None, 'i'): {'think': 1.0},
    ('am', 'i'): {'think': 1.0}}
    """
    trigrams_count = {(None, None): {word_list[0]: 1}, (None, word_list[0]): {word_list[1]: 1}}
    trigrams_prob = {(None, None): {word_list[0]: 1.0}, (None, word_list[0]): {word_list[1]: 1.0}}
    for i in range(len(word_list) - 2):
        word1 = word_list[i]
        word2 = word_list[i + 1]
        word3 = word_list[i + 2]
        tuple_key = (word1, word2)
        if tuple_key not in trigrams_count:
            trigrams_count[tuple_key] = {}
        if word3 not in trigrams_count[tuple_key]:
            trigrams_count[tuple_key][word3] = 1
        else:
            trigrams_count[tuple_key][word3] = trigrams_count[tuple_key][word3] + 1
        value_probs = counts_to_probabilities(trigrams_count[tuple_key])
        trigrams_prob[tuple_key] = value_probs

    return trigrams_prob


def random_bigram_text(first_word, bigrams, num_words):
    """Generate a random sequence of words following the word pair
    probabilities in the provided distribution.

    Arguments:
       first_word -          This word will be the first word in the
                             generated text.
       bigrams -   Probability distribution over word _pairs
                             (as returned by the calculate_bigrams function).
       num_words -           The number of words of random text to generate.

    Returns:
       The random string of words with each subsequent word separated by a
       single space.

    Example:
    >>> b = calculate_bigrams(['i', 'think', 'therefore', 'i', 'am',\
                               'i', 'think', 'i', 'think'])
    >>> random_bigram_text('think', b, 5)
    'think i think therefore i am'

    >>> random_bigram_text('think', b, 5)
    'think therefore i think therefore i'

    """

    result = [first_word]
    curr_word = first_word
    for i in range(num_words - 1):
        next_word = select_random(bigrams[curr_word])
        result.append(next_word)
        curr_word = next_word

    return ' '.join(result)


def random_trigram_text(first_word, second_word, bigrams, trigrams, num_words):
    """Generate a random sequence of words according to the provided
    bigram and trigram distributions.

    By default, each new word will be generated using the trigram
    distribution.  The bigram distribution will be used when a
    particular word pair does not have a corresponding trigram.

    Arguments:
       first_word -          The first word in the generated text.
       second_word -         The second word in the generated text.
       bigrams -             bigram probabilities (as returned by the
                             calculate_bigrams function).
       trigrams -            trigram probabilities (as returned by the
                             calculate_bigrams function).
       num_words -           The number of words of random text to generate.

    Returns:
       The random string of words with each subsequent word separated by a
       single space.

    """
    result = [first_word, second_word]
    curr_words = (first_word, second_word)
    for i in range(num_words - 2):
        prev_word = curr_words[1]
        if curr_words not in trigrams:
            next_word = select_random(bigrams[curr_words[1]])
            result.append(next_word)
            curr_words = (prev_word, next_word)
        else:
            next_word = select_random(trigrams[curr_words])
            result.append(next_word)
            curr_words = (prev_word, next_word)

    return ' '.join(result)


def unigram_main(filename, word_count):
    """
    Generate text from a file's unigrams.
    :param filename: the name of the text file to process
    :param word_count: the number of words to generate
    :return: None
    """
    words = text_to_list(filename)
    unigrams = calculate_unigrams(words)

    word_list = random_unigram_text(unigrams, 100)

    # Print each line.
    wrapper = textwrap.TextWrapper(width=72)
    for element in wrapper.wrap(text=word_list):
        print(element)


def bigram_main(filename, word_count):
    """
    Generate text from a file's bigrams.
    :param filename: the name of the text file to process
    :param word_count: the number of words to generate
    :return: None
    """

    words = text_to_list(filename)
    # words = ['i', 'think', 'therefore', 'i', 'am', 'i', 'think', 'i', 'think']
    bigrams = calculate_bigrams(words)

    word_list = random_bigram_text('the', bigrams, word_count)

    # Print each line.
    wrapper = textwrap.TextWrapper(width=72)
    for element in wrapper.wrap(text=word_list):
        print(element)


def trigram_main(filename, word_count):
    """
    Generate text from a file's trigrams.
    :param filename: the name of the text file to process
    :param word_count: the number of words to generate
    :return: None
    """
    words = text_to_list(filename)
    bigrams = calculate_bigrams(words)
    trigrams = calculate_trigrams(words)
    word_list = random_trigram_text('among', 'other', bigrams, trigrams, word_count)

    # Print each line.
    wrapper = textwrap.TextWrapper(width=72)
    for element in wrapper.wrap(text=word_list):
        print(element)


def n_tuples(seq, n):
    """
    Generate tuples of a sequence starting with (None, i)
    where i = seq[0]
    :param seq: a list
    :param n: the length of each tuple
    :return: a generator of n-tuples

    Adapted from https://stackoverflow.com/questions/5764782/iterate-through-pairs-of-items-in-a-python-list

    >>> list(n_tuples([0, 1, 2, 3, 4, 5], 2))
    [(None,   0), (0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

    >>> list(n_tuples([0, 1, 2, 3, 4, 5], 3))
    [(None, None, 0), (None, 0, 1), (1, 2, 3), (2, 3, 4), (3, 4, 5)]

    """
    # TODO - OPTIONAL!
    return list(seq)[:n]  # STUB


if __name__ == "__main__":
    # You can insert testing code here, or switch out the main method
    # to try bigrams or trigrams.
    if len(sys.argv) != 3:
        print("Usage: {} <filename> <word_count>".format(sys.argv[0]))
        exit(1)

    print("Unigrams:")
    unigram_main(sys.argv[1], int(sys.argv[2]))

    print('-' * 40)
    print("Bigrams:")
    bigram_main(sys.argv[1], int(sys.argv[2]))

    print('-' * 40)
    print("Trigrams:")
    trigram_main(sys.argv[1], int(sys.argv[2]))
