import numpy as np
from matplotlib.path import Path
import matplotlib.patches as patches

def deg_rad_calc(deg_rad,angle):
    return angle*180/np.pi if deg_rad else angle*np.pi/180

def triangle_calc(triangle, deg_rad):
    statusCodes = {'ok':0,'twoSol':1, 'errImpos':2, 'errMiss':3, 'errLim':4}
    status = statusCodes['ok']
    
    A = triangle.get('A',None)
    B = triangle.get('B',None)
    C = triangle.get('C',None)
    a = triangle.get('a',None)
    b = triangle.get('b',None)
    c = triangle.get('c',None)

    triangle = {k: v for k, v in triangle.items() if v}
    if len(triangle)!=3:
        status = statusCodes['errMiss']
    
    if deg_rad:
        A = A*np.pi/180. if A else A
        B = B*np.pi/180. if B else B
        C = C*np.pi/180. if C else C

    
    if A or A==0:
        if A>=np.pi or A<=0:
            status = statusCodes['errLim']
    if B or B==0:
        if B>=np.pi or B<=0:
            status = statusCodes['errLim']
    if C or C==0:
        if C>=np.pi or C<=0:
            status = statusCodes['errLim']
    if a or a==0:
        if a<=0:
            status = statusCodes['errLim']
    if b or b==0:
        if b<=0:
            status = statusCodes['errLim']
    if c or c==0:
        if c<=0:
            status = statusCodes['errLim']

    if status == statusCodes['ok']:
        if A and B:
            if A+B<np.pi:
                C = np.pi-A-B
                if a:
                    b = a*np.sin(B)/np.sin(A)
                    c = a*np.sin(C)/np.sin(A)
                elif b:
                    a = b*np.sin(A)/np.sin(B)
                    c = b*np.sin(C)/np.sin(B)
                elif c:
                    b = c*np.sin(B)/np.sin(C)
                    a = c*np.sin(A)/np.sin(C)
            else:
                status = statusCodes['errImpos']
        elif A and C:
            if A+C<np.pi:
                B = np.pi-A-C
                if a:
                    b = a*np.sin(B)/np.sin(A)
                    c = a*np.sin(C)/np.sin(A)
                elif b:
                    a = b*np.sin(A)/np.sin(B)
                    c = b*np.sin(C)/np.sin(B)
                elif c:
                    b = c*np.sin(B)/np.sin(C)
                    a = c*np.sin(A)/np.sin(C)
            else:
                status = statusCodes['errImpos']
        elif B and C:
            if B+C<np.pi:
                A = np.pi-B-C
                if a:
                    b = a*np.sin(B)/np.sin(A)
                    c = a*np.sin(C)/np.sin(A)
                elif b:
                    a = b*np.sin(A)/np.sin(B)
                    c = b*np.sin(C)/np.sin(B)
                elif c:
                    b = c*np.sin(B)/np.sin(C)
                    a = c*np.sin(A)/np.sin(C)
            else:
                status = statusCodes['errImpos']
        elif A and a and b:
            if a>=b or a == b*np.sin(A):
                c = b*np.cos(A)+np.sqrt(a**2-b**2*np.sin(A)**2)
                B = np.arccos((b**2-a**2-c**2)/(-2*a*c))
                C = np.arccos((c**2-a**2-b**2)/(-2*a*b))
            elif b*np.sin(A)<a and A<=np.pi/2:
                c = []
                B = []
                C = []
                c.append(b*np.cos(A)-np.sqrt(a**2-b**2*np.sin(A)**2))
                c.append(b*np.cos(A)+np.sqrt(a**2-b**2*np.sin(A)**2))
                for cc in c:
                    B.append(np.arccos((b**2-a**2-cc**2)/(-2*a*cc)))
                    C.append(np.arccos((cc**2-a**2-b**2)/(-2*a*b)))
                A = [A,A]
                a = [a,a]
                b = [b,b]
                status = statusCodes['twoSol']
            else:
                status = statusCodes['errImpos']
        elif A and a and c:
            if a>=c or a == c*np.sin(A):
                b = c*np.cos(A)+np.sqrt(a**2-c**2*np.sin(A)**2)
                B = np.arccos((b**2-a**2-c**2)/(-2*a*c))
                C = np.arccos((c**2-a**2-b**2)/(-2*a*b))
            elif c*np.sin(A)<a and A<=np.pi/2:
                b = []
                B = []
                C = []
                b.append(c*np.cos(A)-np.sqrt(a**2-c**2*np.sin(A)**2))
                b.append(c*np.cos(A)+np.sqrt(a**2-c**2*np.sin(A)**2))
                for bb in b:
                    B.append(np.arccos((bb**2-a**2-c**2)/(-2*a*c)))
                    C.append(np.arccos((c**2-a**2-bb**2)/(-2*a*bb)))
                A = [A,A]
                a = [a,a]
                c = [c,c]
                status = statusCodes['twoSol']
            else:
                status = statusCodes['errImpos']
        elif B and a and b:
            if b>=a or b == a*np.sin(B):
                c = a*np.cos(B)+np.sqrt(b**2-a**2*np.sin(B)**2)
                A = np.arccos((a**2-b**2-c**2)/(-2*b*c))
                C = np.arccos((c**2-a**2-b**2)/(-2*a*b))
            elif a*np.sin(B)<b and B<=np.pi/2:
                c = []
                A = []
                C = []
                c.append(a*np.cos(B)-np.sqrt(b**2-a**2*np.sin(B)**2))
                c.append(a*np.cos(B)+np.sqrt(b**2-a**2*np.sin(B)**2))
                for cc in c:
                    A.append(np.arccos((a**2-b**2-cc**2)/(-2*b*cc)))
                    C.append(np.arccos((cc**2-a**2-b**2)/(-2*a*b)))
                B = [B,B]
                a = [a,a]
                b = [b,b]
                status = statusCodes['twoSol']
            else:
                status = statusCodes['errImpos']
        elif B and b and c:
            if b>=c or b == c*np.sin(B):
                a = c*np.cos(B)+np.sqrt(b**2-c**2*np.sin(B)**2)
                A = np.arccos((a**2-b**2-c**2)/(-2*b*c))
                C = np.arccos((c**2-a**2-b**2)/(-2*a*b))
            elif c*np.sin(B)<b and B<=np.pi/2:
                a = []
                A = []
                C = []
                a.append(c*np.cos(B)-np.sqrt(b**2-c**2*np.sin(B)**2))
                a.append(c*np.cos(B)+np.sqrt(b**2-c**2*np.sin(B)**2))
                for aa in a:
                    A.append(np.arccos((aa**2-b**2-c**2)/(-2*b*c)))
                    C.append(np.arccos((c**2-aa**2-b**2)/(-2*aa*b)))
                B = [B,B]
                b = [b,b]
                c = [c,c]
                status = statusCodes['twoSol']
            else:
                status = statusCodes['errImpos']
        elif C and a and c:
            if c>=a or c == a*np.sin(C):
                b = a*np.cos(C)+np.sqrt(c**2-a**2*np.sin(C)**2)
                A = np.arccos((a**2-b**2-c**2)/(-2*b*c))
                B = np.arccos((b**2-a**2-c**2)/(-2*a*c))
            elif a*np.sin(C)<c and C<=np.pi/2:
                b = []
                A = []
                B = []
                b.append(a*np.cos(C)-np.sqrt(c**2-a**2*np.sin(C)**2))
                b.append(a*np.cos(C)+np.sqrt(c**2-a**2*np.sin(C)**2))
                for bb in b:
                    A.append(np.arccos((a**2-bb**2-c**2)/(-2*bb*c)))
                    B.append(np.arccos((bb**2-a**2-c**2)/(-2*a*c)))
                C = [C,C]
                a = [a,a]
                c = [c,c]
                status = statusCodes['twoSol']
            else:
                status = statusCodes['errImpos']
        elif C and b and c:
            if c>=b or c == b*np.sin(C):
                a = b*np.cos(C)+np.sqrt(c**2-b**2*np.sin(C)**2)
                A = np.arccos((a**2-b**2-c**2)/(-2*b*c))
                B = np.arccos((b**2-a**2-c**2)/(-2*a*c))
            elif b*np.sin(C)<c and C<=np.pi/2:
                a = []
                A = []
                B = []
                a.append(b*np.cos(C)-np.sqrt(c**2-b**2*np.sin(C)**2))
                a.append(b*np.cos(C)+np.sqrt(c**2-b**2*np.sin(C)**2))
                for aa in a:
                    A.append(np.arccos((aa**2-b**2-c**2)/(-2*b*c)))
                    B.append(np.arccos((b**2-aa**2-c**2)/(-2*aa*c)))
                C = [C,C]
                b = [b,b]
                c = [c,c]
                status = statusCodes['twoSol']
            else:
                status = statusCodes['errImpos']
        elif A and b and c:
            a = np.sqrt(b**2+c**2-2*b*c*np.cos(A))
            B = np.arccos((b**2-a**2-c**2)/(-2*a*c))
            C = np.arccos((c**2-a**2-b**2)/(-2*a*b))
        elif B and a and c:
            b = np.sqrt(a**2+c**2-2*a*c*np.cos(B))
            A = np.arccos((a**2-b**2-c**2)/(-2*b*c))
            C = np.arccos((c**2-a**2-b**2)/(-2*a*b))
        elif C and a and b:
            c = np.sqrt(a**2+b**2-2*a*b*np.cos(C))
            A = np.arccos((a**2-b**2-c**2)/(-2*b*c))
            B = np.arccos((b**2-a**2-c**2)/(-2*a*c))
        elif a and b and c:
            if a<b+c and b<a+c and c<a+b:
                A = np.arccos((a**2-b**2-c**2)/(-2*b*c))
                B = np.arccos((b**2-a**2-c**2)/(-2*a*c))
                C = np.arccos((c**2-a**2-b**2)/(-2*a*b))
            else:
                status = statusCodes['errImpos']
    
    if status == statusCodes['twoSol']:
        t = []
        for n in range(2):
            t.append({})
            if deg_rad:
                A[n] = A[n]*180./np.pi if A[n] else A[n]
                B[n] = B[n]*180./np.pi if B[n] else B[n]
                C[n] = C[n]*180./np.pi if C[n] else C[n]
            t[n]['A'] = triangle.get('A',A[n])
            t[n]['B'] = triangle.get('B',B[n])
            t[n]['C'] = triangle.get('C',C[n])
            t[n]['a'] = triangle.get('a',a[n])
            t[n]['b'] = triangle.get('b',b[n])
            t[n]['c'] = triangle.get('c',c[n])

        triangle = t
        
    else:
        if deg_rad:
            A = A*180./np.pi if A else A
            B = B*180./np.pi if B else B
            C = C*180./np.pi if C else C
            
        triangle['A'] = triangle.pop('A',A)
        triangle['B'] = triangle.pop('B',B)
        triangle['C'] = triangle.pop('C',C)
        triangle['a'] = triangle.pop('a',a)
        triangle['b'] = triangle.pop('b',b)
        triangle['c'] = triangle.pop('c',c)
    
    return status, triangle

def draw_triangle(fig, triangle, deg_rad):
    fig.clf()
    axes = fig.add_subplot(111)
    
    text_list = info_box(triangle)
        
    A = triangle.get('A',None)
    B = triangle.get('B',None)
    C = triangle.get('C',None)
    a = triangle.get('a',None)
    b = triangle.get('b',None)
    c = triangle.get('c',None)

    if not (None in [A,B,C,a,b,c,deg_rad]):
        
        if deg_rad:
            A = A*np.pi/180. if A else A
            B = B*np.pi/180. if B else B
            C = C*np.pi/180. if C else C

        # setup path
        verts = []
        verts.append((0., 0.))
        verts.append((c*np.cos(A), c*np.sin(A)))
        verts.append((b, 0.))
        verts.append((0., 0.))
        # scale path to 1 + off set
        verts = np.array(verts)
        verts[:,0] = verts[:,0] - np.min(verts[:,0])
        verts[:,1] = verts[:,1] - np.min(verts[:,1])
        scale = np.max([np.max(verts[:,0])-np.min(verts[:,0]),np.max(verts[:,1])-np.min(verts[:,1])])
        verts = verts/scale
        verts[:,0] = verts[:,0]+(1-np.max(verts[:,0]))/2
        verts[:,1] = verts[:,1]+(1-np.max(verts[:,1]))/2
        # describe path
        codes = [Path.MOVETO,
                 Path.LINETO,
                 Path.LINETO,
                 Path.CLOSEPOLY,
                 ]
        # build path
        path = Path(verts, codes)

        patch = patches.PathPatch(path, facecolor='orange', lw=2)
        axes.add_patch(patch)

        fontsize = 'large'
        fontshift = 0.05
        keys = ['A','B','C','a','b','c']
        pos = [[verts[0,0]-fontshift,verts[0,1]-fontshift],
               [verts[1,0],verts[1,1]+fontshift],
               [verts[2,0]+fontshift,verts[2,1]-fontshift],
               [verts[1,0]-(verts[1,0]-verts[2,0])/2+fontshift,verts[1,1]-(verts[1,1]-verts[2,1])/2],
               [verts[0,0]-(verts[0,0]-verts[2,0])/2,verts[0,1]-(verts[0,1]-verts[2,1])/2-fontshift],
               [verts[0,0]-(verts[0,0]-verts[1,0])/2-fontshift,verts[0,1]-(verts[0,1]-verts[1,1])/2]]

        for n in range(len(keys)):
            t = keys[n]
            p = pos[n]
            text_list.append(MplText(p,t, fontsize = fontsize))

        
    for text in text_list:
        text.print(axes)
        
    axes.set_xlim(-0.2,1.2)
    axes.set_ylim(-0.2,1.2)
    axes.axis('off')

def path_list_calc(triangle, deg_rad):
    list_of_args = []
    N = 100
    fontsize = 'large'
    fontshift = 0.05
    fontshifts = {'A':[-fontshift,-fontshift],
                  'B':[0,fontshift],
                  'C':[fontshift,-fontshift],
                  'a':[fontshift,0],
                  'b':[0,-fontshift],
                  'c':[-fontshift,0]}
    
    A = triangle.get('A',None)
    B = triangle.get('B',None)
    C = triangle.get('C',None)
    a = triangle.get('a',None)
    b = triangle.get('b',None)
    c = triangle.get('c',None)

    values = {v for v in triangle.values() if v}
    if len(values)==3:
        if deg_rad:
            A = A*np.pi/180. if A else A
            B = B*np.pi/180. if B else B
            C = C*np.pi/180. if C else C

        if A and a and b:
            NN = N/2
            c = np.hstack([
                np.arange(0,a+b+(a+b)/NN,(a+b)/NN),
                np.arange(a+b,0,-(a+b)/NN)])
            NN = NN/2
            C = np.hstack([
                np.arange(0,np.pi+np.pi/NN,np.pi/NN),
                np.arange(np.pi,0,-np.pi/NN),
                np.arange(0,np.pi+np.pi/NN,np.pi/NN),
                np.arange(np.pi,0,-np.pi/NN)])
            
            P1, P2, P3, P4 = [], [], [], []
            text_keys = ['A','C','a','b','c']
            test_pos = []
            for n in range(N):
                P1.append([c[n]*np.cos(A), c[n]*np.sin(A)])
                P2.append([0,0])
                P3.append([b,0])
                P4.append([a*np.cos(C[n])+b, a*np.sin(C[n])])

                test_pos.append([[P2[-1][0],P2[-1][1]],
                            [P3[-1][0],P3[-1][1]],
                            [(P4[-1][0]+P3[-1][0])/2,(P4[-1][1]+P3[-1][1])/2],
                            [(P3[-1][0]+P2[-1][0])/2,(P3[-1][1]+P2[-1][1])/2],
                            [(P2[-1][0]+P1[-1][0])/2,(P2[-1][1]+P1[-1][1])/2]])
        elif A and a and c:
            NN = N/2
            b = np.hstack([
                np.arange(0,a+c+(a+c)/NN,(a+c)/NN),
                np.arange(a+c,0,-(a+c)/NN)])
            NN = NN/2
            B = np.hstack([
                np.arange(0,np.pi+np.pi/NN,np.pi/NN),
                np.arange(np.pi,0,-np.pi/NN),
                np.arange(0,np.pi+np.pi/NN,np.pi/NN),
                np.arange(np.pi,0,-np.pi/NN)])
            
            P1, P2, P3, P4 = [], [], [], []
            text_keys = ['A','B','a','c','b']
            test_pos = []
            for n in range(N):
                P1.append([b[n], 0])
                P2.append([0,0])
                P3.append([c*np.cos(A),c*np.sin(A)])
                P4.append([P3[-1][0]+a*np.cos(A-np.pi+B[n]), P3[-1][1]+a*np.sin(A-np.pi+B[n])])

                test_pos.append([[P2[-1][0],P2[-1][1]],
                            [P3[-1][0],P3[-1][1]],
                            [(P4[-1][0]+P3[-1][0])/2,(P4[-1][1]+P3[-1][1])/2],
                            [(P3[-1][0]+P2[-1][0])/2,(P3[-1][1]+P2[-1][1])/2],
                            [(P2[-1][0]+P1[-1][0])/2,(P2[-1][1]+P1[-1][1])/2]])


        # scale path to 1
        P = np.array(P1+P2+P3+P4)
        scale = np.max(
            [np.max(P[:,0])-np.min(P[:,0]),
             np.max(P[:,1])-np.min(P[:,1])])
        P1 = np.array(P1)/scale
        P2 = np.array(P2)/scale
        P3 = np.array(P3)/scale
        P4 = np.array(P4)/scale
        # center
        xOffset = (1-np.max([P1[:,0],P2[:,0],P3[:,0],P4[:,0]]))/2
        yOffset = (1-np.max([P1[:,1],P2[:,1],P3[:,1],P4[:,1]]))/2
        P1[:,0], P1[:,1] = P1[:,0]+xOffset, P1[:,1]+yOffset
        P2[:,0], P2[:,1] = P2[:,0]+xOffset, P2[:,1]+yOffset
        P3[:,0], P3[:,1] = P3[:,0]+xOffset, P3[:,1]+yOffset
        P4[:,0], P4[:,1] = P4[:,0]+xOffset, P4[:,1]+yOffset
        
        test_pos = np.array(test_pos)
        test_pos = test_pos/scale
        for n in range(N): 
            test_pos[n][:,0], test_pos[n][:,1] = test_pos[n][:,0]+xOffset, test_pos[n][:,1]+yOffset
            for i in range(test_pos[n].shape[0]):
                test_pos[n][i,0] = test_pos[n][i,0]+fontshifts[text_keys[i]][0]
                test_pos[n][i,1] = test_pos[n][i,1]+fontshifts[text_keys[i]][1]
        
        # describe path
        codes = [Path.MOVETO,
                 Path.LINETO,
                 Path.LINETO,
                 Path.LINETO,
                 ]
        # setup path
        for n in range(N):
            verts = []
            verts.append(P1[n])
            verts.append(P2[n])
            verts.append(P3[n])
            verts.append(P4[n])
        
            # build path
            path = Path(verts, codes)

            # build text
            text_list = info_box(triangle)
            
            for k in range(len(text_keys)):
                t = text_keys[k]
                p = test_pos[n][k]
                text_list.append(MplText(p,t, fontsize = fontsize))
        
            list_of_args.append([path,text_list])
    return list_of_args

def draw_path(fig, path, text_list):
    fig.clf()
    axes = fig.add_subplot(111)

    for text in text_list:
        text.print(axes)

    patch = patches.PathPatch(path, facecolor='none', edgecolor = 'red', lw=2)
    axes.add_patch(patch)
        
    axes.set_xlim(-0.2,1.2)
    axes.set_ylim(-0.2,1.2)
    axes.axis('off')

def info_box(triangle):
    text_list = []
    
    A = triangle.get('A',None)
    B = triangle.get('B',None)
    C = triangle.get('C',None)
    a = triangle.get('a',None)
    b = triangle.get('b',None)
    c = triangle.get('c',None)

    fontsize = 'large'
    
    lineShift = 0.05
    colShift = 0.3
    start_pos = [-0.1,1.05]

    keys = ['A','B','C','a','b','c']
    values = [A,B,C,a,b,c]
    pos = [start_pos,
           [start_pos[0],start_pos[1]-lineShift],
           [start_pos[0],start_pos[1]-2*lineShift],
           [start_pos[0]+colShift,start_pos[1]],
           [start_pos[0]+colShift,start_pos[1]-lineShift],
           [start_pos[0]+colShift,start_pos[1]-2*lineShift]]
    
    for n in range(len(keys)):
        t = '{} = {}'.format(keys[n],'{:.02f}'.format(values[n]) if values[n] else '?')
        p = pos[n]
        text_list.append(MplText(p,t, fontsize = fontsize, axescords = True))
    return text_list

class MplText(object):

    def __init__(self,pos,text,**kwargs):
        self.text = text
        self.pos = pos
        self.axescords = kwargs.pop('axescords',None)
        self.kwargs = kwargs
        
    def print(self,ax):
        if self.axescords:
            ax.text(self.pos[0],self.pos[1],self.text,transform = ax.transAxes,**self.kwargs)
        else:
            ax.text(self.pos[0],self.pos[1],self.text,**self.kwargs)
