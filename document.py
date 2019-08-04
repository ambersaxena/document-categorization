from sklearn.metrics import confusion_matrix
i=1
hn=0
h={}
while i<251:
    s="cs"
    s=s+`i`+"key.txt"
    l=open(s,'r')
    for j in l:
        word=j.split(" ")
        #print word[0],word[1]
        if word[0] not in h:
            h[word[0]]=hn
            hn=hn+1
        #else:
            #print "yes"
    i=i+1
    l.close()
i=1
while i<251:
    s="me"
    s=s+`i`+"key.txt"
    l=open(s,'r')
    for j in l:
        word=j.split(" ")
        #print word[0],word[1]
        if word[0] not in h:
            h[word[0]]=hn
            hn=hn+1
        #else:
            #print "noo"
    i=i+1
    l.close()
i=1
while i<251:
    s="bio"
    s=s+`i`+"key.txt"
    l=open(s,'r')
    for j in l:
        word=j.split(" ")
        #print word[0],word[1]
        if word[0] not in h:
            h[word[0]]=hn
            hn=hn+1
        #else:
            #print "noo"
    i=i+1
    l.close()
i=1
while i<251:
    s="ele"
    s=s+`i`+"key.txt"
    l=open(s,'r')
    for j in l:
        word=j.split(" ")
        #print word[0],word[1]
        if word[0] not in h:
            h[word[0]]=hn
            hn=hn+1
        #else:
            #print "noo"
    i=i+1
    l.close()
i=1
lf=[]
y=[]
while i<251:
    ls=[]
    j=0
    while j<len(h):
        ls.append(0)
        j=j+1
    s="cs"
    s=s+`i`+"key.txt"
    l=open(s,'r')
    for j in l:
        word=j.split(" ")
        ls[h[word[0]]]=int(word[1].replace("\n",""))
    lf.append(ls)
    y.append(1)
    i=i+1
i=1
while i<251:
    ls=[]
    j=0
    while j<len(h):
        ls.append(0)
        j=j+1
    s="me"
    s=s+`i`+"key.txt"
    l=open(s,'r')
    for j in l:
        word=j.split(" ")
        ls[h[word[0]]]=int(word[1].replace("\n",""))
    lf.append(ls)
    y.append(2)
    i=i+1
i=1
while i<251:
    ls=[]
    j=0
    while j<len(h):
        ls.append(0)
        j=j+1
    s="bio"
    s=s+`i`+"key.txt"
    l=open(s,'r')
    for j in l:
        word=j.split(" ")
        ls[h[word[0]]]=int(word[1].replace("\n",""))
    lf.append(ls)
    y.append(3)
    i=i+1
i=1
while i<251:
    ls=[]
    j=0
    while j<len(h):
        ls.append(0)
        j=j+1
    s="ele"
    s=s+`i`+"key.txt"
    l=open(s,'r')
    for j in l:
        word=j.split(" ")
        ls[h[word[0]]]=int(word[1].replace("\n",""))
    lf.append(ls)
    y.append(4)
    i=i+1
print len(lf[0])

x=lf
x_sparse = x
from sklearn.utils import shuffle
x, x_sparse, y = shuffle(x, x_sparse, y, random_state=0)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)
#print type(y_train[0])
p=open("tr1.csv","w")
yin=0
o=0
for i in X_train:
    for j in i:
        p.write(`j`+",")
    #p.write(y[yin])
    if(y_train[o]==1):
        p.write("1")
    else:
        p.write("0")
    o=o+1
    p.write("\n")
p.close()
p=open("tr2.csv","w")
yin=0
o=0
for i in X_train:
    for j in i:
        p.write(`j`+",")
    #p.write(y[yin])
    if(y_train[o]==2):
        p.write("1")
    else:
        p.write("0")
    o=o+1
    p.write("\n")
p.close()
p=open("tr3.csv","w")
yin=0
o=0
for i in X_train:
    for j in i:
        p.write(`j`+",")
    #p.write(y[yin])
    if(y_train[o]==3):
        p.write("1")
    else:
        p.write("0")
    o=o+1
    p.write("\n")
p.close()
p=open("tr4.csv","w")
yin=0
o=0
for i in X_train:
    for j in i:
        p.write(`j`+",")
    #p.write(y[yin])
    if(y_train[o]==4):
        p.write("1")
    else:
        p.write("0")
    o=o+1
    p.write("\n")
p.close()

x1=[]
y1=[]
p=open("tr1.csv","r")
for i in p:
    li=i.split(",")
    lii=li[:-1]
    liii=[]
    for j in lii:
        liii.append(int(j))
    x1.append(liii)
    y1.append(int(li[len(i.split(","))-1].replace('\n','')))
p.close()

x2=[]
y2=[]
p=open("tr2.csv","r")
for i in p:
    li=i.split(",")
    lii=li[:-1]
    liii=[]
    for j in lii:
        liii.append(int(j))
    x2.append(liii)
    y2.append(int(li[len(i.split(","))-1].replace('\n','')))
p.close()

x3=[]
y3=[]
p=open("tr3.csv","r")
for i in p:
    li=i.split(",")
    lii=li[:-1]
    liii=[]
    for j in lii:
        liii.append(int(j))
    x3.append(liii)
    y3.append(int(li[len(i.split(","))-1].replace('\n','')))
p.close()

x4=[]
y4=[]
p=open("tr4.csv","r")
for i in p:
    li=i.split(",")
    lii=li[:-1]
    liii=[]
    for j in lii:
        liii.append(int(j))
    x4.append(liii)
    y4.append(int(li[len(i.split(","))-1].replace('\n','')))
p.close()

from sklearn.svm import SVC 
clf1 = SVC(kernel='linear', random_state=1,probability=True) 
clf1.fit(x1, y1)

clf2 = SVC(kernel='linear', random_state=1,probability=True) 
clf2.fit(x2, y2)

clf3 = SVC(kernel='linear', random_state=1,probability=True) 
clf3.fit(x3, y3) 

clf4 = SVC(kernel='linear', random_state=1,probability=True) 
clf4.fit(x4, y4) 

y1_test=clf1.predict(X_test)
y1_test_pre=clf1.predict_proba(X_test)
y2_test= clf2.predict(X_test) 
y2_test_pre=clf2.predict_proba(X_test)
y3_test=clf3.predict(X_test) 
y3_test_pre=clf3.predict_proba(X_test)
y4_test=clf4.predict(X_test) 
y4_test_pre=clf4.predict_proba(X_test)
print y1_test
print y2_test
print y3_test

i=0
co=1
y_pr=[]
s=len(y1_test)
while(i<s):
    max=0
    f=0
    if y1_test[i]==1:
        max=1
    if y2_test[i]==1:
        if max==1:
            f=1
        max=2
    if y3_test[i]==1:
        if max==1:
            f=1
        max=3
    if y4_test[i]==1:
        if max==1:
            f=1
        max=4
    if f==0 and max!=0:
        y_pr.append(max)
    else:
        #a=[y1_test_pre[i][1],y2_test_pre[i][1],y3_test_pre[i][1]]
        #print i,a
        #max=a.index(max(a))
        print y1_test_pre[i],y2_test_pre[i],y3_test_pre[i]
        if y1_test_pre[i][1]>=y2_test_pre[i][1] and y1_test_pre[i][1]>=y3_test_pre[i][1] and y1_test_pre[i][1]>=y4_test_pre[i][1]:
            max=1
        if y2_test_pre[i][1]>=y1_test_pre[i][1] and y2_test_pre[i][1]>=y3_test_pre[i][1] and y2_test_pre[i][1]>=y4_test_pre[i][1]:
            max=2
        if y3_test_pre[i][1]>=y1_test_pre[i][1] and y3_test_pre[i][1]>=y2_test_pre[i][1] and y3_test_pre[i][1]>=y4_test_pre[i][1]:
            max=3
        if y4_test_pre[i][1]>=y1_test_pre[i][1] and y4_test_pre[i][1]>=y2_test_pre[i][1] and y4_test_pre[i][1]>=y3_test_pre[i][1]:
            max=4
        #print max
        y_pr.append(max)
        co=co+1
    i=i+1
print y_pr,co
print confusion_matrix(y_test, y_pr)

"""#print x
#y=[-1,-1,-1,-1,-1,1,1,1,1,1]
from sklearn.svm import SVC 
#print "done",x[0]
clf = SVC(kernel='linear', random_state=1) 
clf.fit(X_train, y_train) 
y_pred=clf.predict(X_test) 
print confusion_matrix(y_test, y_pred)
#print y_pred"""
"""i=98
lf1=[]
while i<99:
    ls=[]
    j=0
    while j<len(h):
        ls.append(0)
        j=j+1
    s="cs"
    s=s+`i`+"key.txt"
    l=open(s,'r')
    for j in l:
        word=j.split(" ")
        try:
            ls[h[word[0]]]=int(word[1].replace("\n",""))
        except:
            c=1
    lf1.append(ls)
    y.append(1)
    i=i+1
x_1=lf1"""
#print clf.predict(x_1) 