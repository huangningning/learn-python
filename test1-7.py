# -*- coding:utf-8 -*-
#姓名:黄靖宇
#学号:1403050107
#班级:通风14级1班
#test7
import math
a=input('输入a:')
#dx=0.1
f1=(math.pow(3+0.1,a)-math.pow(3,a))/0.1
print 'f1=',f1
#dx=0.01
f2=(math.pow(3+0.01,a)-math.pow(3,a))/0.01
print 'f1=',f1,'f2=',f2
#dx=0.001
f3=(math.pow(3+0.001,a)-math.pow(3,a))/0.001
print 'f1=',f1,'f2=',f2,'f3=',f3
#dx=0.0001
f4=(math.pow(3+0.0001,a)-math.pow(3,a))/0.0001
print 'f1=',f1,'f2=',f2,'f3=',f3,'f4=',f4