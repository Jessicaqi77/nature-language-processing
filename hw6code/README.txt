To get LR python evaluation:
python main.py -e data/twitter dev.ner data/twitter dev test.ner data/twitter_test.ner
And then to get LR CONLL evaluation:
perl data/conlleval.pl -d \\t < twitter dev.ner.pred
perl data/conlleval.pl -d \\t < twitter dev_test.ner.pred

To get CRF python evaluation:
python main.py -T crf -e data/twitter dev.ner data/twitter dev test.ner data/twitter_test.ner
And then to get CRF CONLL evaluation:
perl data/conlleval.pl -d \\t < twitter dev.ner.pred
perl data/conlleval.pl -d \\t < twitter dev_test.ner.pred


