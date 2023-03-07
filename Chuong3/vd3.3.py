x=int(input('Tieuthu='))
gia1=550
gia2=750
gia3=950
gia4=1350
if x<=100:
    Tiendien=x*gia1
elif x<=150 :
    Tiendien=(x-100)*gia2+gia1*100
elif x<=200 :
    Tiendien=gia1*100+gia2*50+(x-150)*gia3
else :
    Tiendien=gia1*100+gia2*50+50*gia3+(x-200)*gia4
Phaitra= Tiendien*1.1
print('Phai tra=',Phaitra,sep='')
