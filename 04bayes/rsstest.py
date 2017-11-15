import feedparser
import bayes
ny = feedparser.parse('https://newyork.craigslist.org/d/community/search/ccc')
#print ny
nasa = 'https://www.yahoo.com/entertainment/rss.xml'  
news = 'https://www.yahoo.com/news/rss.xml'
#url = 'http://www.xinhuanet.com/politics/news_politics.xml'  
feed1 = feedparser.parse(nasa) 
feed2 = feedparser.parse(news) 

print len(feed1['entries'])
print len(feed2['entries'])

#print  feed1['entries'][0]['summary']
#print bayes.textParse1(feed1['entries'][0]['summary'])
# print feed1.entries[0]
# for i in range(50):
#         wordList = textParse(feed1['entries'][i]['summary'])
#         docList.append(wordList)
#         fullText.extend(wordList)
#         classList.append(1) #nasa is class 1
#         wordList = textParse(feed0['entries'][i]['summary'])
#         docList.append(wordList)
#         fullText.extend(wordList)
#         classList.append(0) #news is class 0
bayes.localWords(feed1,feed2)