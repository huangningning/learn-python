# -*- coding:utf-8 -*-
#姓名:黄靖宇
#学号:1403050107
#班级:通风14级1班
#test6
import math
a=input('输入a:')
b=input('输入b:')
c=input('输入c:')
D=b*b-4*a*c
print 'D=',D
if D<0:
 print '无解'
else:
 x1=(-1.0*b+math.sqrt(D))/(2*a)
 x2=(-1.0*b-math.sqrt(D))/(2*a)
 print x1,x2