import DFEC
import pylab as plt
import numpy as np

fsample = 10000000
N = 2047
x=np.arange(((10**6)*(1/fsample)),((10**6)*((N+1)/fsample),((10**6)*(1/fsample))

DFEC.set_srs(1, 300000, 1)
DFEC.set_srs(2, 295000, 1)
x=np.arange(0*(1/200e6)*(1e6),2048*(1/200e6)*(1e6), (1/200e6))
#file is in goodroach1
#srs1 = 300kHz
#srs2 = 295kHz
plt.subplot(121)
plt.plot(x,roachd)
plt.title('Waveform of digital SSB Mixer', fontsize = 18)
plt.xlabel('Time($\mu$s)',fontsize = 16)
plt.ylabel('Amplitude(V)',fontsize = 16)

fy = np.fft.fft(roachd)
py = np.abs(fy)**2)*(1e-6)
freq = np.fft.fftfreq(fy.size, (1/(200*1e6))*(1e6))

plt.subplot(122)
plt.plot(freq, py)
plt.title('Mixed signal power spectrum Vsig=Vlo-dV', fontsize = 18)
plt.xlabel('Frequency(MHz)',fontsize = 16)
plt.ylabel('Power(MW)',fontsize = 16)
plt.show()


y = np.fromfile("mix_bram",dtype = '>i4', count = -1)
plt.plot(x,y)
plt.show()

x=np.arange(0*(1/200e6)*(1e6),2048*(1/200e6)*(1e6), (1e6)*(1/200e6)

fy = np.load('roach_data')
roach_data = fy['arr_0']

plt.subplot(121)
plt.plot(x,data_sin)
plt.title('Waveform of 20MHz signal mixed with sine', fontsize = 18)
plt.xlabel('Time($\mu$s)',fontsize = 16)
plt.ylabel('Amplitude(V)',fontsize = 16)

fy = np.fft.fft(data_sin)
py = (np.abs(fy)**2)*(1e-12)
freq = np.fft.fftfreq(fy.size, (1/(200*1e6))*(1e6))

plt.subplot(122)
plt.plot(freq, py)
plt.title('Power spectrum of 20MHz signal mixed with sine', fontsize = 18)
plt.xlabel('Frequency(MHz)',fontsize = 16)
plt.ylabel('Power(TW)',fontsize = 16)
plt.show()






