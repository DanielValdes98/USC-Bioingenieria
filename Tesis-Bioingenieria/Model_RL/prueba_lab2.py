import numpy as np
from scipy.fftpack import fft
import math
import numpy as np 
import matplotlib.pyplot as plt
from scipy import signal
import wfdb
import os
import scipy.io.wavfile as waves
import wav_rw as wp

def fourierAn(y):
        #aplicar transformada de fourier a los datos
        Y = fft(y)
        # Calcular magnitud y angulo, normalizar por el num de muestras
        absY = abs(Y)/(y.size)                               
        #fase
        pY = np.unwrap(np.angle(Y))
        ###########################################
        #reorganizar el espectro para graficar
        #numero de muestras hasta la mitad del espectro
        hN=int(math.floor((Y.size+1)/2))
        absY=np.hstack((absY[hN:],absY[:hN]))
        pY=np.hstack((pY[hN:],pY[:hN]))

        #calcular la magnitud en dB
        absY[absY < np.finfo(float).eps] = np.finfo(float).eps    # Si hay ceros, reemplazar por un valor muy pequeno, antes de aplicar el log
        Ydb = 20 * np.log10(absY) 
        #retornar la magnitud, la magnitud en decibeles y la fase
        return absY,Ydb,pY

#’100’ corresponde a el archivo que se pretende leer, es necesario dar la
# direccion completa
#data=wfdb.io.rdsamp('100')
# data1=wfdb.io.rdsamp('ecg/clean/100')
# data2=wfdb.io.rdsamp('ecg/clean/101')
# data3=wfdb.io.rdsamp('ecg/clean/102')
# data4=wfdb.io.rdsamp('ecg/clean/103')
# data5=wfdb.io.rdsamp('ecg/clean/104')

# ecg100 = data1[0] #tomar el canal 0
# ecg101 = data2[0] #tomar el canal 0
# ecg102 = data3[0] #tomar el canal 0
# ecg103 = data4[0] #tomar el canal 0
# ecg104 = data5[0] #tomar el canal 0

# ecg100c1 = ecg100[:,0]
# ecg101c1 = ecg101[:,0]
# ecg102c1 = ecg102[:,0]
# ecg103c1 = ecg103[:,0]
# ecg104c1 = ecg104[:,0]

# fs = 360

# absY100,mY100,pY100=fourierAn(ecg100c1)
# absY101,mY101,pY101=fourierAn(ecg101c1)
# absY102,mY102,pY102=fourierAn(ecg102c1)
# absY103,mY103,pY103=fourierAn(ecg103c1)
# absY104,mY104,pY104=fourierAn(ecg104c1)

# #vector de frecuencias, desde -fs/2 a fs/2  (-pi<w<pi)
# f100=np.linspace(-fs/2,fs/2,mY100.size)
# f101=np.linspace(-fs/2,fs/2,mY101.size)
# f102=np.linspace(-fs/2,fs/2,mY102.size)
# f103=np.linspace(-fs/2,fs/2,mY103.size)
# f104=np.linspace(-fs/2,fs/2,mY104.size)

# # subplot(Filas,Columnas, posicion)

# plt.figure(figsize=(10, 20))
# # plt.figure(1)

# # plt.subplot(511)
# # plt.plot(ecg100)
# # plt.title('ECG 100')

# # plt.subplot(512)
# # plt.plot(ecg101)
# # plt.title('ECG 101')

# # plt.subplot(513)
# # plt.plot(ecg102)
# # plt.title('ECG 102')

# # plt.subplot(514)
# # plt.plot(ecg103)
# # plt.title('ECG 103')

# # plt.subplot(515)
# # plt.plot(ecg104)
# # plt.title('ECG 104')

# # Canales 1 
# plt.subplot(511)
# plt.plot(ecg100c1)
# plt.title('Canal 1 ECG 100')

# plt.subplot(512)
# plt.plot(ecg101c1)
# plt.title('Canal 1 ECG 101')

# plt.subplot(513)
# plt.plot(ecg102c1)
# plt.title('Canal 1 ECG 102')

# plt.subplot(514)
# plt.plot(ecg103c1)
# plt.title('Canal 1 ECG 103')

# plt.subplot(515)
# plt.plot(ecg104c1)
# plt.title('Canal 1 ECG 104')

# plt.show()

#######################################################################################################################

#lectura del archivo de texto donde se encuentran los datos
# file_name100='ecg/noisy/100.txt'
# file_name101='ecg/noisy/101.txt'
# file_name102='ecg/noisy/102.txt'
# file_name103='ecg/noisy/103.txt'
# file_name104='ecg/noisy/104.txt'


# #convertir los datos de texto a valores numericos la senal ecg
# x100=np.loadtxt(file_name100, delimiter=',') 
# x101=np.loadtxt(file_name101, delimiter=',') 
# x102=np.loadtxt(file_name102, delimiter=',') 
# x103=np.loadtxt(file_name103, delimiter=',') 
# x104=np.loadtxt(file_name104, delimiter=',') 

# Fs=360   #frecuencia de muestreo 

# ###########################################
# #aplicar transformada de fourier a los datos
# absYN100,mYdbN100,pYN100=fourierAn(x100)
# absYN101,mYdbN101,pYN101=fourierAn(x101)
# absYN102,mYdbN102,pYN102=fourierAn(x102)
# absYN103,mYdbN103,pYN103=fourierAn(x103)
# absYN104,mYdbN104,pYN104=fourierAn(x104)
# #vector de frecuencias, desde -fs/2 a fs/2  (-pi<w<pi)
# fN100=np.linspace(-Fs/2,Fs/2,absYN100.size)
# fN101=np.linspace(-Fs/2,Fs/2,absYN101.size)
# fN102=np.linspace(-Fs/2,Fs/2,absYN102.size)
# fN103=np.linspace(-Fs/2,Fs/2,absYN103.size)
# fN104=np.linspace(-Fs/2,Fs/2,absYN104.size)

# #se grafican las 3000 muestras del lado positivo y 1000 muestras del lado negativo, esto se puede modificar a conveniencia
# #y dependiendo del numero de muestras que se tengan
# Nplot=3000

# #disenar el filtro usando una ventana hamming
# b = signal.firwin(1024, 0.3, window='hamming', pass_zero=True)
# #filtrar la onda con ruido usando el filtro FIR
# yf100=signal.lfilter(b, [1.0],x100)
# yf101=signal.lfilter(b, [1.0],x101)
# yf102=signal.lfilter(b, [1.0],x102)
# yf103=signal.lfilter(b, [1.0],x103)
# yf104=signal.lfilter(b, [1.0],x104)

# #aplicar transformada de fourier a los datos
# absYN100f,mYdbN100f,pYN100f=fourierAn(yf100)
# absYN101f,mYdbN101f,pYN101f=fourierAn(yf101)
# absYN102f,mYdbN102f,pYN102f=fourierAn(yf102)
# absYN103f,mYdbN103f,pYN103f=fourierAn(yf103)
# absYN104f,mYdbN104f,pYN104f=fourierAn(yf104)

# #vector de frecuencias, desde -fs/2 a fs/2  (-pi<w<pi)
# fN100f=np.linspace(-Fs/2,Fs/2,absYN100f.size)
# fN101f=np.linspace(-Fs/2,Fs/2,absYN101f.size)
# fN102f=np.linspace(-Fs/2,Fs/2,absYN102f.size)
# fN103f=np.linspace(-Fs/2,Fs/2,absYN103f.size)
# fN104f=np.linspace(-Fs/2,Fs/2,absYN104f.size)

# print(Fs)
# # plt.figure(1)
# plt.subplot(311)
# plt.plot(x104)
# plt.title('ECG 104 con ruido')

# plt.subplot(312)
# plt.plot(yf104)
# plt.title('ECG 104 filtrada')

# plt.subplot(313)
# plt.plot(fN104f,mYdbN104f)
# plt.title('Espectro (dB) ECG 104 filtrada')

# # plt.savefig('punto7_101.png',bbox_inches='tight')
# plt.show()

#############################################################################

filename1='pcg/f10.wav'

#leer los archivos de audio
fs1,x1=wp.wavread(filename1)


t1=(np.arange(1,x1.size+1))/float(fs1)
#calcular el espectro de las ondas limpias y contaminadas
absY1,mY1,pY1=fourierAn(x1)


#vector de frecuencias, desde -fs/2 a fs/2  (-pi<w<pi)
f1=np.linspace(-fs1/2,fs1/2,absY1.size)

plt.figure(figsize=(20, 5))

# plt.figure(1)
plt.subplot(221)
plt.plot(t1,x1)
plt.title('Señal f10')

plt.subplot(222)
plt.plot(f1,mY1)
plt.title('Espectro (dB) f10')

plt.show()