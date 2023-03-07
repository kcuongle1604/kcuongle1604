#duoc
a=float(input('a=(a>0)'))
b=float(input('b=(b>0)'))
c=float(input('c=(c>0)'))
import math
if (a+b)>c and (a+c)>b and (b+c)>a :
   p=(a+b+c)/2
   s=math.sqrt(p*(p-a)*(p-b)*(p-c))
   print ('Dien tich=',round(s,3),sep='')
else :
 print('Khong hop le')