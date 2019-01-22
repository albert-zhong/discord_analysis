# -*- coding: utf-8 -*-
from textblob import TextBlob
from unidecode import unidecode

def remove_non_ascii(text):
    return unidecode(unicode(text, encoding = "utf-8"))

def average(list):
    polaritySum = 0
    subjectivitySum = 0
    for currentTuple in list:
        polaritySum += currentTuple[0]
        subjectivitySum += currentTuple[1]
    return (polaritySum/len(list), subjectivitySum/len(list))

def main():
    lines = open("/home/albert/workspace/coffee/discord_analysis/western_frontier.txt", "r")

    albert_data = []
    lifan_data = []
    ansen_data = []
    daniel_data = []
    eric_data = []

    last_line = ""
    for current_line in lines:
        current_line = remove_non_ascii(current_line)
        if "Changed the channel name." not in current_line and "Added a recipient." not in current_line and "Started a call." not in current_line and "https" not in current_line:
            if "olux#0673" in last_line:
                albert_data.append(TextBlob(current_line[:-1]).sentiment)
            if "green#2773" in last_line:
                lifan_data.append(TextBlob(current_line[:-1]).sentiment)
            if "Chibba#5643" in last_line:
                ansen_data.append(TextBlob(current_line[:-1]).sentiment)
            if "Twangybeast#1791" in last_line:
                daniel_data.append(TextBlob(current_line[:-1]).sentiment)
            if "Epik Xiang#0788" in last_line:
                eric_data.append(TextBlob(current_line[:-1]).sentiment)
        last_line = current_line

    print("Albert:")
    print(average(albert_data))
    print("Lifan:")
    print(average(lifan_data))
    print("Ansen:")
    print(average(ansen_data))
    print("Daniel:")
    print(average(daniel_data))
    print("Eric:")
    print(average(eric_data))

main()