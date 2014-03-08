import DFEC
import pylab as plt
import numpy as np
sample = 100000.
N=256

x=np.arange(((10**6)*(1/sample)),((10**6)*((N+1)/sample)),((10**6)*(1/sample)))


#DFEC.set_srs(1,.2*sample,2)
y=DFEC.sampler(N,sample)

plt.subplot(121)
plt.plot(x,y)
plt.title(r'$\nu_{sig} =.9\nu_{sampl} (\nu_{sampl}=100kHz)$', fontsize=18)
plt.xlabel('Time($\mu$s)',fontsize = 16)
plt.ylabel("Voltage(V)", fontsize = 16)


fy=np.fft.fft(y)
py=np.abs(fy)**2
freq=np.fft.fftfreq(fy.size,(10**(3))*(1/sample))
plt.subplot(122)
plt.plot(freq,py)
plt.title('Fourier Transform', fontsize = 18)
plt.xlabel('Frequency(kHz)', fontsize = 16)
plt.ylabel('Power(W)', fontsize = 16)



plt.show()




