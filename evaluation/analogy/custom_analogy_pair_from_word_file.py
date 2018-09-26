from itertools import combinations
import os
import sys

inpath=(os.path.split(sys.argv[1]))[0]
filename=os.path.basename(sys.argv[1])
inputfile=open(sys.argv[1],'r')
outfile=open(os.path.join(inpath,filename)+'_eval.txt','w')
print(outfile)
wordlist=[x.strip() for x in inputfile.readlines()]
print(wordlist)
outfile.write(': no relation between pair of words'+'\n')
outline=combinations(wordlist,4)
count=0
for i in outline:
    print(i)
    words=' '.join(i)
    outfile.write(words+'\n')
    count+=1
    if count==50000:
        break




