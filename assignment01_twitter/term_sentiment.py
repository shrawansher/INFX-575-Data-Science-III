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
    new_words={}
    new_words_count ={}
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
        score = 0
        tokens = re.split('\W+', tweet)
        words = [ word.lower() for word in tokens if len(word)>0]

        for word in words:
            if word in afinn_scores:
                score += int(afinn_scores[word])


        tweet_scores[tweet] = score

    #Calculate the scores for the new words

    for tweet in tweets:
        score = tweet_scores[tweet]
        tokens = re.split('\W+', tweet)
        words = [ word.lower() for word in tokens if len(word)>0]


        for word in words:
            if word not in afinn_scores:
                if word not in new_words:
                    new_words[word] = score
                    new_words_count[word] = 1
                else:
                    new_words[word] += score
                    new_words_count[word] +=1

    for word, sum_score in new_words.items():
        print(word, sum_score/new_words_count[word])


if __name__ == '__main__':
    main()
