lexicon = {
    'direction': ['north', 'south', 'east', 'west', 'down', 'up',
                  'left', 'right', 'back'],
    'verb': ['go', 'stop', 'kill', 'eat'],
    'stop': ['the', 'in', 'of', 'from', 'at', 'it'],
    'noun': ['door', 'bear', 'princess', 'cabinet']
}


def swap_lexicon(lexicon):
    swapped = {}
    for k, v in lexicon.items():
        for e in v:
            swapped[e] = k
    return swapped


def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None


def scan(sentence):
    swapped_lexicon = swap_lexicon(lexicon)
    words = sentence.split()
    sentence_list = []

    for word in words:

        if word in swapped_lexicon.keys():
            sentence_list.append((swapped_lexicon[word], word))
        else:
            converted = convert_number(word)

            if converted:
                sentence_list.append(('number', converted))
            else:
                sentence_list.append(('error', word))

    return sentence_list

    # take in a sentence string
    # break up sentence string into word strings
    # for each word, search lexicon
    # generate (TYPE, WORD) tuple
    # return list of tuples
