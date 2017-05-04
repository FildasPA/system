#!/usr/bin/python
#coding: utf-8


import feedparser

feed = feedparser.parse('http://www.cert.ssi.gouv.fr/site/cert-fr_alerte.rss')

if not feed.entries:
	print "No entry. No connection ?"
	exit(0)

print feed.entries[0].title

# for entry in feed.entries:
    # print entry.title




    # print entry
    # content = urlopen(entry['link']).read()
# for post in feed.entries:
 #        if post is already in the database, skip it
 #        TODO check the time
        # if post_is_in_db_with_old_timestamp(title):
            # posts_to_skip.append(title)
 #        else:
 #            posts_to_print.append(title)


# import feedparser
# import time
# from subprocess import check_output
# import sys
# import codecs

# feed_name = 'TRIBUNE'
# url = 'http://www.cert.ssi.gouv.fr/site/cert-fr_alerte.rss'

# # feed_name = sys.argv[1]
# # url = sys.argv[2]

# db = '/home/fildas/dev/adminsys-projet/feeds.db'
# limit = 12 * 3600 * 1000

# #
# # function to get the current time
# #
# current_time_millis = lambda: int(round(time.time() * 1000))
# current_timestamp = current_time_millis()

# def post_is_in_db(title):
#     with open(db, 'r') as database:
#         for line in database:
#             if title in line:
#                 return True
#     return False

# # return true if the title is in the database with a timestamp > limit
# def post_is_in_db_with_old_timestamp(title):
#     with open(db, 'r') as database:
#         for line in database:
#             if title in line.encode('utf-8'):
#                 ts_as_string = line.split('\xe9'.encode('utf-8'), 1)[1]
#                 ts = long(ts_as_string)
#                 if current_timestamp - ts > limit:
#                     return True
#     return False

# #
# # get the feed data from the url
# #
# feed = feedparser.parse(url)

# #
# # figure out which posts to print
# #
# posts_to_print = []
# posts_to_skip = []

# for post in feed.entries:
#     # if post is already in the database, skip it
#     # TODO check the time
#     title = post.title.encode('utf-8')
#     if post_is_in_db_with_old_timestamp(title):
#         posts_to_skip.append(title)
#     else:
#         posts_to_print.append(title)

# #
# # add all the posts we're going to print to the database with the current timestamp
# # (but only if they're not already in there)
# #
# f = codecs.open(db, 'a', encoding='utf-8')
# for title in posts_to_print:
#     if not post_is_in_db(title):
#       line = title + "|" + str(current_timestamp) + '\n'
#       f.write(line)
# f.close

# #
# # output all of the new posts
# #
# count = 1
# blockcount = 1
# for title in posts_to_print:
#     if count % 5 == 1:
#         print("\n" + time.strftime("%a, %b %d %I:%M %p") + '  ((( ' + feed_name + ' - ' + str(blockcount) + ' )))')
#         print("-----------------------------------------\n")
#         blockcount += 1
#     print(title + "\n")
#     count += 1







# import urllib

# response = urllib.urlopen('http://www.cert.ssi.gouv.fr/site/cert-fr_alerte.rss')
# print 'RESPONSE:', response
# print 'URL     :', response.geturl()
# print 'URL     :', response.()

# print response.title()
# headers = response.info()
# print 'DATE    :', headers['date']
# print 'HEADERS :'
# print '---------'
# print headers

# data = response.read()
# print 'LENGTH  :', len(data)
# print 'DATA    :'
# print '---------'
# print data
