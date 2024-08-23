import re
import rstr
import random
import fractions
from AWPPolygon import AWPPolygon
import math

def GenerateSize():
    frac_b=random.SystemRandom().randint(1,6)
    frac_a=random.SystemRandom().randint(1,4*frac_b)

    basesize=fractions.Fraction(frac_a,frac_b)
    return basesize

def GeneratePolygon(fixedsize=False, size=1):
    if fixedsize==False:
        frac_b=random.SystemRandom().randint(1,6)
        frac_a=random.SystemRandom().randint(1,4*frac_b)

        basesize=fractions.Fraction(frac_a,frac_b)
    else:
        basesize=size


    sides=random.SystemRandom().choices([3,4,5,6,7,8,9,10,11,12],weights=[0.3,0.3,0.05,0.05,0.05,0.05,0.05,0.95,0.05,0.05],k=1)[0]

    basepolygon=AWPPolygon(sides,basesize)

    return basepolygon

def GeneratePolygonLimited(fixedsize=bool, size=1):
    if fixedsize==False:
        frac_b=random.SystemRandom().randint(1,6)
        frac_a=random.SystemRandom().randint(1,4*frac_b)

        basesize=fractions.Fraction(frac_a,frac_b)
    else:
        basesize=size

    sides=random.SystemRandom().choice([3,4,5,6])

    basepolygon=AWPPolygon(sides,basesize)

    return basepolygon

def GeneratePolygonSuperLimited(fixedsize=bool, size=1):
    if fixedsize==False:
        frac_b=random.SystemRandom().randint(1,6)
        frac_a=random.SystemRandom().randint(1,4*frac_b)

        basesize=fractions.Fraction(frac_a,frac_b)
    else:
        basesize=size

    sides=random.SystemRandom().choice([3,4])

    basepolygon=AWPPolygon(sides,basesize)

    return basepolygon

def GenerateSizeArray():
    length=random.SystemRandom().randint(1,12)
    l=[]
    for i in range(length):
        l1=[]
        l1.append(GenerateSize())
        l1.append(random.SystemRandom().randint(1,6*math.ceil(l1[0])))
        l.append(l1)
    return l

def GenerateTriangularArray():
    length=random.SystemRandom().randint(1,24)
    return 't{'+str(length)+'}'

def GenerateSidePolygons(sides,size):
    ConnectedObjectsToSide=[]
    for i in range(sides):
        if sides<5:
            r=random.SystemRandom().choices(['No Polygon',GeneratePolygon(fixedsize=True, size=size),GenerateSizeArray(),GenerateTriangularArray()],weights=[fractions.Fraction(6,10),fractions.Fraction(4,30),fractions.Fraction(4,30),fractions.Fraction(4,30)],k=1)[0]
            ConnectedObjectsToSide.append(r)
        elif 5<=sides<7:
            r=random.SystemRandom().choices(['No Polygon',GeneratePolygonLimited(fixedsize=True, size=size),GenerateSizeArray(),GenerateTriangularArray()],weights=[fractions.Fraction(6,10),fractions.Fraction(4,30),fractions.Fraction(4,30),fractions.Fraction(4,30)],k=1)[0]
            ConnectedObjectsToSide.append(r)
        else:
            r=random.SystemRandom().choices(['No Polygon',GeneratePolygonSuperLimited(fixedsize=True, size=size),GenerateSizeArray(),GenerateTriangularArray()],weights=[fractions.Fraction(6,10),fractions.Fraction(4,30),fractions.Fraction(4,30),fractions.Fraction(4,30)],k=1)[0]
            ConnectedObjectsToSide.append(r)
    return ConnectedObjectsToSide

f=open('generatedawpshapes.txt','w', encoding='utf-8')        

for i in range(100):
    g1=GeneratePolygon()
    g=GenerateSidePolygons(g1.getSides(),g1.getSize())
    l=[str(g1),g]
    f.write(str(l))
    f.write('\n')
    for j in g:
        f.write(str(j))
        f.write('\n')

f.close()
