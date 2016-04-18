import numpy as np
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from SimpleTrigometri.models.Calculations import triangle_calc

def test(triangle, deg_rad):

    ang_lim = [0, 180 if deg_rad else np.pi]
    pres = 0.00001
    len_lim = 0
    
    A = triangle.get('A',None)
    B = triangle.get('B',None)
    C = triangle.get('C',None)
    a = triangle.get('a',None)
    b = triangle.get('b',None)
    c = triangle.get('c',None)

    triangle = {k: v for k, v in triangle.items() if v}
    if len(triangle)!=6:
        print('Missing values!')
    else:
        for ang in [A,B,C]:
             if ang>=ang_lim[1] or ang<=ang_lim[0]:
                print('An Angle out of limits!')

        for l in [a,b,c]:
            if l<=len_lim:
                print('length below limit!')

        if not (a<b+c and b<a+c and c<a+b):
            print('a>b+c or b>a+c or c>a+b!')

        if A+B+C<ang_lim[1]-ang_lim[1]*pres or A+B+C>ang_lim[1]+ang_lim[1]*pres:
            print('Total angle is out of limits!')
        
def role(V,D):
    d = [D,D]
    v = []
    v.append([V[2],V[0],V[1],V[5],V[3],V[4]])
    v.append([V[1],V[2],V[0],V[4],V[5],V[3]])
    return v, d

V = [[30,None,None,5,7,None]]
dr = [True]

v, d = role(V[0],dr[0])

V+=v
dr+=d

v = [30,60,None,5,None,None]
d = True

V+=[v]
dr+=[d]

v, d = role(v,d)

V+=v
dr+=d


for n in range(len(dr)):
    deg_rad = dr[n]
    triangle = {}
    if V[n][0]:
        triangle['A']=V[n][0]
    if V[n][1]:
        triangle['B']=V[n][1]
    if V[n][2]:
        triangle['C']=V[n][2]
    if V[n][3]:
        triangle['a']=V[n][3]
    if V[n][4]:
        triangle['b']=V[n][4]
    if V[n][5]:
        triangle['c']=V[n][5]
    
    status, triangle = triangle_calc(triangle,deg_rad)

    if status == 0:
        test(triangle, deg_rad)
    elif status == 1:
        for t in triangle:
            test(t, deg_rad)

print('Done')
