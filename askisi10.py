import random
import string

w=100
Matrix=[[random.choice(string.ascii_lowercase) for i in range(w)] for j in range(w)]
	
leksiko=raw_input("Dose arxeio: ") #px. myfile.txt
words=open(leksiko,"r")

result=[]
#elegxos orizontia
for line in words:
	l=list(line)
	if "\n" in l:
		l.remove("\n")
	word=''.join(l)
	#elegxos orizontia
	for i in range(w):
		if word in ''.join(Matrix[i]):
			result.append(word)
			break
	
	#an exei vrei ti leksi orizontia, min psaksi kai katheta
	if word in result:
		continue
			
	#elegxos katheta
	for j in range(w):
		str1=""
		for i in range(w):
			str1=str1+Matrix[i][j]
		if word in str1:
			result.append(word)
			break	

print result
			
			
				
