import sys
import json
import re


def read_scores(sent_file):
    with open(sent_file) as f:
        return {line.split('\t')[0]: int(line.split('\t')[1]) for line in f}


def score_tweet(tweet, scores):
    return sum(scores.get(word, 0) for word in tweet)

def main():
    sent_file = open(sys.argv[1])

    tweet_file = open(sys.argv[2])

    afinn_scores = {}
    tweet_scores={}
    new_words=[]
    tweets = []



    for line in sent_file:
        word, score = line.strip().split("\t")
        afinn_scores[word] = score

    #Store the new tweets
    for line in tweet_file:
        tweet = json.loads(line)
        if 'text' in tweet:
            text = tweet['text'].lower()
            tweets.append(text)

    #Calculate scores

    for tweet in tweets:
        #print(tweet)
        score = 0
        words = tweet.split()

        for word in words:
            if word in afinn_scores:
                score += int(afinn_scores[word])

            else:
                new_words.append(word)
            tweet_scores[tweet] = score

    #Calculate the scores for the new words

    for word in new_words:
        pos =0
        neg =0
        total=0
        for tweet in tweet_scores:
            if word in tweet:
                if tweet_scores[tweet]>0:
                    pos+=1
                elif tweet_scores[tweet]<0:
                    neg+=1

                total+=1


        print(word,":",(pos-neg)/total)








if __name__ == '__main__':
    main()
