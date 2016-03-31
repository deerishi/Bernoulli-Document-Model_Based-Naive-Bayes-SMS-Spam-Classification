import json
import numpy as np
import nltk
from os.path import expanduser
import simplejson

spamDict={'SPAMCOUNT':0}
hamDict={'HAMCOUNT':0}



def saveFile(data,name):
    with open(name+'.txt', 'w') as outfile:
        json.dump(data, outfile)

def wcount(filename):
    f=open(filename,'r')
    dictionary=[]
    for line in f:
        words=nltk.word_tokenize(line)
        #words.remove('\n')
        for w in words[1:]:
            if w not in dictionary:
                dictionary.append(w)
        if(words[0]=='ham'):
            hamDict['HAMCOUNT']+=1
            for i in range(1,len(words)):
                word=words[i]
                if word in hamDict:
                    hamDict[word]+=1
                else:
                    hamDict[word]=1
        else:
            spamDict['SPAMCOUNT']+=1
            for i in range(1,len(words)):
                word=words[i]
                if word in spamDict:
                    spamDict[word]+=1
                else:
                    spamDict[word]=1

    saveFile(spamDict,'TrainSpamDict')  
    saveFile(hamDict,'TrainHamDict')  
    f='dictionary'
    dictionary=np.asarray(dictionary)
    np.save(f,dictionary)
    
    
if __name__=='__main__':
    wcount('all.txt')

