
import twitter
#import json  # -> Not using this unless you want to print out strings
import sys
import nltk

if len(sys.argv) < 2:
    print 'Please add search terms to this script '
    print 'for example, $python freq_dist.py lady gaga'
    sys.exit()

search_str = ''
counter = 0
for parts in sys.argv:
    if counter == 0:
        pass
    else:
        search_str += parts + ' '
    counter = counter + 1


twitter_search = twitter.Twitter(domain="search.twitter.com")
search_results = []
for page in range(1,6):
    search_results.append(twitter_search.search(q=search_str, rpp=100, page=page))

#print json.dumps(search_results, sort_keys=True, indent=1)

tweets = [ r['text'] \
    for result in search_results \
        for r in result['results'] ]
words = []
for t in tweets:
    words += [ w for w in t.split() ]

print 'total words: ' + str(len(words))
if len(words) == 0:
    sys.exit()
    # We don't want to divide by zero down below so bail out if you don't have any words

print 'unique words: ' + str(len(set(words))) 

print 'lexical diversity: ' + str(1.0*len(set(words))/len(words))

print 'avg words per tweet: ' + str(1.0*sum([ len(t.split()) for t in tweets ])/len(tweets))

freq_dist = nltk.FreqDist(words)

print '50 most frequent tokens: '
str_of_toks = ''
for tok in freq_dist.keys()[:50]:
    str_of_toks += tok + ' '

print str_of_toks

