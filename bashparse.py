

f1=open(".bash_history","r")
com=f1.readlines()
com1=[]
#parsing history file and taking only commands and appending to the list com1 
for i in range(0,len(com)):
	k=com[i].split()
	if(len(k) > 1):
		com1.append(k[0])
rc=[]
count=[]
#deleting all the duplicate items
for j in range(0,len(com1)):
	k=com1[j]
	for i in com1:
		if k not in rc:
			rc.append(k)
#counting the number of occurence of comammand
for i in rc:
	count1=0
	for k in com1:
		if k==i:
			count1=count1+1
	count.append(count1)

f2=open("bar-data.csv","w")
f2.write("command,value\n")
if len(rc)==len(count):
	for i in range(0,len(rc)):
		
		f2.write(rc[i])
		f2.write(",")
		f2.write(str(count[i]))
		f2.write("\n")  

