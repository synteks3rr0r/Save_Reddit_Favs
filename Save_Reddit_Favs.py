import praw
import urllib
import datetime
import time

reddit = praw.Reddit(client_id='my_client_id', 
                     client_secret='my_client_secret',
                     user_agent='my_user_agent',
                     password = 'my_password',
                     username = 'my_username')

_image_formats = ['mp3','avi','png','jpg']

# print 'Hello world'
i = 0

for submission in reddit.redditor('my_reddit_username').saved(limit=None):

  count = 0
  dotPos = 0
  dotPos2 = 0
  dotPos3 = 0
  finalPos = 0

  print "Found URL: %s" %submission.url

  while count < 3:
    dotPos = submission.url.find('.')+1
    # print dotPos
    dotPos2 = dotPos + submission.url[dotPos:].find('.')+1
    if dotPos2 == dotPos:
      print "Did not add URL: %s \r\n" %submission.url
      break
    dotPos3 = dotPos2 + submission.url[dotPos2:].find('/')+1
    # print dotPos3
    count += 1

  for eachFileType in _image_formats:
    if submission.url[dotPos3:].find(eachFileType) > -1:
      filePos = submission.url.find(eachFileType)
      finalFileType = submission.url[dotPos3:filePos+4]
      finalFileType = finalFileType.replace('/','_')
      finalFileType = finalFileType.replace('-','_')
      # print submission.url

      try:
        urllib.urlretrieve(submission.url, 'E:\\Python27\\RedditSaved\\'+finalFileType)
        print "Added file: %s \r\n" %finalFileType
        time.sleep(.05)
      except:
        break