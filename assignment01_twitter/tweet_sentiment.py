import sys
import json
import re

def hw():
    print('Hello, world!')

def lines(fp):
    print(str(len(fp.readlines())))

def calculate_score(words,afinn_scores):
    score =0
    for word in words:
        if word in afinn_scores:
            score += afinn_scores[word]

    return score


def extract_words(tweet):
    words = tweet.split(" ")
    return [ word.lower() for word in words if len(word)>1]

def main():
    sent_file = open(sys.argv[1])

    tweet_file = open(sys.argv[2])
    #tweet_json = json.loads(tweet_file)
    #print(tweet_json)
    #print(tweet_file)
    #tweet_file = json.loads(tweet_file.decode("utf-8"))

    afinn_scores = {}  # initialize an empty dictionary
    for line in sent_file:
        term, score = line.strip().split("\t")  # The file is tab-delimited. "\t" means "tab character"
        afinn_scores[term] = int(score)  # Convert the score to an integer.
    sentiment_score =[]
    #tweet_sentiments = {}

    for line in tweet_file:
        print(type(line))
        tweet_line = json.loads(line)
        score = 0
        #Fetch tweet text
        if "text" in tweet_line:
            tweet = tweet_line["text"]
            print(tweet)
            #tweet = tweet.encode('ascii', 'ignore')
            print(tweet)

        #Extract words
            words = extract_words(tweet)

            score = calculate_score(words,afinn_scores)
        sentiment_score.append(score)


    print(sentiment_score)



    
    
if __name__ == '__main__':
    main()
   # afinnfile = open("AFINN-111.txt")

   # tweet_file = open("output.txt")


