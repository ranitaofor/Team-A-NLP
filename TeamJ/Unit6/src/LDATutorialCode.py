'''
#Topic identification using LDA (gensim) example-Code:
#Created on Oct 15, 2014
#Authors: Xuan Zhang and Tarek Kanan
'''


from gensim import corpora, models
from nltk.corpus import stopwords

#Call the NLTK stop words list
stoplist = stopwords.words('english')

documents = ["Computational Linguistics, sometimes called Natural Language Processing (NLP), is a new course at VT.",
             "With support from a grant from the National Science Foundation, Computing in Context, and resulting subaward from Villanova to Virginia Tech,",
             "this course will give students the opportunity to engage in active learning about how to work with large collections of text, one aspect of 'big data'.",
             "A tailored Cloudera virtual machine (VM), and an 11-node Hadoop cluster, along with other tailored computing resources, will aid handling of over 500 million tweets and over 11 terabytes of webpages.",
             "Using methods employed in search engines, including linguistic analysis and NLP, as well as statistical techniques,",
             "students will engage in problem based learning with the semester long challenge of analyzing content collections automatically,",
             "extracting key information, and generating easily readable summaries of important events in English.",
             "Just-in-time learning will allow development of an understanding of concepts, techniques, and toolkits"]

#Remove the stop words
texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

#Build the dictionary and the corpus
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

#Define the LDA model and the number of topics.
notopics = 3
lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=notopics)

#Printing the topic with their probabilities
print "\n\n", notopics, "Topics with their corresponding probabilities\n"
for i in range(0, lda.num_topics):
    print "Topic", i+1, ":", lda.print_topic(i)

