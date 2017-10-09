import sys
import json

def main():
    tweet_file = open(sys.argv[1])
    word_freq ={}
    total_words =0

    for line in tweet_file:
        tweet = json.loads(line)
        if 'text' in tweet:
            words = tweet['text'].lower().split(" ")
            for word in words:
                if word in word_freq:

                    word_freq[word] = word_freq[word]+1
                else:
                    word_freq[word]=1

                total_words +=1


    for t in word_freq:
        print(t, " ", word_freq[t]/total_words)




if __name__ == '__main__':
    main()