import sys
import json
import re

# Calculates the sentiment score for a tweet
def calculate_score(words,afinn_scores):
    score =0
    for word in words:
        if word in afinn_scores:
            score += afinn_scores[word]

    return score

# Creates a word list from a tweet
def extract_words(tweet):
    words = re.split('\W+',tweet)
    return [ word.lower() for word in words if len(word)>0]

def main():
    #AFINN file
    sent_file = open(sys.argv[1])
    #Tweet File
    tweet_file = open(sys.argv[2])

    #Dictionary to store afinn scores
    afinn_scores = {}

    #Saves Afinn scores
    for line in sent_file:
        term, score = line.strip().split("\t")
        afinn_scores[term] = int(score)

    sentiment_score =[]


    for line in tweet_file:
        tweet_line = json.loads(line)
        score = 0

        #Fetch tweet text
        if "text" in tweet_line:
            tweet = tweet_line["text"]

        #Extract words
            words = extract_words(tweet)
            #Fetch scores for each tweet
            score = calculate_score(words,afinn_scores)

        sentiment_score.append(score)

    for score in sentiment_score:
        print(score)
    
if __name__ == '__main__':
    main()



