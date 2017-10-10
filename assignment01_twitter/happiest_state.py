from states import states
import sys
import json
import operator
import re

def calculate_score(words,afinn_scores):
    score =0
    for word in words:
        if word in afinn_scores:
            score += afinn_scores[word]

    return score


def extract_words(tweet):
    words = re.split('\W+',tweet)
    return [ word.lower() for word in words if len(word)>0]

def get_happiest_state(afinn_scores,sentiment_score,tweets):
    print()

def get_state_code(stateName):
    for s in states:
        if states[s] == stateName:
            return s
    return None

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    afinn_scores = {}  # initialize an empty dictionary

    count = 0
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

        found = False

        #Look in place tag
        if "place" in tweet_line:
            place = tweet_line["place"]

            if place is not None and "place_type" in place:
                place_type= place["place_type"]
                if place_type is not None and "country_code" in place and place["country_code"] == "US" :
                    #Case 1: when place_type is city look for the state code at the end of text
                    if place_type =="city" and "full_name" in place :

                        name_line = place["full_name"]
                        details = name_line.split()
                        state = details[-1]

                        if state in states:
                            count += 1
                            found = True
                            if state in state_score:
                                state_counts[state] = state_counts[state] + 1
                                state_score[state] = state_score[state] + score
                            else:
                                state_counts[state] = 1
                                state_score[state]=score

                    #Case 2: when place_type is admin look for the state name
                    if place_type =="admin" and "name" in place:

                        state_name = place["name"]
                        state = get_state_code(state_name)

                        if state is not None:
                            count += 1
                            if state in state_score:
                                found =True
                                state_counts[state] = state_counts[state] + 1
                                state_score[state] = state_score[state] + score

        #If state is not found in place tag look in user
        if found == False:
            if  "user" in tweet_line and tweet_line["user"] is not None:
                if "location" in tweet_line["user"] and tweet_line["user"]["location"] is not None:
                    details = tweet_line["user"]["location"].split(" ")

                    state = details[-1]

                    if state in states:
                        count +=1
                        if state in state_score:
                            state_counts[state] = state_counts[state] + 1
                            state_score[state] = state_score[state] + score
                        else:
                            state_counts[state] = 1
                            state_score[state] = score




    #Calculate the average score for each state
    for state in state_score:
        state_score[state] = state_score[state]/state_counts[state]

    #Sort the scores and select the highest
    sorted_states = sorted(state_score.items(), key=operator.itemgetter(1),reverse=True)[:1]

    for state in sorted_states:
        print(states[state[0]])

if __name__ == '__main__':
    main()