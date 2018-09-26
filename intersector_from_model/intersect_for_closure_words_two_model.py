#create model and convert it to text vector file..
import os
import csv
import sys
# dir=sys.argv[1].split()
# print(dir)
# abs_path=os.path.abspath(dir)+'/'
outfile=open('common_closure_words_between_models.txt','w')
cfl=[]

f1_name=sys.argv[1]
f2_name=sys.argv[2]
with open(f1_name) as f1, open(f2_name) as f2:
      w1=[x.strip().split() for x in f1.readlines()]
      w2=[x.strip().split() for x in f2.readlines()]
      for a,b in zip(w1,w2):
          if(a[0]==b[0]) and (len(a)>1 and len(b)>1):
              w1=set(a[1:])
              w2=set(b[1:])
              inter=w1.intersection(w2)
              print(a[0]+" "+" ".join(list(inter)))
              outfile.write('\nWord-'+a[0]+'\nModel_1-'+ str(a[0:])+'\nModel_2-'+ str(b[1:])+'\nIntersection-'+str(list(inter))+'\n\n')

