import sys
import json
import operator
def main():
    #Tweet file
    tweet_file = open(sys.argv[1])
    #Dictionary for hashtags
    hashtag_freq ={}

    for line in tweet_file:
        tweet = json.loads(line)
        #Checks if entities tag exist in tweet
        if 'entities' in tweet:
            if 'hashtags' in tweet['entities']:
                tags = tweet['entities']['hashtags']
                for tag in tags:
                    tag_text = tag["text"]
                    #Increments the existing entry by 1 if it exists else initializes to 1
                    if tag_text in hashtag_freq:
                        hashtag_freq[tag_text] +=1
                    else:
                        hashtag_freq[tag_text] =1

    #Sorts the frequency dictionary by the values
    sorted_tags = sorted(hashtag_freq.items(), key=operator.itemgetter(1),reverse=True)[:10]

    for tag in sorted_tags:
        print(tag[0], tag[1])


if __name__ == '__main__':
    main()