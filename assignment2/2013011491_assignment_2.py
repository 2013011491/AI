from konlpy.tag import Mecab
from konlpy.tag import Komoran
from konlpy.tag import Hannanum
from konlpy.tag import Kkma
from konlpy.tag import Twitter
import math
komoran=Komoran()
mecab = Mecab()
hannanum = Hannanum()
kkma = Kkma()
twitter = Twitter()
Pword= {}
Nword = {}
Pcount = 0
Ncount = 0

def train() :
	global Pword,Nword,Pcount,Ncount
	f=open("ratings_train.txt",'r')
#1st. all morphs and not duplicate
	data = f.readline() #first line deleting
	while 1  :
		data=f.readline()
		if not data : break
		temp=data[8:-3]
		morph = mecab.morphs(temp)
		morph = list(set(morph))
		print(data[-2])
		if data[-2] == '1' :
			Pcount = Pcount + 1	
			for ele in morph : 
				if ele in Pword :
					Pword[ele] = Pword[ele]+1
				else :
					Pword[ele] = 1
		else :
			Ncount = Ncount + 1
			for ele in morph :
				if ele in Nword :
					Nword[ele] = Nword[ele]+1
				else :
					Nword[ele] = 1
	f.close()
	f=open("trained.txt","w")
	for key, value in Nword.items() :
		f.write('%s:%s\n' %(key,value))
	f.write("Nword finish\n")
	for key, value in Pword.items() :
		f.write('%s:%s\n' %(key,value))
	f.write("Pword finish\n")
	f.write(str(Ncount))
	f.write("\n")
	f.write(str(Pcount))
	f.close()
#1.1st. all morphs and not duplicate
	'''data = f.readline() #first line deleting
	PPcount=0
	NNcount=0
	while 1  :
		data=f.readline()
		if not data : break
		temp=data[8:-3]
		morph = mecab.morphs(temp)
		morph = list(set(morph))
		print(data[-2])
		if data[-2] == '1' :
			Pcount = Pcount + 1	
			for ele in morph : 
				PPcount = PPcount+1
				if ele in Pword :
					Pword[ele] = Pword[ele]+1
				else :
					Pword[ele] = 1
		else :
			Ncount = Ncount + 1
			for ele in morph :
				NNcount = NNcount+1
				if ele in Nword :
					Nword[ele] = Nword[ele]+1
				else :
					Nword[ele] = 1
	f.close()
	f=open("trained11.txt","w")
	for key, value in Nword.items() :
		f.write('%s:%s\n' %(key,value))
	f.write("Nword finish\n")
	for key, value in Pword.items() :
		f.write('%s:%s\n' %(key,value))
	f.write("Pword finish\n")
	f.write(str(Ncount))
	f.write("\n")
	f.write(str(Pcount))
	f.write("\n")
	f.write(str(NNcount))
	f.write("\n")
	f.write(str(PPcount))
	f.close()'''
	# 2nd all morph and permit duplicate	
	'''data = f.readline() #first line deleting
	PPcount=0
	NNcount=0
	while 1  :
		data=f.readline()
		if not data : break
		temp=data[8:-3]
		morph = mecab.morphs(temp)
		print(data[-2])
		if data[-2] == '1' :
			Pcount = Pcount + 1	
			for ele in morph : 
				PPcount = PPcount+1
				if ele in Pword :
					Pword[ele] = Pword[ele]+1
				else :
					Pword[ele] = 1
		else :
			Ncount = Ncount + 1
			for ele in morph : 
				NNcount = NNcount+1
				if ele in Nword :
					Nword[ele] = Nword[ele]+1
				else :
					Nword[ele] = 1
	f.close()
	f=open("trained2.txt","w")
	for key, value in Nword.items() :
		f.write('%s:%s\n' %(key,value))
	f.write("Nword finish\n")
	for key, value in Pword.items() :
		f.write('%s:%s\n' %(key,value))
	f.write("Pword finish\n")
	f.write(str(Ncount))
	f.write("\n")
	f.write(str(Pcount))
	f.write("\n")
	f.write(str(NNcount))
	f.write("\n")
	f.write(str(PPcount))
	f.close()'''
	# 3rd traing noun and not duplicate
	'''data = f.readline() #first line deleting
	while 1  :
		data=f.readline()
		if not data : break
		temp=data[8:-3]
		morph = mecab.nouns(temp)
		morph = list(set(morph))
		print(data[-2])
		if data[-2] == '1' :
			Pcount = Pcount + 1	
			for ele in morph : 
				if ele in Pword :
					Pword[ele] = Pword[ele]+1
				else :
					Pword[ele] = 1
		else :
			Ncount = Ncount + 1
			for ele in morph :
				if ele in Nword :
					Nword[ele] = Nword[ele]+1
				else :
					Nword[ele] = 1
	f.close()
	f=open("trained3.txt","w")
	for key, value in Nword.items() :
		f.write('%s:%s\n' %(key,value))
	f.write("Nword finish\n")
	for key, value in Pword.items() :
		f.write('%s:%s\n' %(key,value))
	f.write("Pword finish\n")
	f.write(str(Ncount))
	f.write("\n")
	f.write(str(Pcount))
	f.close()'''
	# 4th traing noun and permit duplicate
	'''data = f.readline() #first line deleting
	while 1  :
		data=f.readline()
		if not data : break
		temp=data[8:-3]
		morph = mecab.nouns(temp)
		print(data[-2])
		if data[-2] == '1' :
			Pcount = Pcount + 1	
			for ele in morph : 
				if ele in Pword :
					Pword[ele] = Pword[ele]+1
				else :
					Pword[ele] = 1
		else :
			Ncount = Ncount + 1
			for ele in morph :
				if ele in Nword :
					Nword[ele] = Nword[ele]+1
				else :
					Nword[ele] = 1
	f.close()
	f=open("trained4.txt","w")
	for key, value in Nword.items() :
		f.write('%s:%s\n' %(key,value))
	f.write("Nword finish\n")
	for key, value in Pword.items() :
		f.write('%s:%s\n' %(key,value))
	f.write("Pword finish\n")
	f.write(str(Ncount))
	f.write("\n")
	f.write(str(Pcount))
	f.close()'''
#5nd. using Twitter all morphs and not duplicate
	'''data = f.readline() #first line deleting
	while 1  :
		data=f.readline()
		if not data : break
		temp=data[8:-3]
		morph = twitter.morphs(temp)
		morph = list(set(morph))
		print(data[-2])
		if data[-2] == '1' :
			Pcount = Pcount + 1	
			for ele in morph : 
				if ele in Pword :
					Pword[ele] = Pword[ele]+1
				else :
					Pword[ele] = 1
		else :
			Ncount = Ncount + 1
			for ele in morph :
				if ele in Nword :
					Nword[ele] = Nword[ele]+1
				else :
					Nword[ele] = 1
	f.close()
	f=open("trained5.txt","w")
	for key, value in Nword.items() :
		f.write('%s:%s\n' %(key,value))
	f.write("Nword finish\n")
	for key, value in Pword.items() :
		f.write('%s:%s\n' %(key,value))
	f.write("Pword finish\n")
	f.write(str(Ncount))
	f.write("\n")
	f.write(str(Pcount))
	f.close()'''
#6th. using Kkma all morphs and not duplicate
	'''data = f.readline() #first line deleting
	while 1  :
		data=f.readline()
		if not data : break
		temp=data[8:-3]
		morph = kkma.morphs(temp)
		morph = list(set(morph))
		print(data[-2])
		if data[-2] == '1' :
			Pcount = Pcount + 1	
			for ele in morph : 
				if ele in Pword :
					Pword[ele] = Pword[ele]+1
				else :
					Pword[ele] = 1
		else :
			Ncount = Ncount + 1
			for ele in morph :
				if ele in Nword :
					Nword[ele] = Nword[ele]+1
				else :
					Nword[ele] = 1
	f.close()
	f=open("trained6.txt","w")
	for key, value in Nword.items() :
		f.write('%s:%s\n' %(key,value))
	f.write("Nword finish\n")
	for key, value in Pword.items() :
		f.write('%s:%s\n' %(key,value))
	f.write("Pword finish\n")
	f.write(str(Ncount))
	f.write("\n")
	f.write(str(Pcount))
	f.close()'''


def main() :
    # train() #only for first training
	f = open("trained.txt","r")
	while 1 : 
		Nwordlist = f.readline()
		if Nwordlist == 'Nword finish\n' : break
		Nword[Nwordlist.split(':')[0]] = int(Nwordlist.split(':')[-1])
	while 1 : 
		Pwordlist = f.readline()
		if Pwordlist == 'Pword finish\n' : break
		Pword[Pwordlist.split(':')[0]] = int(Pwordlist.split(':')[-1])
	Ncount=int(f.readline())
	Pcount=int(f.readline())
	f.close()
	prN=Ncount/(Ncount+Pcount)
	prP=Pcount/(Ncount+Pcount)
	f=open("ratings_test.txt",'r')
	rf=open("ratings_result.txt",'w')
	data = f.readline() #first line deleting
	rf.write(data)
	comp=[]
	nPr=prN
	pPr=prP
	while 1 :
		data=f.readline()
		if not data : break
		temp=data[8:-3]
		morph = mecab.morphs(temp)
		morph = list(set(morph))
		for ele in morph : 
			if ele in Nword :
				nPr = nPr*(Nword[ele]/Ncount)
			if ele in Pword :
				pPr = pPr*(Pword[ele]/Pcount)
		if math.log(nPr)>math.log(pPr) :
			ndata = data[0:-2]+' 0\n'
			rf.write(ndata)
		else :
			ndata = data[0:-2]+' 1\n'
			rf.write(ndata)
		nPr=prN
		pPr=prP
	f.close()
	rf.close()
	 	 
if __name__ == "__main__" :
	main()
