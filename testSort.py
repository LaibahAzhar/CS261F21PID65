import csv
from Sorting import bubble_Sort


def read_file():
    with open('twitter.csv')as r:
        reader = csv.reader(r)
        for row in reader:
            timeStamp=(row[4])
            
        return timeStamp

bubble_Sort(read_file())
