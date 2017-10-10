import sys
import json
import re

def main():
    tweet_file = open(sys.argv[1])
    #Dictionary for word frequency
    word_freq ={}
    total_words =0

    for line in tweet_file:
        tweet = json.loads(line)
        if 'text' in tweet:
            tweet_text = tweet['text']
            tokens = re.split('\W+', tweet_text)
            words = [word.lower() for word in tokens if len(word) > 0]

            for word in words:
                # Increments the existing entry by 1 if it exists else initializes to 1
                if word in word_freq:
                    word_freq[word] = word_freq[word]+1
                else:
                    word_freq[word]=1

                total_words +=1

    for t in word_freq:
        print(t, word_freq[t]/total_words)


if __name__ == '__main__':
    main()