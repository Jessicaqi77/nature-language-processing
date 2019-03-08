#!/usr/bin/env python
import distsim
word_to_vec_dict = distsim.load_word2vec("nyt_word2vec.4k")
###Provide your answer below

###Answer examples; replace with your choices

print 'jack'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['jack'],set(['jack']),distsim.cossim_dense)):
    print("{}: {} ({})".format(i, word, score))

print '\n'
print 'man'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['man'],set(['man']),distsim.cossim_dense)):
    print("{}: {} ({})".format(i, word, score))

print '\n'
print 'nice'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['nice'],set(['nice']),distsim.cossim_dense)):
    print("{}: {} ({})".format(i, word, score))


print '\n'
print 'move'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['move'],set(['move']),distsim.cossim_dense)):
    print("{}: {} ({})".format(i, word, score))

print '\n'
print 'father'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['father'],set(['father']),distsim.cossim_dense)):
    print("{}: {} ({})".format(i, word, score))

print '\n'
print 'london'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['london'],set(['london']),distsim.cossim_dense)):
    print("{}: {} ({})".format(i, word, score))