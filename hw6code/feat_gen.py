#!/bin/python
import nltk

lexicon_dic = {}


def preprocess_corpus(train_sents):
    """Use the sentences to do whatever preprocessing you think is suitable,
    such as counts, keeping track of rare features/words to remove, matches to lexicons,
    loading files, and so on. Avoid doing any of this in token2features, since
    that will be called on every token of every sentence.

    Of course, this is an optional function.

    Note that you can also call token2features here to aggregate feature counts, etc.
    """

    label = 'PERSON'
    file = open('data/lexicon/people.person', 'r')
    for line in file.readlines():
        entity = line.strip().lower()
        if entity == "":
            continue
        for w in entity.split():
            if w not in lexicon_dic:
                lexicon_dic[w] = [label]
            else:
                if label not in lexicon_dic[w]:
                    lexicon_dic[w].append(label)
    # label = 'PERSON'
    file = open('data/lexicon/firstname.5k', 'r')
    for line in file.readlines():
        entity = line.strip().lower()
        if entity == "":
            continue
        for w in entity.split():
            if w not in lexicon_dic:
                lexicon_dic[w] = [label]
            else:
                if label not in lexicon_dic[w]:
                    lexicon_dic[w].append(label)

    # label = 'PERSON'
    file = open('data/lexicon/lastname.5000', 'r')
    for line in file.readlines():
        entity = line.strip().lower()
        if entity == "":
            continue
        for w in entity.split():
            if w not in lexicon_dic:
                lexicon_dic[w] = [label]
            else:
                if label not in lexicon_dic[w]:
                    lexicon_dic[w].append(label)

    label = 'STOPWORD'
    file = open('data/lexicon/english.stop', 'r')
    for line in file.readlines():
        entity = line.strip().lower()
        if entity == "":
            continue
        for w in entity.split():
            if w not in lexicon_dic:
                lexicon_dic[w] = [label]
            else:
                if label not in lexicon_dic[w]:
                    lexicon_dic[w].append(label)

    label = 'LOCATION'
    file = open('data/lexicon/location', 'r')
    for line in file.readlines():
        entity = line.strip().lower()
        if entity == "":
            continue
        for w in entity.split():
            if w not in lexicon_dic:
                lexicon_dic[w] = [label]
            else:
                if label not in lexicon_dic[w]:
                    lexicon_dic[w].append(label)
    file = open('data/lexicon/location.country', 'r')
    for line in file.readlines():
        entity = line.strip().lower();
        if entity == "":
            continue
        for w in entity.split():
            if w not in lexicon_dic:
                lexicon_dic[w] = [label]
            else:
                if label not in lexicon_dic[w]:
                    lexicon_dic[w].append(label)

    label = 'COMPANY'
    file = open('data/lexicon/business.consumer_company', 'r')
    for line in file.readlines():
        entity = line.strip().lower()
        if entity == "":
            continue
        for w in entity.split():
            if w not in lexicon_dic:
                lexicon_dic[w] = [label]
            else:
                if label not in lexicon_dic[w]:
                    lexicon_dic[w].append(label)

    label = 'TV_SHOWS'
    file = open('data/lexicon/tv.tv_program', 'r')
    for line in file.readlines():
        entity = line.strip().lower()
        if entity == "":
            continue
        for w in entity.split():
            if w not in lexicon_dic:
                lexicon_dic[w] = [label]
            else:
                if label not in lexicon_dic[w]:
                    lexicon_dic[w].append(label)
    # another is business product

    label = 'PRODUCT'
    file = open('data/lexicon/business.consumer_product', 'r')
    for line in file.readlines():
        entity = line.strip().lower()
        if entity == "":
            continue
        for w in entity.split():
            if w not in lexicon_dic:
                lexicon_dic[w] = [label]
            else:
                if label not in lexicon_dic[w]:
                    lexicon_dic[w].append(label)

    label = 'SPORTTEAM'
    file = open('data/lexicon/sports.sports_team', 'r')
    for line in file.readlines():
        entity = line.strip().lower()
        if entity == "":
            continue
        for w in entity.split():
            if w not in lexicon_dic:
                lexicon_dic[w] = [label]
            else:
                if label not in lexicon_dic[w]:
                    lexicon_dic[w].append(label)

    label = 'FACILITY'
    file = open('data/lexicon/architecture.museum', 'r')
    for line in file.readlines():
        entity = line.strip().lower()
        if entity == "":
            continue
        for w in entity.split():
            if w not in lexicon_dic:
                lexicon_dic[w] = [label]
            else:
                if label not in lexicon_dic[w]:
                    lexicon_dic[w].append(label)

    pass


def token2features(sent, i, add_neighs=True):
    """Compute the features of a token.

    All the features are boolean, i.e. they appear or they do not. For the token,
    you have to return a set of strings that represent the features that *fire*
    for the token. See the code below.

    The token is at position i, and the rest of the sentence is provided as well.
    Try to make this efficient, since it is called on every token.

    One thing to note is that it is only called once per token, i.e. we do not call
    this function in the inner loops of training. So if your training is slow, it's
    not because of how long it's taking to run this code. That said, if your number
    of features is quite large, that will cause slowdowns for sure.

    add_neighs is a parameter that allows us to use this function itself in order to
    recursively add the same features, as computed for the neighbors. Of course, we do
    not want to recurse on the neighbors again, and then it is set to False (see code).
    """
    ftrs = []
    # bias
    ftrs.append("BIAS")
    # position features
    if i == 0:
        ftrs.append("SENT_BEGIN")
    if i == len(sent) - 1:
        ftrs.append("SENT_END")

    # the word itself
    word = unicode(sent[i])
    ftrs.append("WORD=" + word)
    ftrs.append("LCASE=" + word.lower())
    # some features of the word
    if word.isalnum():
        ftrs.append("IS_ALNUM")

    '''
    if word.isnumeric():
        ftrs.append("IS_NUMERIC")
    if word.isdigit():
        ftrs.append("IS_DIGIT")
    
    else:
        for letter in word :
            if letter.isdigit() :
                ftrs.append("IS_NUMERIC")
                break
    '''

    if word.isupper():
        ftrs.append("IS_UPPER")
    if word.islower():
        ftrs.append("IS_LOWER")


    #tag

    pos = nltk.pos_tag([word])
    if pos:
        tag = pos[0][1]
        ftrs.append("IS_"+tag)



    # lexicon
    temp = ""
    if word[0] == "#" or word[0] == "@":
        if len(word) > 1:
            temp = word[1:].lower()
    else:
        temp = word.lower()
    if temp in lexicon_dic:
        for label in lexicon_dic[temp]:
            ftrs.append("IS_" + str(label))


    #sentence
    if word[0] == "@" :
        ftrs.append("TWITTER_TAG")
    if word[0] == "#":
        ftrs.append("HASH_TAG")
    '''
    if 'http' in word or '.com' in word:
        ftrs.append("HYPERLINK")
    '''

    # previous/next word feats
    if add_neighs:
        if i > 0:
            for pf in token2features(sent, i - 1, add_neighs=False):
                ftrs.append("PREV_" + pf)
        if i < len(sent) - 1:
            for pf in token2features(sent, i + 1, add_neighs=False):
                ftrs.append("NEXT_" + pf)

    # return it!
    return ftrs


if __name__ == "__main__":
    sents = [
        ["@mary", "nokia", "Bronx", "t77t"]
    ]
    preprocess_corpus(sents)
    for sent in sents:
        for i in xrange(len(sent)):
            print sent[i], ":", token2features(sent, i)


