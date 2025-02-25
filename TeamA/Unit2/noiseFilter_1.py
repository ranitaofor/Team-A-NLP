
# Scrape useless noise from Texas */*.txt files
def is_ascii(s):
    return all(ord(c) < 128 for c in s)

#analyzes the text based on the number of lines in comparison to the words of a text file
#if there are more lines than text then it's not an article. (Interesting to look at whether a
#   cluster of text may indicate that the text is an article)
#If it's an article then we use a k-means clustering to look at: 
#   - top 10 most frequent words
#   - top collocation phrases   
#If it's not an article then we report:
#   - top 5 most frequent words
#   - find the common phrases
#Question: which one is better? common phrases for an article or most frequent words in 
#                                                                   a non-article
def classifyTxt(strTxt):
    if strTxt == None: 
        print "parameter cannot be empty"
    else:
        numNewLines = 0
        for c in strTxt: 
            if c == '\n':
                numNewLines += 1
        if numNewLines < len(strTxt.split()) and numNewLines != 0:
            return True
        else: 
            return False

#extracts a chunk of text that are similar distance to one another, assuming that the
#article is double or single spaced. 
#returns the extracted text
'''Need to ask Dr. Fox what the best approach would be to classify a particular text: 
    according to the chunk it belongs to, but since for this program we are not classify
    the text on a particular file, we just want to know which content is the most relevant'''
def extractTxtArticle(strTxt):
    strTxt = strTxt.splitlines()
    extractTxt = []
    for r in range(len(strTxt)):
        if len(strTxt[r].strip(' ')) >= 80 and '|' not in strTxt[r] and '#' not in strTxt[r]:
            extractTxt.append(strTxt[r])
    return extractTxt
