from googletrans import Translator
import sys
translator=Translator()


inputfile=open(sys.argv[1],'r')
outfile=open(sys.argv[2],'w')
des=sys.argv[3]

for line in inputfile.readlines():
 wordL=line.split(' ')
 print(wordL)
 if wordL[0]==':':
     outfile.write(line)
     continue
 else:
     translated = translator.translate(line, dest=des)
     outfile.write(translated.text+'\n')
     print (translated.text)