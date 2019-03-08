def findMatchingRules( word, grammar_dict):
    matches = []
    def search(right):
        for key, value in grammar_dict.items():
            for val in value:
                if right == val[0]:
                    matches.append([key, val[-1]])

    search(word)
    if len(word.split()) == 1 and not matches:
        search('<unk>')
    return matches