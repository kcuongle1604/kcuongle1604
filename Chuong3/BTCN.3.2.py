#duoc
M1=int(input('M1='))
M2=int(input('M2='))
M3=int(input('M3='))
S=int(input('S='))
if S<100 :
    Tiendien=M1*S
elif S<150 :
    Tiendien=(S-100)*M2+100*M1
elif S>150 :
    Tiendien=(S-150)*M3+50*M2+100*M1
print('Phai tra=',Tiendien,sep='')
    