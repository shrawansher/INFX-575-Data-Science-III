import sys
import json
import operator
def main():
    tweet_file = open(sys.argv[1])
    hashtag_freq ={}

    for line in tweet_file:
        tweet = json.loads(line)
        if 'entities' in tweet:
            if 'hashtags' in tweet['entities']:
                tags = tweet['entities']['hashtags']
                for tag in tags:
                    tag_text = tag["text"]
                    if tag_text in hashtag_freq:
                        hashtag_freq[tag_text] +=1
                    else:
                        hashtag_freq[tag_text] =1

    sorted_tags = sorted(hashtag_freq.items(), key=operator.itemgetter(1),reverse=True)[:10]

    for tag in sorted_tags:
        print(tag[0], " ", tag[1])


if __name__ == '__main__':
    main()