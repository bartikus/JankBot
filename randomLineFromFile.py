import os
import sys
import nltk #Used for tagging parts of speech
import random

# Get a radom line from a file:
def random_line(quoteFile):
    selected_line = ''
    with open(quoteFile) as f:
        selected_line = random.choice([rand_quote for rand_quote in f])
    return selected_line.strip()

# These words are not to be replaced because they often result in a
# "jank janked" scenario:
def on_blacklist(word):
    blacklist = ('be','is','was','are')
    for words in blacklist:
        if(word == words):
            return True
    return False

if __name__=='__main__':
    #Get the path to the directory of this script (used to open the text
    # file of quotes):
    rootdir = os.path.dirname(__file__)

    # The list of words with their parts of speech to replace words in
    # the original quote:
    replacementList = [ ('jank','crank','VB'),
                        ('janked','cranked','VBD'),
                        ('janking','cranking','VBG'),
                        ('janked','cranked','VBN'),
                        ('jank','crank','VBP'),
                        ('jank','crank','VBZ')]
                        #('jank','crank','NN')]

    #Get a random quote from the file of quotes:
    quote = random_line(os.path.join(rootdir,'fortunes.txt'))
    print(quote)

    #Tokenize the words in the quote (parse into individual words for tagging):
    tokens = nltk.word_tokenize(quote)
    #print(tokens)

    #Tag the tokens with their parts of speech:
    tagged = nltk.pos_tag(tokens)
    #print(tagged)

    #Replace all verbs and count nouns:
    jankedQuote = quote
    nounsList = list('')
    for words in tagged:
        for pos in replacementList:
            if(words[1]=='NN'):
                nounsList.append(words[0])
            elif(words[1] == pos[2]):
                if(not on_blacklist(words[0])):
                    sub = pos[random.getrandbits(1)]
                    #print('replacing', words[0], ' with ', sub)
                    jankedQuote = jankedQuote.replace(str(words[0]), str(sub), 1)

    # Replace just one random noun:
    if(len(nounsList) != 0):
        selectedNoun = 0
        subs = ['jank','crank']

        if(len(nounsList) > 1):
            selectedNoun = random.randrange(0,len(nounsList)-1)
        jankedQuote = jankedQuote.replace(nounsList[selectedNoun],random.choice(subs))

    print(jankedQuote.title())
