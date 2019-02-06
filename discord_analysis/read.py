from textblob import TextBlob
from unidecode import unidecode
import csv

def is_safe(str):
    if str.isspace() or "Changed the channel name." in str or "Added a recipient." in str or "Started a call." in str or "https" in str:
        return False
    else:
        return True
    
def remove_non_ascii(str):
    return unidecode(unicode(str, encoding = "utf-8"))

# create the set of the authors
authors = {}

with open("/home/albert/workspace/discord_analysis/data/Direct Messages - WESTERN FRONTIER.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        if is_safe(row[2]):
            row[2] = remove_non_ascii(row[2]) # Removes non-ASCII characters
            blob = TextBlob(row[2]) # Creates TextBlob for current line
            if row[0] not in authors:
                authors[row[0]] = [blob.polarity, 1]
            else:
                authors[row[0]][0] += (blob.polarity*len(row[2]))
                authors[row[0]][1] += 1

authors.pop("Author")

for x in authors:
    authors[x][0] = authors[x][0] / authors[x][1]

print(authors)
