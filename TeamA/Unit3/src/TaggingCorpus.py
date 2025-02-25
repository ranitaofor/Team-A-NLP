'''
  Separates the text in ClassEvent sentences and tags them in the appropriate
  manner.
'''
from __future__ import division
import nltk
from nltk.corpus import PlaintextCorpusReader
import sys, os
from nltk.probability import FreqDist
# #####################sets up the path######
currPath = os.path.abspath("")
startPath = 0
endPath = len(currPath) - 1
pathSrc = currPath[0:endPath - 9] + '/lib/src/'
pathClass = currPath[0:endPath - 9] + '/lib/ClassCode/'
sys.path.append(pathSrc)
sys.path.append(pathClass)
from FilterFiles import extractTxtArticle, removeStopWords
from AnalysisWords import *
##########################################


#a text of body that needs to ?
def getTagCorpus(textToks):
    listOfAllTags, listOfTags = [], []
    for sent in textToks:
        toks = nltk.word_tokenize(sent)  # toks= list of tokens in a sentence
        tags = nltk.pos_tag(toks)  # tags = list of tuples (token/word, tag)
        listOfTags.append(tags)
        for t in tags:
            listOfAllTags.append(t)
    #print 'Printing listOfAllTags'
    #print listOfAllTags
    return listOfAllTags


def getOurTagCorpus(textToks):
    from cPickle import load

    inp = open('TrigramTagger.pkl', 'rb')
    tagger = load(inp)
    inp.close()
    listOfAllTags, listOfTags = [], []
    for sent in textToks:
        toks = nltk.word_tokenize(sent)  # toks= list of tokens in a sentence
        tags = tagger.tag(toks)  # tags = list of tuples (token/word, tag)
        listOfTags.append(tags)
        for t in tags:
            listOfAllTags.append(t)
    #print 'Printing listOfAllTags'
    #print listOfAllTags
    return listOfAllTags


#compares the list when there are nouns that are filtered
#and ones that are not filtered
def getNouns(listTags):
    listOfAllNouns = [a.lower() for (a, b) in listTags if b[0] == 'N' and b != "NUM" and len(a) > 2]
    return listOfAllNouns


def getNounsExceptNN_NC(listTags):
    listOfAllNounsExceptNN_NC = [a.lower() for (a, b) in listTags if
                                 b[0] == 'N' and b != "NUM" and b != "NN-NC" and len(a) > 2]
    return listOfAllNounsExceptNN_NC


def getVerbs(listTags):
    listOfAllVerbs = [a.lower() for (a, b) in listTags if b[0] == 'V' and b != "NUM" and len(a) > 2]
    return listOfAllVerbs


def getAdjs(listTags):
    listOfAllAdjs = [a.lower() for (a, b) in listTags if b[0] == 'J' and b[1] == 'J']
    return listOfAllAdjs


#returns summary of the tags based on:
#  1. FreqDist
#  2. Not in Stop Words
def getPOS(listOfWords):
    #distWords = getFreqDist(listOfWords, 10)
    freqd = FreqDist(listOfWords)  #simulates freqdist obtained from reducer
    distWords = getReducerFreqDist(freqd, listOfWords, 50)
    swFreeWords = removeStopWords(distWords)
    return swFreeWords


#compares the result we had gotten from solr
def compareSolr(wordsPOS):
    results, solrWords = " some results ", []
    return results

def getAdjs(listTags):
    listOfAllAdjs = [a.lower() for (a, b) in listTags if b [0]== 'J' and b[1]=='J']
    return listOfAllAdjs


def extractTopPOS(location, descriptionLocation):
    CEcorpus_root = location

    CEWordLists = PlaintextCorpusReader(CEcorpus_root, ".*\.txt")
    CE = CEWordLists.raw()  # read all texts, CE = string of all texts

    extractTxt = extractTxtArticle(CE)  #list of lines separated by \n
    #print "this is the CE",  CE
    if len(extractTxt) == 0:
        extractTxt = CE
    CE = "".join(extractTxt)  # CE now is a string with all lines of all texts

    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    CEsents = sent_tokenizer.tokenize(CE)  # CEsents= list of sentences(strings)

    listOfAllTags = getOurTagCorpus(CEsents)  # list of tuples (word, tag)

    allNouns = getNouns(listOfAllTags)  # allNouns= list of all nouns
    posSum = getPOS(allNouns)  #posSum= list of top stop-word free nouns

    nounsExceptNN_NC = getNounsExceptNN_NC(listOfAllTags)  # nounsExceptNN_NC= list of all nouns
    topNounsExceptNN_NC = getPOS(nounsExceptNN_NC)  # topNounsExceptNN_NC= list of top stop-word free nouns

    allVerbs = getVerbs(listOfAllTags)  # allNouns= list of all nouns
    topVerbs = getPOS(allVerbs)  #posSum= list of top 10 stop-word free nouns
    topAdjs = getAdjs(listOfAllTags)
    print listOfAllTags
    #print "These are the list of top nouns in the ", descriptionLocation, '\n', len(posSum)

    #print "These are the list of top nouns in the class event corpus\n", len(posSum)

    print "These are the list of top verbs in the ", descriptionLocation,  "Corpus \n", len(topVerbs)
    for x in topVerbs:
        print x

    print "These are the list of top adjectives in the class event corpus\n", len(topAdjs)
    for x in topAdjs:
        print x


    print 'Printing top (stop-word free) nouns '
    for x in posSum:
        print x

    print "These are the list of top nouns EXCEPT NN-NC in the", descriptionLocation,  "\n", len(topNounsExceptNN_NC)

    for x in topNounsExceptNN_NC:
        print x

    print "These are the list of top adjectives in the class event corpus\n", len(topAdjs)
    for x in topAdjs:
        print x

#extractTopPOS('../../lib/Corpus/ClassEvent', 'class event')
extractTopPOS('../output/SolrOutputFolder', 'solr folder')
