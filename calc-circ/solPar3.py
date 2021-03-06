#Milton Orlando Sarria Paja
#USC 2017
#solucion parcial 3

import numpy as np
import math


def text2numbers(lines):
    x=[]
    numID=[]
    for line in lines:
      #leer el dato de cada linea e ignorar el cambio de linea
      data = line[:-1]
      #convertir (x[-1:],x[-2:-1]) a flotantes y apilar en la lista x
      x.append([float(data[-1:]), float(data[-2:-1])])
      numID.append(data)
    #convertir la lista a un arreglo numpy
    x=np.array(x)
    return (x,numID)
    
file_name='data.txt'
hf = open(file_name,'r')
lines=hf.readlines()
hf.close()
#convertir los datos a valores numericos
x,numID=text2numbers(lines)
#definir parametros que son fijos
Vp=120.0
r3=np.sqrt(3)
r2=np.sqrt(2)
def unitC(angle):
    C=(np.cos(np.deg2rad(angle))+1j*np.sin(np.deg2rad(angle)))
    return C
    
for ii in np.arange(x.shape[0]):
    d=x[ii]
    ids=numID[ii]

    da=d[0]
    db=d[1]
    if (da==0): 
       da=5.
    if (db==0):
       db=5.
    if (ids=='1117513080'):
       da=5          
    if (ids== '92061276523'):
       da=8
       db=2
    #1) definir los valores que dependen del numero de identidad
    Z=da+1j*db
    theta=10*db
    Van=Vp*unitC(theta)
    VAB=r3*Vp*unitC(theta+30)
    IAB=VAB/Z
    #Realizar calculos
    angle_IAB=np.angle(IAB,deg=True)
    Ia=r3*np.abs(IAB)*unitC(angle_IAB-30)
        
    IBC=np.abs(IAB)*unitC(angle_IAB-120)
    angle_IBC=np.angle(IBC,deg=True)
    Ib=r3*np.abs(IAB)*unitC(angle_IBC-30)

    
    ICA=np.abs(IAB)*unitC(angle_IAB+120)
    angle_ICA=np.angle(ICA,deg=True)
    Ic=r3*np.abs(IAB)*unitC(angle_ICA-30)

    S=3*VAB*np.conjugate(IAB)
    print('#########################################')
    print('Solucion para', [da, db], ids)

    print('1)---------------')   
    print('Z:     ', np.abs(Z),np.angle(Z, deg=True)) 
    print('VAB:   ', np.abs(VAB),np.angle(VAB, deg=True))
    print('IAB: C ',IAB,' P:' ,np.abs(IAB),np.angle(IAB, deg=True))
    print('IBC: C ',IBC,' P:' ,np.abs(IBC),np.angle(IBC, deg=True))
    print('ICA: C ',ICA,' P:' ,np.abs(ICA),np.angle(ICA, deg=True))

    print('Ia: C  ',Ia,'  P:' ,np.abs(Ia),np.angle(Ia, deg=True))
    print('Ib: C  ',Ib,'  P:' ,np.abs(Ib),np.angle(Ib, deg=True))
    print('Ic: C  ',Ic,'  P:' ,np.abs(Ic),np.angle(Ic, deg=True))
    
    print('P=', S.real, ' S=', np.abs(S),'   fp=', S.real/np.abs(S))
    
    #2)     
    Vrms=10*db/r2*unitC(-10)
    Irms=3*db/r2*unitC(-50)
    S=Vrms*np.conjugate(Irms)
    print('2)---------------')
    print('|V|=', np.abs(Vrms), '  |I|=', np.abs(Irms))
    print('S=', S, '  |S|=', np.abs(S),'   P=', S.real,'   Q=', S.imag, '   fp=', S.real/np.abs(S))
    Z=Vrms/Irms
    print('Z=', Z, '; Polar:  |Z|=', np.abs(Z),'   theta=', np.angle(Z, deg=True))
    
    #3) 
    print('3)---------------')
    M  = 1j*(da+db)
    Zc = 1j*da
    R  = db
    V  = 100
    
    A =np.array([[4-Zc+1j*6,  -(1j*6+M)],\
                 [-(1j*6+M)  ,  1j*14+2*M+R]])
                 
    A1=np.array([[V    ,  -(1j*6+M)],\
                 [0.0  ,  1j*14+2*M+R]])
                 
    A2=np.array([[4-Zc+1j*6,  V],\
                 [-(1j*6+M) ,  0.0]]) 
     
    detA =np.linalg.det(A)
    detA1=np.linalg.det(A1)
    detA2=np.linalg.det(A2)
    
    I1=detA1/detA
    I2=detA2/detA
    print(A)
    print('I1', I1, 'Polar: ',np.abs(I1),np.angle(I1, deg=True))
    print('I2', I2, 'Polar: ',np.abs(I2),np.angle(I2, deg=True))
    
    
