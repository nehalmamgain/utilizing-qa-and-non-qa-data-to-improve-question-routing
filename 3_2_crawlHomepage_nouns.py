# -*- coding: utf-8 -*-
"""
Created on Wed Feb 07 09:46:04 2018

@author: Nehal
"""
import nltk

a = open('user_external_nonqa_info_homepage_text.txt')
b = open('user_external_nonqa_info_homepage_nouns.txt', 'w')



for i, line in enumerate(a):
    if line!='!':
        tokens = nltk.word_tokenize(line)
        tagged = nltk.pos_tag(tokens)
        nouns = [word for word,pos in tagged if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]
        output = " ".join(nouns)
        output += '\n'
    else:
        output='!\n'
    b.write(output)
    print 'Done for line %d' %i

b.close()
