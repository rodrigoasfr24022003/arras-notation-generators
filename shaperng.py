import random
s=random.SystemRandom()
xcmax=10
ycmax=10
pointsmax=10
def Generate2DPoint(FixedX=None, FixedY=None, xmax=xcmax, ymax=ycmax, xmin=-xcmax, ymin=-ycmax, diag=0, knight=0, fill=0, doublefill=0, quadfill=0):
    t=()
    if FixedX!=None and FixedY!=None:
        t=(FixedX,FixedY)
    elif FixedX!=None and FixedY==None:
        t=(FixedX,s.randint(ymin,ymax))
    elif FixedX==None and FixedY!=None:
        t=(s.randint(xmin,xmax),FixedY)
    elif fill==1:
        if diag==1:
            posx=s.randint(xmin,xmax)
            t=(s.randint(xmin,posx),s.randint(posx,ymax))
        elif diag==-1:
            posx=s.randint(xmin,xmax)
            t=(s.randint(xmin,posx),s.randint(ymin,-posx))
        elif knight==1:
            posx=s.randint(2*xmin,2*xmax)
            t=(s.randint(2*xmin,2*posx),s.randint(posx,ymax))
        elif knight==-1:
            posx=s.randint(2*xmin,2*xmax)
            t=(s.randint(2*xmin,2*posx),s.randint(ymin,posx))
        elif knight==2:
            posx=s.randint(2*xmin,2*xmax)
            t=(s.randint(2*xmin,posx),s.randint(2*posx,2*ymax))
        elif knight==-2:
            posx=s.randint(2*xmin,2*xmax)
            t=(s.randint(2*xmin,posx),s.randint(2*ymin,-2*posx))
    elif fill==-1:
        if diag==1:
            posx=s.randint(xmin,xmax)
            t=(s.randint(posx,xmax),s.randint(ymin,posx))
        elif diag==-1:
            posx=s.randint(xmin,xmax)
            t=(s.randint(posx,xmax),s.randint(posx,-ymax))
        elif knight==1:
            posx=s.randint(2*xmin,2*xmax)
            t=(s.randint(2*posx,2*xmax),s.randint(ymin,posx))
        elif knight==-1:
            posx=s.randint(2*xmin,2*xmax)
            t=(s.randint(2*posx,2*xmax),s.randint(posx,ymax))
        elif knight==2:
            posx=s.randint(2*xmin,2*xmax)
            t=(s.randint(posx,xmax),s.randint(2*ymin,2*posx))
        elif knight==-2:
            posx=s.randint(2*xmin,2*xmax)
            t=(s.randint(posx,xmax),s.randint(-2*posx,-2*ymax))
    elif doublefill==1 and diag!=0:
            posx=s.randint(-xmax,xmax)
            if posx<0:
                t=(s.randint(posx,0),s.randint(-posx,ymax))
            else:
                t=(s.randint(0,posx),s.randint(posx,ymax))
    # elif doublefill==2 and diag!=0:
    #         posx=s.randint(xmin,xmax)
    #         t=(s.randint(0,xmax),s.randint(-posx,posx))
    # elif doublefill==3 and diag!=0:
    #         posx=s.randint(xmin,xmax)
    #         t=(s.randint(-posx,posx),s.randint(ymin,0))
    # elif doublefill==4 and diag!=0:
    #         posx=s.randint(xmin,xmax)
    #         t=(s.randint(xmin,0),s.randint(-posx,posx))
    elif quadfill==1 and diag!=0:
            posx=s.randint(0,xmax)
            t=(s.randint(0,posx),s.randint(0,posx))
    # elif quadfill==2 and diag!=0:
    #         posx=s.randint(xmin,xmax)
    #         t=(s.randint(0,posx),s.randint(-posx,0))
    elif fill==0 and (diag!=0 or knight !=0):
        if diag==1:
            posx=s.randint(xmin,xmax)
            t=(posx,posx)
        elif diag==-1:
            posx=s.randint(xmin,xmax)
            t=(posx,-posx)
        elif knight==1:
            posx=s.randint(2*xmin,2*xmax)
            t=(2*posx,posx)
        elif knight==-1:
            posx=s.randint(2*xmin,2*xmax)
            t=(2*posx,-posx)
        elif knight==2:
            posx=s.randint(2*xmin,2*xmax)
            t=(posx,2*posx)
        elif knight==-2:
            posx=s.randint(2*xmin,2*xmax)
            t=(posx,-2*posx)
    else:
        t=(s.randint(xmin,xmax),s.randint(ymin,ymax))
    return t
f=open('polygon3.txt','w')
for i in range(1024):
    shape=[]
    sym=s.choices(['none','2wayx','2wayy','double2way','diag','antidiag','doublediag','octangular'],weights=[1,4,4,4,3,3,3,3],k=1)[0]
    shape.append(sym)
    points=s.randint(4,pointsmax)
    if sym=='none':
        sp=[]
        for i in range(points):
            sp.append(Generate2DPoint(None,None,xcmax,ycmax,-xcmax,-ycmax))
        shape.append(sp)
        sl=[]
        for j in range(points):
            sl.append(s.choices(['rect','line','arc','sarc'],weights=[0.2,0.3,0.3,0.2],k=1)[0])
        shape.append(sl)
    if sym=='2wayy':
        sp=[]
        fixedn=s.randint(2,max(2,int(points/2)))
        for i1 in range(fixedn):
            sp.append(Generate2DPoint(0,None,0,ycmax,0,-ycmax))
        for i in range(points-fixedn):
            sp.append(Generate2DPoint(None,None,xcmax,ycmax,0,-ycmax))
        shape.append(sp)
        sl=[]
        for j in range(points):
            sl.append(s.choices(['rect','line','arc','sarc'],weights=[0.2,0.3,0.3,0.2],k=1)[0])
        shape.append(sl)
    if sym=='2wayx':
        sp=[]
        fixedn=s.randint(2,max(2,int(points/2)))
        for i1 in range(fixedn):
            sp.append(Generate2DPoint(None,0,xcmax,0,-ycmax,0))
        for i in range(points-fixedn):
            sp.append(Generate2DPoint(None,None,xcmax,ycmax,-xcmax,0))
        shape.append(sp)
        sl=[]
        for j in range(points):
            sl.append(s.choices(['rect','line','arc','sarc'],weights=[0.2,0.3,0.3,0.2],k=1)[0])
        shape.append(sl)
    if sym=='double2way':
        sp=[]
        fixednx=s.randint(1,max(2,int(points/3)))
        fixedny=s.randint(1,max(2,int(points/3)))
        sp.append((0,0))
        for i1 in range(fixednx-1):
            sp.append(Generate2DPoint(0,None,0,ycmax,0,-ycmax))
        for i1 in range(fixedny-1):
            sp.append(Generate2DPoint(None,0,xcmax,0,-xcmax,0))
        for i in range(points-fixednx-fixedny+1):
            sp.append(Generate2DPoint(None,None,xcmax,ycmax,0,0))
        shape.append(sp)
        sl=[]
        for j in range(points):
            sl.append(s.choices(['rect','line','arc','sarc'],weights=[0.2,0.3,0.3,0.2],k=1)[0])
        shape.append(sl)
    if sym=='diag':
        sp=[]
        fixedn=s.randint(2,max(2,int(points/2)))
        for i1 in range(fixedn):
            sp.append(Generate2DPoint(None,None,xcmax,ycmax,-xcmax,-ycmax,diag=1))
        for i in range(points-fixedn):
            sp.append(Generate2DPoint(None,None,xcmax,ycmax,-xcmax,-ycmax, diag=1, fill=1))
        shape.append(sp)
        sl=[]
        for j in range(points):
            sl.append(s.choices(['rect','line','arc','sarc'],weights=[0.2,0.3,0.3,0.2],k=1)[0])
        shape.append(sl)
    if sym=='antidiag':
        sp=[]
        fixedn=s.randint(2,max(2,int(points/2)))
        for i1 in range(fixedn):
            sp.append(Generate2DPoint(None,None,xcmax,ycmax,-xcmax,-ycmax,diag=-1))
        for i in range(points-fixedn):
            sp.append(Generate2DPoint(None,None,xcmax,ycmax,-xcmax,-ycmax, diag=-1, fill=1))
        shape.append(sp)
        sl=[]
        for j in range(points):
            sl.append(s.choices(['rect','line','arc','sarc'],weights=[0.2,0.3,0.3,0.2],k=1)[0])
        shape.append(sl)
    if sym=='doublediag':
        sp=[]
        fixednx=s.randint(1,max(2,int(points/3)))
        fixedny=s.randint(1,max(2,int(points/3)))
        sp.append((0,0))
        for i1 in range(fixednx-1):
            sp.append(Generate2DPoint(None,None,xcmax,ycmax,-xcmax,-ycmax, diag=1))
        for i1 in range(fixedny-1):
            sp.append(Generate2DPoint(None,None,xcmax,ycmax,-xcmax,-ycmax, diag=-1))
        for i in range(points-fixednx-fixedny+1):
            sp.append(Generate2DPoint(None,None,xcmax,ycmax,-xcmax,-ycmax,doublefill=1, diag=1))
        shape.append(sp)
        sl=[]
        for j in range(points):
            sl.append(s.choices(['rect','line','arc','sarc'],weights=[0.2,0.3,0.3,0.2],k=1)[0])
        shape.append(sl)
    if sym=='octangular':
        sp=[]
        fixednx=s.randint(1,max(2,int(points/3)))
        fixedny=s.randint(1,max(2,int(points/3)))
        sp.append((0,0))
        for i1 in range(fixednx-1):
            sp.append(Generate2DPoint(0,None,0,ycmax,0,0, diag=1))
        for i1 in range(fixedny-1):
            sp.append(Generate2DPoint(None,0,xcmax,0,0,0))
        for i in range(points-fixednx-fixedny+1):
            sp.append(Generate2DPoint(None,None,xcmax,ycmax,0,0, quadfill=1))
        shape.append(sp)
        sl=[]
        for j in range(points):
            sl.append(s.choices(['rect','line','arc','sarc'],weights=[0.2,0.3,0.3,0.2],k=1)[0])
        shape.append(sl)
    f.write(str(shape))
    f.write('\n')
f.close()