#!/usr/bin/env python
import sys
import cPickle
from cPickle import load
import re
#import zipimport
#importer = zipimport.zipimporter('nltk.mod')
#nltk = importer.load_module('nltk')
#nltk.data.path += ["./nltkData/"]

#import featureList
#input= open('/home/cla/UITeamA/Unit4/src/featureList.pkl','rb')
input= open('featureList.pkl','rb')
featureList= load(input)
input.close()
# import best classifier model
#input = open('/home/cla/UITeamA/Unit4/src/classifierModel.pkl', 'rb')
input = open('classifierModel.pkl', 'rb')
classifier = load(input)
input.close() 
# input is file with fullpath filenames
for line in ['../../Unit2/output/TexasExtractedFiles/1.txt\n']:
    #assume line is the full path for a file
    currentFile = open(line[:-1])
    #extract features
    text= currentFile.read()
    featureset={}
    for word in featureList:
        if re.search(word, text):
            featureset[word]= True
        else:
            featureset[word]= False        
    print line[:-1]+'\t'+ classifier.classify(featureset)
    
    


    
