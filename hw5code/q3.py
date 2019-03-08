#!/usr/bin/env python
import distsim

word_to_ccdict = distsim.load_contexts("nytcounts.4k")


### provide your answer below


###Answer examples; replace with your choices

print 'jack'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['jack'],set(['jack']),distsim.cossim_sparse), start=1):
    print("{}: {} ({})".format(i, word, score))




print '\n'
print 'man'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['man'],set(['man']),distsim.cossim_sparse), start=1):
    print("{}: {} ({})".format(i, word, score))

print '\n'
print 'nice'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['nice'], set(['nice']), distsim.cossim_sparse),start=1):
    print("{}: {} ({})".format(i, word, score))

print '\n'
print 'move'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['move'], set(['move']), distsim.cossim_sparse),start=1):
    print("{}: {} ({})".format(i, word, score))

print '\n'
print 'father'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['father'], set(['father']), distsim.cossim_sparse),start=1):
    print("{}: {} ({})".format(i, word, score))

print '\n'
print 'mother'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['mother'], set(['mother']), distsim.cossim_sparse),start=1):
    print("{}: {} ({})".format(i, word, score))



print '\n'
print 'london'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['london'], set(['london']), distsim.cossim_sparse),start=1):
    print("{}: {} ({})".format(i, word, score))

