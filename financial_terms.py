import sys
import csv

word_dic = {}

def extract_words(fname):
    """Argument takes a csv file name with .csv attachment.
    return value is a dictionary with all the words and their value attached to it.
    """
    with open(fname,'rt') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            word_dic[row[0].lower()]=int(row[1])
    return word_dic

def compare_headlines(headlines):
    """Argument is the list of headlines gathered from stock name.
    Returns a value number based on comparing thge headline string words
    with values assigned from word_dic.
    """
    total = 0
    
    for line in headlines:
        words = line.split()
        for word in words:
            word=word.lower()
            if word in word_dic:
                total += word_dic[word]
#            else:
#                learning = input("Input value for "+word+ " not found in dictionary: ")
#                word_dic[word] = int(learning)
#                total += int(learning)


    return total
            
            
            
        
    

        
    
