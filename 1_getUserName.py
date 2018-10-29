# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 08:40:00 2018

@author: Nehal
"""
# output: user ID, user name, user homepage, about me

a = open('Users.xml').readlines()
b = open('user_internal_nonqa_info.txt', 'w')

for i, line in enumerate(a):
    fields = line.split('" ')
    
    userId = '!'
    username = '!'
    homepage = '!'
    aboutMe = '!'
    
    for j in fields:
        if 'AccountId' in j:
            userId = j[j.find('"')+1:]
        elif 'DisplayName' in j:
            username = j[j.find('"')+1:]
        elif 'WebsiteUrl' in j:
            homepage = j[j.find('"')+1:]
        elif 'AboutMe' in j:
            aboutMe = j[j.find('"')+1:]
        
    output = userId + '\t' + username + '\t' + homepage + '\t' + aboutMe + '\n'
    b.write(output)
    print 'Done for line %d' %i

b.close()
