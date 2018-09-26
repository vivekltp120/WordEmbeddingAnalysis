from collections import Counter


inputfile=open('/home/vivek/ML_Sep_2017/DataCorpus/English/text8Dir/text8','r')
outfile=open('biagram_tokens.txt','w')
tokens=[]
s=inputfile.readline()

while s:
    tokens.append(s.split('.'))

biagram=[(tokens[i],tokens[i+1]) for i in range(len(tokens))]
count=Counter(biagram)
outfile.write(count)

