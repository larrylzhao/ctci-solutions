'''
5.  Given a const null terminated string containing a sentence,
can you print out the words of the sentence in reverse without changing
any data and without creating a temporary string buffer?
Do not use any helper functions, write it all out on your own.
(ie "The dog is fast" becomes "fast is dog The")

seems like a pointer question. not as relevant for a high level language like python.

would need clarification on what to do with special characters.
assuming space is the delimiter

how should multiple spaces be handled?

'''

import sys

def sentence_reverser(sentence):
    if sentence is None:
        return None

    # not really necessary, especially since we probably don't get length of sentence
    if sentence[-1] is not "\n":
        print("sentence does not end in \\n")
        return None

    lead = 0
    follow = 0

    # move lead to end of sentence
    while sentence[lead] is not "\n":
        lead += 1

    follow = lead
    while follow >= 0:
        # decrement follow until it gets to the head of the word
        while sentence[follow] is not " " and follow >= 0:
            follow -= 1

        # print word
        ptr = follow + 1

        while ptr < lead:
            print(sentence[ptr], end='')
            ptr += 1

        if follow > 0:
            print(" ", end='')

        # move lead to follow beginning of next word
        lead = follow
        follow -= 1

    print("")

sentence_reverser("The dog is fast  \n")

sentence_reverser("a\n")

sentence_reverser("\n")
