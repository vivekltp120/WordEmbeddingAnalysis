#create model and convert it to text vector file..
import os
import csv
import sys
import datetime
dir=os.getcwd()#sys.argv[1]
abs_path=os.path.abspath(dir)+'/'
cfl=[]
print("abs path" + abs_path)
current_time=datetime.datetime.now().strftime('%d_%b_%y')
f1_path=sys.argv[1]
f2_path=sys.argv[2]
f3_path=sys.argv[3]
f4_path=sys.argv[4]
if f1_path:
    f1_name=os.path.basename(f1_path)  #f1_path.split("/")[-1].split('.')[0]
if f2_path:
    f2_name=os.path.basename(f2_path)
if f3_path:
    f3_name=os.path.basename(f3_path)
if f4_path:
    f4_name=os.path.basename(f4_path)

# outfile=open("_".join(f1_name.split('_')[0:2]+f2_name.split('_')[0:2])+'_common_closure_words.txt','w')
outfile=open('common_closure_words_'+current_time+'.txt','w')

# writeCSV = csv.writer(outfile, delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
# fieldnames = ['Word',f1_name,f2_name,f3_name,f4_name,'Intersection']
outfile.write('WEM_1 - '+'_'.join(f1_name.split("_")[0:10])+'\n')
outfile.write('WEM_2 - '+'_'.join(f2_name.split("_")[0:10])+'\n')
outfile.write('WEM_3 - '+'_'.join(f3_name.split("_")[0:10])+'\n')
outfile.write('WEM_4 - '+'_'.join(f4_name.split("_")[0:10])+'\n')

with open(f1_path) as f1, open(f2_path) as f2,open(f3_path) as f3,open(f4_path) as f4:
      w1=[x.strip().split() for x in f1.readlines()]
      w2=[x.strip().split() for x in f2.readlines()]
      w3=[x.strip().split() for x in f3.readlines()]
      w4=[x.strip().split() for x in f4.readlines()]
      for a,b,c,d in zip(w1,w2,w3,w4):
          if(a[0]==b[0]==c[0]==d[0]):
              w1=set(a[1:])
              w2=set(b[1:])
              w3=set(c[1:])
              w4=set(d[1:])
              inter=w1.intersection(w2).intersection(w3).intersection(w4)
              union=w1.union(w2).union(w3).union(w4)
              # writeCSV.writerow([a[0],a[1:],b[1:],c[1:],d[1:],inter])
              # outfile.write('\nWord-'+a[0]+'\n'+str(f1_name)+str(a[0:])+'\n'+str(f2_name)+ str(b[1:])+'\n'+str(f3_name)+ str(c[1:])+'\n'+str(f4_name)+ str(d[1:])+'\nIntersection-'+str(list(inter))+'\n\n')
              outfile.write('\nWord-'+a[0]+'\nWEM_1 - '+str(a[0:])+'\nWEM_2 - '+ str(b[1:])+'\nWEM_3 - '+ str(c[1:])+'\nWEM_4 - '+ str(d[1:])+'\nIntersection-'+str(list(inter))+'\n\n')
              # print(a[0]+" "+" ".join(list(inter)))

