import numpy as np

def status_decorator(func):
    msgSys = 'System Status | {}'
    def add_str(*args, **kwargs):
        return msgSys.format(func(*args, **kwargs))
    return add_str

##@status_decorator
##def status_ok():
##    msgOk = 'Ok'
##    return msgOk
##
##@status_decorator
##def status_unacceptable_values():
##    msgError = 'Error: {}'
##    msgUnacc = 'Unacceptable values.'
##    msgUnacc = msgError.format(msgUnacc)
##    return msgUnacc

@status_decorator
def status_triangle(status_code):
    msg = {0:'Ok.',
           1:'Two solutions.',
           2:'No posible solution.',
           3:'Missing apropriate value or values.',
           4:'One or more values are above/below limits.'}
    if status_code in msg.keys():
        return msg[status_code]
    else:
        return 'Unknown status code!'
        
    
##@status_decorator
##def status_triangle(triangle, deg_rad):
##    
##    A = triangle.get('A',None)
##    B = triangle.get('B',None)
##    C = triangle.get('C',None)
##    a = triangle.get('a',None)
##    b = triangle.get('b',None)
##    c = triangle.get('c',None)
##    
##    msgError = 'Error: {}'
##    msgA = 'Angle A'
##    msgB = 'Angle B'
##    msgC = 'Angle C'
##    msga = 'Side a'
##    msgb = 'Side b'
##    msgc = 'Side c'
##    msgG = 'greater'
##    msgL = 'less'
##    msgDeg = ' degree'
##    msg180d = '180{}'.format(msgDeg)
##    msg0d = '0{}'.format(msgDeg)
##    msgPi = 'Pi'
##    msg0 = '0'
##    msgAngULim = msg180d if deg_rad else msgPi
##    msgAngLLim = msg0d if deg_rad else msg0
##    msgMis = 'Missing apropriate value or values.'
##    msgMis = msgError.format(msgMis)
##    msgML = 'Missing at least one length.'
##    msgML = msgError.format(msgML)
##    msgAng = 'The sum of the angles {} and {} are above {}.'
##    msgAng = msgAng.format('{}','{}',msg180d if deg_rad else msgPi)
##    msgAng = msgError.format(msgAng)
##    msgLim1 = '{} is {} or equal to {}.'
##    msgLim1 = msgError.format(msgLim1)
##    msgLim2 = '{}*sin({})/{} must be less than 1.'
##    msgLim2 = msgError.format(msgLim2)
##    msgLim3 = '{} must be less than {} + {}.'
##    msgLim3 = msgError.format(msgLim3)
##
##    msgData = 'A = {:.2f}{}, B = {:.2f}{}, C = {:.2f}{}, a = {:.2f}, b = {:.2f}, c = {:.2f}'
##    
##    values = [v for v in [A,B,C,a,b,c] if v!=None]
##    upLim = 180 if deg_rad else np.pi
##    msg = ''
##    if len(values)<3:
##        msg = msgMis
##    elif len(values)==3:
##        if A or A==0:
##            if A>=upLim:
##                msg = msgLim1.format(msgA, msgG, msgAngULim)
##            elif A<=0:
##                msg = msgLim1.format(msgA, msgL, msgAngLLim)
##        if B or B==0:
##            if B>=upLim:
##                msg = msgLim1.format(msgB, msgG, msgAngULim)
##            elif B<=0:
##                msg = msgLim1.format(msgB, msgL, msgAngLLim)
##        if C or C==0:
##            if C>=upLim:
##                msg = msgLim1.format(msgC, msgG, msgAngULim)
##            elif C<=0:
##                msg = msgLim1.format(msgC, msgL, msgAngLLim)
##        if a or a==0:
##            if a<=0:
##                msg = msgLim1.format(msga, msgL, msg0)
##        if b or b==0:
##            if b<=0:
##                msg = msgLim1.format(msgb, msgL, msg0)
##        if c or c==0:
##            if c<=0:
##                msg = msgLim1.format(msgc, msgL, msg0)
##        if msg=='':
##            if A and B and C:
##                msg = msgML
##            elif A and B:
##                msg = msgAng.format('A','B')
##            elif A and C:
##                msg = msgAng.format('A','C')
##            elif B and C:
##                msg = msgAng.format('B','C')
##            elif A and a and b:
##                msg = msgLim2.format('b','A','a')
##            elif A and a and c:
##                msg = msgLim2.format('c','A','a')
##            elif B and a and b:
##                msg = msgLim2.format('a','B','b')
##            elif B and b and c:
##                msg = msgLim2.format('c','B','b')
##            elif C and a and c:
##                msg = msgLim2.format('a','C','c')
##            elif C and b and c:
##                msg = msgLim2.format('b','C','c')
##            elif a and b and c:
##                vi = ['a','b','c']
##                v = [a,b,c]
##                mv = vi[v.index(np.max(v))]
##                vi.remove(mv)
##                msg = msgLim3.format(mv,vi[0],vi[1])
##    else:
##        msg = msgData.format(
##            A, msgDeg if deg_rad else '',
##            B, msgDeg if deg_rad else '',
##            C, msgDeg if deg_rad else '',
##            a,b,c)
##    return msg

