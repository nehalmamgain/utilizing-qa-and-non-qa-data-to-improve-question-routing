# -*- coding: utf-8 -*-
"""
Created on Wed Feb 07 09:46:04 2018

@author: Nehal
"""

from newspaper import Article
import re
import unicodedata

a = open('user_internal_nonqa_info.txt')
b = open('user_external_nonqa_info_homepage_text.txt', 'w')


anchrPtrn   = re.compile('(<[^>]*>)|(</\w+>)|\\n')


for i, line in enumerate(a):
    fields = line.split('\t')
    
    flagMe = 0 # text on homepage or not
    seed = '!'
    output = fields[0]+'\t'
        
#    if i == 59735:
 #       output += '!\n'
  #      b.write(output)
   #     continue

    if 'http://twitter.com/' not in fields[2] and fields[2] != '!':
        seed = fields[2]
        try:
            article = Article(seed)
        except Exception, e:
            seed = '!'
    
    if seed != '!': # there is a homepage
        try:
            article.download()
            article.parse()
            content = article.text.strip()
            if len(content) >= 1:
                flagMe = 1 # found text on site
                content = anchrPtrn.sub('',content)
                if type(content) != str:
                    content = unicodedata.normalize('NFKD', content).encode('ascii','ignore')
        except Exception, e:
            print e
    if flagMe == 1:
        output += content + '\n'
    else:
        output += '!\n'
         
    b.write(output)
    print 'Done for line %d' %i

b.close()
