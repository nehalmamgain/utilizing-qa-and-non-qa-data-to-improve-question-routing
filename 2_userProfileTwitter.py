# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:44:00 2018

@author: Nehal
"""
# output: user name, about me

import tweepy
a = open('user_internal_nonqa_info.txt')
b = open('user_external_nonqa_info.txt', 'w')

consumer_key = 'E5ariPVOfo1M5NaJ5cXRkE3v5'
consumer_secret = 'tqYrq9oDg09RyqaXw1BgEZm7vXYQ46wgzCMY8ica9EdOjkaRrr'
access_token = '3269924305-X7C2hNTFnNcwJX2Tq1HL58uyx0hP53qkY4u4cAo'
access_token_secret = 'DaxuMGOyfIOr4s00tIk5bpWOcvzWBsERtLEmvJ6BSsbOC'

auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

for i, line in enumerate(a):
    fields = line.split('\t')
    
    twitterMe = '!'
    username = ''
    output = fields[0]+'\t'
    #also need homepage
    if 'http://twitter.com/' in fields[2]:
        username = fields[2][fields[2].find('m/')+2:]
    elif 'http://twitter.com/' in fields[3]:
        username = fields[3][fields[3].find('http://twitter.com/')+19:fields[3].find('&quot')]
    
    if username != '': # there is a twitter link in either aboutMe or homepage
        try:
            user = api.get_user(username)
            twitterMe = str(user.description)
        except Exception, e:
            twitterMe = str(type(e)) + ' for user '+username
    output += twitterMe + '\n'# no author found
 
    b.write(output)
    print 'Done for line %d' %i

b.close()
