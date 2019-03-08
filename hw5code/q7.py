
#!/usr/bin/env python
#from __future__ import division
import distsim
from collections import defaultdict


file = open('q8.txt' , 'r')
word_to_vec_dict = distsim.load_word2vec("wiki-news-300d-1M.vec4")
match_position = defaultdict(list)
catorder = []


for line in file :
    line = line.strip().split()
    if line[0] == '//' :
        continue
    if line[0] == ':' :
        cat = line[1]
        catorder.append(cat)
    else :
        word0 = word_to_vec_dict[line[0]]
        word1 = word_to_vec_dict[line[1]]
        word3 = word_to_vec_dict[line[3]]
        ret = distsim.show_nearest(word_to_vec_dict,
                           word0-word1+word3,
                           set([line[0],line[1],line[3]]),
                           distsim.cossim_dense)
        count = 0
        while ( count < len(ret) ) :
            if ret[count][0] == line[2] :
                break
            else :
                count += 1
        if count !=len(ret)  :
            match_position[cat].append([count+1])
        else :
            match_position[cat].append([-1])
            print cat + " " + str(line) + "\n"
            print str(ret)

for key in catorder:
    best1 = 0
    best5 = 0
    best10 = 0
    list = match_position[key]
    length = len(list)
    for num in list :
        if num[0] ==1 :
            best1 +=1
        if num[0] < 6 and num[0] > 0:
            best5 +=1
        if num[0]< 11 and num[0] > 0 :
            best10 +=1

    print key + " " + str(format(float(best1 )/float(length),".3f")) + " " + str(format(float(best5 )/float(length),".3f")) + " " + str(format(float(best10 )/float(length),".3f"))
