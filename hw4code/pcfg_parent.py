#!/usr/bin/env python
import argparse
import sys
import codecs
if sys.version_info[0] == 2:
  from itertools import izip
else:
  izip = zip
from collections import defaultdict
import re
import os.path
import gzip
import tempfile
import shutil
import atexit

#import matplotlib.pyplot as plt
from findMatching import findMatchingRules
import math
import time
from tree import Tree

scriptdir = os.path.dirname(os.path.abspath(__file__))

reader = codecs.getreader('utf8')
writer = codecs.getwriter('utf8')
def prepfile(fh, code):
  if type(fh) is str:
    fh = open(fh, code)
  ret = gzip.open(fh.name, code if code.endswith("t") else code+"t") if fh.name.endswith(".gz") else fh
  if sys.version_info[0] == 2:
    if code.startswith('r'):
      ret = reader(fh)
    elif code.startswith('w'):
      ret = writer(fh)
    else:
      sys.stderr.write("I didn't understand code "+code+"\n")
      sys.exit(1)
  return ret
def addonoffarg(parser, arg, dest=None, default=True, help="TODO"):
  ''' add the switches --arg and --no-arg that set parser.arg to true/false, respectively'''
  group = parser.add_mutually_exclusive_group()
  dest = arg if dest is None else dest
  group.add_argument('--%s' % arg, dest=dest, action='store_true', default=default, help=help)
  group.add_argument('--no-%s' % arg, dest=dest, action='store_false', default=default, help="See --%s" % arg)

def generateTable(sentences, start, grammar_dict):
    start_time = start
    # Create the CYK table and  a back bp table
    sentence = sentences.strip().split()
    length = len(sentence)
    table = []
    bp_table = []
    for x in range(length):
        table.append([])
        bp_table.append([])
        for y in range(length + 1):
            table[x].append([])
            bp_table[x].append([])

    # Fill the diagonal of the CYK table
    for i in range(0, length):
        terminals = findMatchingRules(sentence[i], grammar_dict)
        for j in range(len(terminals)):
            table[i][i + 1].extend([(terminals[j][0], terminals[j][1])])

    # Fill the CYK table
    for i in range(0, length + 1):
        for j in range(i - 2, -1, -1):
            for k in range(j + 1, i):
                for left_rule in (table[j][k]):
                    for down_rule in (table[k][i]):
                        if time.time() - start_time > 100:
                            return None
                        rule_right = left_rule[0] + ' ' + down_rule[0]
                        prob = left_rule[1] * down_rule[1]
                        new_rule = findMatchingRules(rule_right, grammar_dict)
                        if len(new_rule) is not 0:
                            rules_added = []
                            for rule in new_rule:
                                temp = [rule[0], rule[1] * prob]
                                if temp not in table[j][i]:
                                    rules_added.append(temp)
                                    table[j][i].extend([temp])
                            if rules_added:
                                occu = len(rules_added)
                                bp_table[j][i].extend([[[j, k, table[j][k].index(left_rule)],[k, i, table[k][i].index(down_rule)]]] * occu)

    return table,bp_table

def parse(sentences, start, grammar_dict) :
    table = []
    bp_table = []
    if generateTable(sentences, start, grammar_dict) :
       table,bp_table = generateTable(sentences, start, grammar_dict)

       sentence = sentences.strip().split()
       length = len(sentence)
       if table[0][length]:
           max, index = float("-inf"), 0
           for rule in (table[0][length]):
               prob = rule[1]
               if prob > max:
                  max = prob
                  index = table[0][length].index(rule)
           return parseFromTable(sentence, table, bp_table, 0, length, index)
       else:
           return None
    else:
        return None

# Create parse tree and form a String
def parseFromTable(sentence, table, bp, start, end, root):
    if bp[start][end]:
        list = []
        pre = bp[start][end][root]
        start1 = pre[0][0]
        end1 = pre[0][1]
        left = pre[0][2]
        start2 = pre[1][0]
        end2 = pre[1][1]
        right = pre[1][2]
        list.append(parseFromTable(sentence, table, bp, start1, end1, left))
        list.append(parseFromTable(sentence, table, bp, start2, end2, right))
    else:
        list = [sentence[end - 1]]
    str = table[start][end][root][0]
    str2 = ' '.join(list)
    str3 = "(" + str + " " + str2 + ")"
    return str3
'''
def drawPlot(parsingTime, sentenceLength):
    plt.plot(sentenceLength, parsingTime, 'ro' )
    plt.xlabel('Sentence Length')
    plt.ylabel('Parseing Time')
    plt.title('Parsing time vs Sentence length(Log-Log)')
    plt.show()
'''
def learnGrammar() :
    f1 = open('train.trees.pre.unk', 'r')
    grammar_dict_log = defaultdict(list)
    grammar_dict = defaultdict(list)
    pro_dict = defaultdict(list)
    for line in f1:
        t = Tree.from_str(line)
 #when learn the grammar annotate the node parent at the same time
        for node in t.bottomup():
            if node.label == 'S':
                node.label = 'S_TOP'
            if len(node.children) > 1:
                for child in node.children:
                    if '*' in child.label:
                        child.label = child.label + '_' + node.label
        for node in t.bottomup():
            if node.children == []:
                continue
            elif len(node.children) == 1:
                pro_dict[node.label].append([node.children[0].label])
            else:
                temp = str(node.children[0].label) + ' ' + str(node.children[1].label)
                pro_dict[node.label].append([temp])

    max, left, right = 0, [], []
    for key, value in pro_dict.iteritems():
        rule_dict = defaultdict(int)
        length = len(value)
        for v in value:
            rule_dict[str(v)] += 1
            if rule_dict[str(v)] > max:
                max = rule_dict[str(v)]
                left = [key]
                right = [v]
        for k, v in rule_dict.iteritems():
            prob = (float(v) / float(length))
            grammar_dict[key].append([k[2:-2], prob])
            prob_log = math.log10(float(v) / float(length))
            grammar_dict_log[key].append([k[2:-2], prob_log])


    return grammar_dict,left,right,max

def main():

  parser = argparse.ArgumentParser(description="trivial right-branching parser that ignores any grammar passed in",                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  addonoffarg(parser, 'debug', help="debug mode", default=False)
  parser.add_argument("--infile", "-i", nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="input (one sentence per line strings) file")
  parser.add_argument("--grammarfile", "-g", nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="grammar file; ignored")
  parser.add_argument("--outfile", "-o", nargs='?', type=argparse.FileType('w'), default=sys.stdout, help="output (one tree per line) file")




  try:
    args = parser.parse_args()
  except IOError as msg:
    parser.error(str(msg))

  workdir = tempfile.mkdtemp(prefix=os.path.basename(__file__), dir=os.getenv('TMPDIR', '/tmp'))

  def cleanwork():
    shutil.rmtree(workdir, ignore_errors=True)
  if args.debug:
    print(workdir)
  else:
    atexit.register(cleanwork)


  infile = prepfile(args.infile, 'r')
  outfile = prepfile(args.outfile, 'w')

  grammar_dict ,left,right,max= learnGrammar()

  '''
  # Write to grammar.txt
  f3 = open('grammar.txt', 'w')
  count = 0
  for key, value in grammar_dict.iteritems():
        for v in value:
            count += 1
            f3.write(str(key) + " -> " + str(v[0]) + " # " + str(v[1]) + "\n")
  f3.write("There are " + str(count) + " rules in the grammar" + "\n")
  f3.write("The most common rule is " + str(left) + " -> " + str(right) + "  " + str(max) + "times" + "\n")
  '''

  parseTime,sentenceLen=[],[]
  for line in infile:
        start = time.time()
        tree =parse(line, start,grammar_dict)
        end=time.time()
        if tree is None:
            outfile.write("\n")
        else:
            outfile.write(tree + "\n")
            parseTime.append(math.log10((end - start)))
            sentenceLen.append(math.log10(len(line)))
  #drawPlot(parseTime,sentenceLen)



if __name__ == '__main__':
    main()



