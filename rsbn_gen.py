import random
s=random.SystemRandom()
f=open('rsbn.txt','w')
def GenerateJointing():
    return s.choice(['(tw)','(st)','(di[l])','(di[r])','(mi)','(su)','(vu)','(oc)','(na)','(ps)','(dr)','(v)'])
def GenerateRSBN(max=12):
    l=[]
    l.append(s.randint(1,max))
    l.append(GenerateJointing())
    return l
def GenerateProperRSBN(layeramount=1):
    l=[]
    if layeramount>2:
        for i in range(0,s.randint(3,12)):
            l.append(GenerateProperRSBN(layeramount-1))
        l.append(GenerateJointing())
        return l
    elif layeramount==2:
        for i in range(0,s.randint(3,12)):
            l.append(GenerateRSBN(36))
        l.append(GenerateJointing())
        return l
    elif layeramount==1:
        return GenerateRSBN(36)
for j in range(0,100):
    f.write(str((GenerateProperRSBN(random.choices([1,2,3,4],[1/6,1,1/120,1/5040],k=1)[0]))))
    f.write('\n')
f.close()