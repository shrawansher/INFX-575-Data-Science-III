from states import states
import sys
import json
import operator
import types

def calculate_score(words,afinn_scores):
    score =0
    for word in words:
        if word in afinn_scores:
            score += afinn_scores[word]

    return score


def extract_words(tweet):
    words = tweet.split(" ")
    return [ word.lower() for word in words if len(word)>1]

def get_happiest_state(afinn_scores,sentiment_score,tweets):
    print()

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    afinn_scores = {}  # initialize an empty dictionary


    for line in sent_file:
        term, score = line.strip().split("\t")  # The file is tab-delimited. "\t" means "tab character"
        afinn_scores[term] = int(score)  # Convert the score to an integer.
    sentiment_score =[]
    state_counts = {}
    state_score = {}

    for line in tweet_file:
        tweet_line = json.loads(line)
        score = 0

        #Fetch tweet text
        if "text" in tweet_line:
            tweet = tweet_line["text"]

        #Extract words
            words = extract_words(tweet)
            score = calculate_score(words,afinn_scores)
        sentiment_score.append(score)


        if "place" in tweet_line:
            if tweet_line["place"] is not None and "full_name" in tweet_line["place"]:
                if tweet_line["place"] is not None and "country_code" in tweet_line["place"]:
                    if tweet_line["place"]["country_code"] == "US":
                        name_line = tweet_line["place"]["full_name"]
                        details = name_line.split()
                        state = details[-1]

                        if state in states:
                            if state in state_score:
                                state_counts[state] = state_counts[state] + 1
                                state_score[state] = state_score[state] + score
                            else:
                                state_counts[state] = 1
                                state_score[state]=score



    for state in state_score:
        state_score[state] = state_score[state]/state_counts[state]

    sorted_states = sorted(state_score.items(), key=operator.itemgetter(1),reverse=True)[:10]

    for state in sorted_states:
        print(state[0], " ", state[1])

if __name__ == '__main__':
    main()