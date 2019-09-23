from qutip import * #Liberia qutip
from matplotlib.pyplot import * #Libreria matplotlib
import numpy as np #Liberia numpy
import math as math
I1 = Qobj( np.array( [ [0.5, 0.0, 0.0, 0.5], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.5, 0.0, 0.0, 0.5] ] ) ) #Definir estado inicial Bell 1
I1_A = Qobj( np.array( [[0.5, 0.0], [0.0, 0.5]] ) ) #Traza parcial A
I1_B = Qobj( np.array( [[0.5, 0.0], [0.0, 0.5]] ) ) #Traza parcial B
I2 = Qobj( np.array( [ [0.0, 0.0, 0.0, 0.0], [0.0, 0.5, 0.5, 0.0], [0.0, 0.5, 0.5, 0.0], [0.0, 0.0, 0.0, 0.0] ] ) ) #Definir estado inicial Bell 3
I2_A = Qobj( np.array( [[0.5, 0.0], [0.0, 0.5]] ) ) #Traza parcial A
I2_B = Qobj( np.array( [[0.5, 0.0], [0.0, 0.5]] ) ) #Traza parcial B
I3 = Qobj( np.array( [ [0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0] ] ) ) #Definir estado inicial logico 01
I3_A = Qobj( np.array( [[1.0, 0.0], [0.0, 0.0]] ) ) #Traza parcial A
I3_B = Qobj( np.array( [[0.0, 0.0], [0.0, 1.0]] ) ) #Traza parcial B
I4 = Qobj( np.array( [ [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0] ] ) ) #Definir estado inicial logico 11
I4_A = Qobj( np.array( [[0.0, 0.0], [0.0, 1.0]] ) )#Traza parcoial A
I4_B = Qobj( np.array( [[0.0, 0.0], [0.0, 1.0]] ) )#Traza parcial B
I5 = Qobj( np.array( [ [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0] ] ) ) #Definir estado inicial logico 00
I5_A = Qobj( np.array( [[1.0, 0.0], [0.0, 0.0]] ) )#Traza parcial A
I5_B = Qobj( np.array( [[1.0, 0.0], [0.0, 0.0]] ) )#Traza parcial B
times = np.linspace(int(0.0), int(10.0), int(1000.0)) #Definir intervalo temporal
S0S = Qobj( np.array( [ [0.0, 0.0], [1.0, 0.0] ] ) )#Reservorio vacio sin interaccion con el otro
S1S = Qobj( np.array( [ [0.0, 0.0], [1.1, 0.0] ] ) )#Reservorio termal sin interaccion con el otro
S2S = Qobj( np.array( [ [0.0, -0.1], [1.1, 0.0] ] ) )#Reservorio comprimido sin interaccion con el otro
S0C = Qobj( np.array( [ [0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 1.0, 0.0] ]) ) #Reservorios vacios con interaccion
S1C = Qobj( np.array( [ [0.0, 0.0, 0.0, 0.0], [1.1, 0.0, 0.0, 0.0], [1.1, 0.0, 0.0, 0.0], [0.0, 1.1, 1.1, 0.0] ]) ) #Reservorios termales con interaccion
S2C = Qobj( np.array( [ [0.0,-0.1,-0.1, 0.0], [1.1, 0.0, 0.0, 0.0], [1.1, 0.0, 0.0, 0.0], [0.0, 1.1, 1.1, 0.0] ]) ) #Reservorios comprimidos con interaccion
em_I1_S0C = mesolve(identity(4), I1, times, S0C)  #Ecuacion Maestra para estado inicial Bell 00 con reservorios vacios con interaccion
em_I2_S0C = mesolve(identity(4), I2, times, S0C)  #Ecuacion Maestra para estado inicial Bell 10 con reservorios vacios con interaccion
em_I3_S0C = mesolve(identity(4), I3, times, S0C)  #Ecuacion Maestra para estado inicial logico 01 con reservorios vacios con interaccion
em_I4_S0C = mesolve(identity(4), I4, times, S0C)  #Ecuacion Maestra para estado inicial logico 11 con reservorios vacios con interaccion
em_I5_S0C = mesolve(identity(4), I5, times, S0C)  #Ecuacion Maestra para estado inicial logico 00 con reservorios vacios con interaccion
em_I1_S1C = mesolve(identity(4), I1, times, S1C)  #Ecuacion Maestra para estado inicial Bell 00 con reservorios termales con tinteraccion
em_I2_S1C = mesolve(identity(4), I2, times, S1C) #Ecuacion Maestra para estado inicial Bell 10 con reservorios termales con interaccion
em_I3_S1C = mesolve(identity(4), I3, times, S1C) #Ecuacion Maestra para estado inicial logico 01 con reservorios termales con interaccion
em_I4_S1C = mesolve(identity(4), I4, times, S1C) #Ecuacion Maestra para estado inicial logico 11 con reservorios termales con interaccion
em_I5_S1C = mesolve(identity(4), I5, times, S1C) #Ecuacion Maestra para estado inicial logico 00 con reservorios termales con interaccion
em_I1_S2C = mesolve(identity(4), I1, times, S2C) #Ecuacion Maestra para estado inicial Bell 00 con reservorios comprimidos con interaccion
em_I2_S2C = mesolve(identity(4), I2, times, S2C) #Ecuacion Maestra para estado inicial Bell 10 con reservorios comprimidos con interaccion
em_I3_S2C = mesolve(identity(4), I3, times, S2C) #Ecuacion Maestra para estado inicial logico 01 con reservorios comprimidos con interaccion
em_I4_S2C = mesolve(identity(4), I4, times, S2C) #Ecuacion Maestra para estado inicial logico 11 con reservorios comprimidos con interaccion
em_I5_S2C = mesolve(identity(4), I5, times, S2C) #Ecuacion Maestra para estado inicial logico 00 con reservorios comprimidos con interaccion
emA_I1_S0S = mesolve(identity(2), I1_A, times, S0S) #Ecuacion Maestra para estado inicial Bell 00 con reservorios vacios sin interaccion
emA_I2_S0S = mesolve(identity(2), I2_A, times, S0S) #Ecuacion Maestra para estado inicial Bell 10 con reservorios vacios sin interaccion
emA_I3_S0S = mesolve(identity(2), I3_A, times, S0S) #Ecuacion Maestra para estado inicial logico 01 con reservorios vacios sin interaccion
emA_I4_S0S = mesolve(identity(2), I4_A, times, S0S) #Ecuacion Maestra para estado inicial logico 11 con reservorios vacios sin interaccion
emA_I5_S0S = mesolve(identity(2), I5_A, times, S0S) #Ecuacion Maestra para estado inicial logico 00 con reservorios vacios sin interaccion
emA_I1_S1S = mesolve(identity(2), I1_A, times, S1S) #Ecuacion Maestra para estado inicial Bell 00 con reservorios termales sin interaccion
emA_I2_S1S = mesolve(identity(2), I2_A, times, S1S) #Ecuacion Maestra para estado inicial Bell 10 con reservorios termales sin interaccion
emA_I3_S1S = mesolve(identity(2), I3_A, times, S1S) #Ecuacion Maestra para estado inicial logico 01 con reservorios termales sin interaccion
emA_I4_S1S = mesolve(identity(2), I4_A, times, S1S) #Ecuacion Maestra para estado inicial logico 11 con reservorios termales sin interaccion
emA_I5_S1S = mesolve(identity(2), I5_A, times, S1S) #Ecuacion Maestra para estado inicial logico 00 con reservorios termales sin interaccion
emA_I1_S2S = mesolve(identity(2), I1_A, times, S2S) #Ecuacion Maestra para estado inicial Bell 00 con reservorios comprimidos sin interaccion
emA_I2_S2S = mesolve(identity(2), I2_A, times, S2S) #Ecuacion Maestra para estado inicial Bell 10 con reservorios comprimidos sin interaccion
emA_I3_S2S = mesolve(identity(2), I3_A, times, S2S) #Ecuacion Maestra para estado inicial logico 01 con reservorios comprimidos sin interaccion
emA_I4_S2S = mesolve(identity(2), I4_A, times, S2S) #Ecuacion Maestra para estado inicial logico 11 con reservorios comprimidos sin interaccion
emA_I5_S2S = mesolve(identity(2), I5_A, times, S2S) #Ecuacion Maestra para estado inicial logico 00 con reservorios comprimidos sin interaccion
emB_I1_S0S = mesolve(identity(2), I1_B, times, S0S) #Ecuacion Maestra para estado inicial Bell 00 con reservorios vacios sin interaccion
emB_I2_S0S = mesolve(identity(2), I2_B, times, S0S) #Ecuacion Maestra para estado inicial Bell 10 con reservorios vacios sin interaccion
emB_I3_S0S = mesolve(identity(2), I3_B, times, S0S) #Ecuacion Maestra para estado inicial logico 01 con reservorios vacios sin interaccion
emB_I4_S0S = mesolve(identity(2), I4_B, times, S0S) #Ecuacion Maestra para estado inicial logico 11 con reservorios vacios sin interaccion
emB_I5_S0S = mesolve(identity(2), I5_B, times, S0S) #Ecuacion Maestra para estado inicial logico 00 con reservorios vacios sin interaccion
emB_I1_S1S = mesolve(identity(2), I1_B, times, S1S) #Ecuacion Maestra para estado inicial Bell 00 con reservorios termales sin interaccion
emB_I2_S1S = mesolve(identity(2), I2_B, times, S1S) #Ecuacion Maestra para estado inicial Bell 10 con reservorios termales sin interaccion
emB_I3_S1S = mesolve(identity(2), I3_B, times, S1S) #Ecuacion Maestra para estado inicial logico 01 con reservorios termales sin interaccion
emB_I4_S1S = mesolve(identity(2), I4_B, times, S1S) #Ecuacion Maestra para estado inicial logico 11 con reservorios termales sin interaccion
emB_I5_S1S = mesolve(identity(2), I5_B, times, S1S) #Ecuacion Maestra para estado inicial logico 00 con reservorios termales sin interaccion
emB_I1_S2S = mesolve(identity(2), I1_B, times, S2S) #Ecuacion Maestra para estado inicial Bell 00 con reservorios comprimidos sin interaccion
emB_I2_S2S = mesolve(identity(2), I2_B, times, S2S) #Ecuacion Maestra para estado inicial Bell 10 con reservorios comprimidos sin interaccion
emB_I3_S2S = mesolve(identity(2), I3_B, times, S2S) #Ecuacion Maestra para estado inicial logico 01 con reservorios comprimidos sin interaccion
emB_I4_S2S = mesolve(identity(2), I4_B, times, S2S) #Ecuacion Maestra para estado inicial logico 11 con reservorios comprimidos sin interaccion
emB_I5_S2S = mesolve(identity(2), I5_B, times, S2S) #Ecuacion Maestra para estado inicial logico 00 con reservorios comprimidos sin interaccion
tiempo = [(1/20)*i for i in range(100)]#Intervalo de tiempo para los gráficos
#Reservorio vacío sin interacción
conc_I1_S0S=[0 for i in range(100)]
disc_I1_S0S=[0 for i in range(100)]
conc_I2_S0S=[0 for i in range(100)]
disc_I2_S0S=[0 for i in range(100)]
conc_I3_S0S=[0 for i in range(100)]
disc_I3_S0S=[0 for i in range(100)]
conc_I4_S0S=[0 for i in range(100)]
disc_I4_S0S=[0 for i in range(100)]
conc_I5_S0S=[0 for i in range(100)]
disc_I5_S0S=[0 for i in range(100)]
for i in range (0,100):
    matA=Qobj(emA_I1_S0S.states[i])
    matB=Qobj(emB_I1_S0S.states[i])
    c1=tensor(matA,matB).eigenenergies()[2]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[1]
    c2=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[2]
    c3=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[2]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I1_S0S[i]=np.amax(carray)
    disc_I1_S0S[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))

    
for i in range (0,100):
    matA=Qobj(emA_I2_S0S.states[i])
    matB=Qobj(emB_I2_S0S.states[i])
    c1=tensor(matA,matB).eigenenergies()[2]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[1]
    c2=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[2]
    c3=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[2]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I2_S0S[i]=np.amax(carray)
    disc_I2_S0S[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    matA=Qobj(emA_I3_S0S.states[i])
    matB=Qobj(emB_I3_S0S.states[i])
    c1=tensor(matA,matB).eigenenergies()[2]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[1]
    c2=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[2]
    c3=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[2]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I3_S0S[i]=np.amax(carray)
    disc_I3_S0S[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    matA=Qobj(emA_I4_S0S.states[i])
    matB=Qobj(emB_I4_S0S.states[i])
    c1=tensor(matA,matB).eigenenergies()[2]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[1]
    c2=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[2]
    c3=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[2]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[3]
    print(c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I4_S0S[i]=np.amax(carray)
    disc_I4_S0S[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    matA=Qobj(emA_I5_S0S.states[i])
    matB=Qobj(emB_I5_S0S.states[i])
    c1=tensor(matA,matB).eigenenergies()[2]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[1]
    c2=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[2]
    c3=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[2]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I5_S0S[i]=np.amax(carray)
    disc_I5_S0S[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


#Reservorio térmico sin interacción
conc_I1_S1S=[0 for i in range(100)]
disc_I1_S1S=[0 for i in range(100)]
conc_I2_S1S=[0 for i in range(100)]
disc_I2_S1S=[0 for i in range(100)]
conc_I3_S1S=[0 for i in range(100)]
disc_I3_S1S=[0 for i in range(100)]
conc_I4_S1S=[0 for i in range(100)]
disc_I4_S1S=[0 for i in range(100)]
conc_I5_S1S=[0 for i in range(100)]
disc_I5_S1S=[0 for i in range(100)]
for i in range (0,100):
    matA=Qobj(emA_I1_S1S.states[i])
    matB=Qobj(emB_I1_S1S.states[i])
    c1=tensor(matA,matB).eigenenergies()[2]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[1]
    c2=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[2]
    c3=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[2]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I1_S1S[i]=np.amax(carray)
    disc_I1_S1S[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))

    
for i in range (0,100):
    matA=Qobj(emA_I2_S1S.states[i])
    matB=Qobj(emB_I2_S1S.states[i])
    c1=tensor(matA,matB).eigenenergies()[2]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[1]
    c2=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[2]
    c3=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[2]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I2_S1S[i]=np.amax(carray)
    disc_I2_S1S[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    matA=Qobj(emA_I3_S1S.states[i])
    matB=Qobj(emB_I3_S1S.states[i])
    c1=tensor(matA,matB).eigenenergies()[2]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[1]
    c2=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[2]
    c3=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[2]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I3_S1S[i]=np.amax(carray)
    disc_I3_S1S[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    matA=Qobj(emA_I4_S1S.states[i])
    matB=Qobj(emB_I4_S1S.states[i])
    c1=tensor(matA,matB).eigenenergies()[2]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[1]
    c2=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[2]
    c3=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[2]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I4_S1S[i]=np.amax(carray)
    disc_I4_S1S[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    matA=Qobj(emA_I5_S1S.states[i])
    matB=Qobj(emB_I5_S1S.states[i])
    c1=tensor(matA,matB).eigenenergies()[2]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[1]
    c2=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[2]
    c3=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[2]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0.5*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I5_S1S[i]=np.amax(carray)
    disc_I5_S1S[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


#Reservorio comprimido sin interacción
conc_I1_S2S=[0 for i in range(100)]
disc_I1_S2S=[0 for i in range(100)]
conc_I2_S2S=[0 for i in range(100)]
disc_I2_S2S=[0 for i in range(100)]
conc_I3_S2S=[0 for i in range(100)]
disc_I3_S2S=[0 for i in range(100)]
conc_I4_S2S=[0 for i in range(100)]
disc_I4_S2S=[0 for i in range(100)]
conc_I5_S2S=[0 for i in range(100)]
disc_I5_S2S=[0 for i in range(100)]
for i in range (0,100):
    matA=Qobj(emA_I1_S2S.states[i])
    matB=Qobj(emB_I1_S2S.states[i])
    c1=tensor(matA,matB).eigenenergies()[2]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[1]
    c2=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[2]
    c3=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[2]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I1_S2S[i]=np.amax(carray)
    disc_I1_S2S[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))

for i in range (0,100):
    matA=Qobj(emA_I2_S2S.states[i])
    matB=Qobj(emB_I2_S2S.states[i])
    c1=tensor(matA,matB).eigenenergies()[2]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[1]
    c2=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[2]
    c3=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[2]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I2_S2S[i]=np.amax(carray)
    disc_I2_S2S[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))

for i in range (0,100):
    matA=Qobj(emA_I3_S2S.states[i])
    matB=Qobj(emB_I3_S2S.states[i])
    c1=tensor(matA,matB).eigenenergies()[2]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[1]
    c2=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[2]
    c3=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[2]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I3_S2S[i]=np.amax(carray)
    disc_I3_S2S[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    matA=Qobj(emA_I4_S2S.states[i])
    matB=Qobj(emB_I4_S2S.states[i])
    c1=tensor(matA,matB).eigenenergies()[2]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[1]
    c2=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[2]
    c3=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[2]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I4_S2S[i]=np.amax(carray)
    disc_I4_S2S[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    matA=Qobj(emA_I5_S2S.states[i])
    matB=Qobj(emB_I5_S2S.states[i])
    c1=tensor(matA,matB).eigenenergies()[2]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[1]
    c2=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[3]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[2]
    c3=tensor(matA,matB).eigenenergies()[1]+tensor(matA,matB).eigenenergies()[2]-tensor(matA,matB).eigenenergies()[0]-tensor(matA,matB).eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I5_S2S[i]=np.amax(carray)
    disc_I5_S2S[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


#Reservorio vacío con interacción
conc_I1_S0C=[0 for i in range(100)]
disc_I1_S0C=[0 for i in range(100)]
conc_I2_S0C=[0 for i in range(100)]
disc_I2_S0C=[0 for i in range(100)]
conc_I3_S0C=[0 for i in range(100)]
disc_I3_S0C=[0 for i in range(100)]
conc_I4_S0C=[0 for i in range(100)]
disc_I4_S0C=[0 for i in range(100)]
conc_I5_S0C=[0 for i in range(100)]
disc_I5_S0C=[0 for i in range(100)]
for i in range (0,100):
    mat=Qobj(em_I1_S0C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I1_S0C[i]=np.amax(carray)
    disc_I1_S0C[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))

    
for i in range (0,100):
    mat=Qobj(em_I2_S0C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I2_S0C[i]=np.amax(carray)
    disc_I2_S0C[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    mat=Qobj(em_I3_S0C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I3_S0C[i]=np.amax(carray)
    disc_I3_S0C[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    mat=Qobj(em_I4_S0C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print(c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I4_S0C[i]=np.amax(carray)
    disc_I4_S0C[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    mat=Qobj(em_I5_S0C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I5_S0C[i]=np.amax(carray)
    disc_I5_S0C[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


#Reservorio térmico con interacción
conc_I1_S1C=[0 for i in range(100)]
disc_I1_S1C=[0 for i in range(100)]
conc_I2_S1C=[0 for i in range(100)]
disc_I2_S1C=[0 for i in range(100)]
conc_I3_S1C=[0 for i in range(100)]
disc_I3_S1C=[0 for i in range(100)]
conc_I4_S1C=[0 for i in range(100)]
disc_I4_S1C=[0 for i in range(100)]
conc_I5_S1C=[0 for i in range(100)]
disc_I5_S1C=[0 for i in range(100)]
for i in range (0,100):
    mat=Qobj(em_I1_S1C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I1_S1C[i]=np.amax(carray)
    disc_I1_S1C[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))

    
for i in range (0,100):
    mat=Qobj(em_I2_S1C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I2_S1C[i]=np.amax(carray)
    disc_I2_S1C[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    mat=Qobj(em_I3_S1C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I3_S1C[i]=np.amax(carray)
    disc_I3_S1C[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    mat=Qobj(em_I4_S1C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I4_S1C[i]=np.amax(carray)
    disc_I4_S1C[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    mat=Qobj(em_I5_S1C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0.5*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I5_S1C[i]=np.amax(carray)
    disc_I5_S1C[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


#Reservorio comprimido con interacción
conc_I1_S2C=[0 for i in range(100)]
disc_I1_S2C=[0 for i in range(100)]
conc_I2_S2C=[0 for i in range(100)]
disc_I2_S2C=[0 for i in range(100)]
conc_I3_S2C=[0 for i in range(100)]
disc_I3_S2C=[0 for i in range(100)]
conc_I4_S2C=[0 for i in range(100)]
disc_I4_S2C=[0 for i in range(100)]
conc_I5_S2C=[0 for i in range(100)]
disc_I5_S2C=[0 for i in range(100)]
for i in range (0,100):
    mat=Qobj(em_I1_S2C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I1_S2C[i]=np.amax(carray)
    disc_I1_S2C[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))

for i in range (0,100):
    mat=Qobj(em_I2_S2C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I2_S2C[i]=np.amax(carray)
    disc_I2_S2C[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))

for i in range (0,100):
    mat=Qobj(em_I3_S2C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I3_S2C[i]=np.amax(carray)
    disc_I3_S2C[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    mat=Qobj(em_I4_S2C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I4_S2C[i]=np.amax(carray)
    disc_I4_S2C[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


for i in range (0,100):
    mat=Qobj(em_I5_S2C.states[i])
    c1=mat.eigenenergies()[2]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[1]
    c2=mat.eigenenergies()[1]+mat.eigenenergies()[3]-mat.eigenenergies()[0]-mat.eigenenergies()[2]
    c3=mat.eigenenergies()[1]+mat.eigenenergies()[2]-mat.eigenenergies()[0]-mat.eigenenergies()[3]
    print (c1,c2,c3)
    consar=np.array([c1,c2,c3])
    c=np.amax(consar)
    carray=np.array([0,2*(c1+c2-1-c3),2*(c1-c1-1+c3)])
    conc_I5_S2C[i]=np.amax(carray)
    disc_I5_S2C[i]=0.5*((1-c1-c2-c3)*np.log2(np.absolute(1-c1-c2-c3))+(1-c1+c2+c3)*np.log2(np.absolute(1-c1+c2+c3))-(1+c)*np.log2(np.absolute(1+c))-(1-c)*np.log2(np.absolute(1-c)))


#Graficar
figure()
plot(tiempo,disc_I1_S0S)
plot(tiempo,disc_I1_S1S)
plot(tiempo,disc_I1_S2S)
xlabel('gamma tiempo')
ylabel('discordia cuantica')
legend(('reservorio vacio', 'reservorio termico','reservorio comprimido'))
savefig('disc_bell1_S.png')

figure()
plot(tiempo,disc_I2_S0S)
plot(tiempo,disc_I2_S1S)
plot(tiempo,disc_I2_S2S)
xlabel('gamma tiempo')
ylabel('discordia cuantica')
legend(('reservorio vacio', 'reservorio termico','reservorio comprimido'))
savefig('disc_bell3_S.png')

figure()
plot(tiempo,disc_I3_S0S)
plot(tiempo,disc_I3_S1S)
plot(tiempo,disc_I3_S2S)
xlabel('gamma tiempo')
ylabel('discordia cuantica')
legend(('reservorio vacio', 'reservorio termico','reservorio comprimido'))
savefig('disc_logi2_S.png')

figure()
plot(tiempo,disc_I4_S0S)
plot(tiempo,disc_I4_S1S)
plot(tiempo,disc_I4_S2S)
xlabel('gamma tiempo')
ylabel('discordia cuantica')
legend(('reservorio vacio', 'reservorio termico','reservorio comprimido'))
savefig('disc_logi4_S.png')

figure()
plot(tiempo,disc_I5_S0S)
plot(tiempo,disc_I5_S1S)
plot(tiempo,disc_I5_S2S)
xlabel('gamma tiempo')
ylabel('discordia cuantica')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('disc_logi1_S.png')

figure()
plot(tiempo,conc_I1_S0S)
plot(tiempo,conc_I1_S1S)
plot(tiempo,conc_I1_S2S)
xlabel('gamma tiempo')
ylabel('concurrencia')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('conc_bell1_S.png')

figure()
plot(tiempo,conc_I2_S0S)
plot(tiempo,conc_I2_S1S)
plot(tiempo,conc_I2_S2S)
xlabel('gamma tiempo')
ylabel('concurrencia')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('conc_bell3_S.png')

figure()
plot(tiempo,conc_I3_S0S)
plot(tiempo,conc_I3_S1S)
plot(tiempo,conc_I3_S2S)
xlabel('gamma tiempo')
ylabel('concurrencia')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('conc_logi3_S.png')

figure()
plot(tiempo,conc_I4_S0S)
plot(tiempo,conc_I4_S1S)
plot(tiempo,conc_I4_S2S)
xlabel('gamma tiempo')
ylabel('concurrencia')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('conc_logi4_S.png')

figure()
plot(tiempo,conc_I5_S0S)
plot(tiempo,conc_I5_S1S)
plot(tiempo,conc_I5_S2S)
xlabel('gamma tiempo')
ylabel('concurrencia')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('conc_logi1_S.png')

figure()
plot(tiempo,disc_I1_S0C)
plot(tiempo,disc_I1_S1C)
plot(tiempo,disc_I1_S2C)
xlabel('gamma tiempo')
ylabel('discordia cuantica')
legend(('reservorio vacio', 'reservorio termico','reservorio comprimido'))
savefig('disc_bell1_C.png')

figure()
plot(tiempo,disc_I2_S0C)
plot(tiempo,disc_I2_S1C)
plot(tiempo,disc_I2_S2C)
xlabel('gamma tiempo')
ylabel('discordia cuantica')
legend(('reservorio vacio', 'reservorio termico','reservorio comprimido'))
savefig('disc_bell3_C.png')

figure()
plot(tiempo,disc_I3_S0C)
plot(tiempo,disc_I3_S1C)
plot(tiempo,disc_I3_S2C)
xlabel('gamma tiempo')
ylabel('discordia cuantica')
legend(('reservorio vacio', 'reservorio termico','reservorio comprimido'))
savefig('disc_logi2_C.png')

figure()
plot(tiempo,disc_I4_S0C)
plot(tiempo,disc_I4_S1C)
plot(tiempo,disc_I4_S2C)
xlabel('gamma tiempo')
ylabel('discordia cuantica')
legend(('reservorio vacio', 'reservorio termico','reservorio comprimido'))
savefig('disc_logi4_C.png')

figure()
plot(tiempo,disc_I5_S0C)
plot(tiempo,disc_I5_S1C)
plot(tiempo,disc_I5_S2C)
xlabel('gamma tiempo')
ylabel('discordia cuantica')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('disc_logi1_C.png')

figure()
plot(tiempo,conc_I1_S0C)
plot(tiempo,conc_I1_S1C)
plot(tiempo,conc_I1_S2C)
xlabel('gamma tiempo')
ylabel('concurrencia')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('conc_bell1_C.png')

figure()
plot(tiempo,conc_I2_S0C)
plot(tiempo,conc_I2_S1C)
plot(tiempo,conc_I2_S2C)
xlabel('gamma tiempo')
ylabel('concurrencia')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('conc_bell3_C.png')

figure()
plot(tiempo,conc_I3_S0C)
plot(tiempo,conc_I3_S1C)
plot(tiempo,conc_I3_S2C)
xlabel('gamma tiempo')
ylabel('concurrencia')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('conc_logi3_C.png')

figure()
plot(tiempo,conc_I4_S0C)
plot(tiempo,conc_I4_S1C)
plot(tiempo,conc_I4_S2C)
xlabel('gamma tiempo')
ylabel('concurrencia')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('conc_logi4_C.png')

figure()
plot(tiempo,conc_I5_S0C)
plot(tiempo,conc_I5_S1C)
plot(tiempo,conc_I5_S2C)
xlabel('gamma tiempo')
ylabel('concurrencia')
legend(('reservorio vacio', 'reservorio termico', 'reservorio comprimido'))
savefig('conc_logi1_S.png')


