#ssh -xy radiolab@quasar
#go to group_3 stuff

import numpy as np
import pylab as plt

F = np.load('sun_04-02-2014_153105.npz')
F.files
data_sun= F['volts']
fft_sun = np.fft.fft(data_sun)
power_sun = np.abs(fft_sun)**2
x = fft_sun.size
freq = np.fft.fftfreq(x, 1)
plt.subplot(121)
plt.plot(data_sun)
plt.title('Sun data with time', fontsize = 18)
plt.xlabel('Time(s)', fontsize = 16)
plt.ylabel('Voltage(V)', fontsize = 16)

plt.subplot(122)
plt.plot(freq, psun)
plt.title('Power Spectrum of Sun', fontsize = 18)
plt.xlabel('Frequency(Hz)', fontsize = 16)
plt.ylabel('Power(W)', fontsize = 16)
plt.show()

F = np.load('moon_04-06-2014_033444.npz')
F.files
data_moon= F['volts']
fft_moon = np.fft.fft(data_moon)
power_moon = np.abs(fft_moon)**2
x = fft_moon.size
freq = np.fft.fftfreq(x, 1)

plt.plot(data_moon)
plt.title('Moon data with time', fontsize = 18)
plt.xlabel('Time(s)', fontsize = 16)
plt.ylabel('Voltage(V)', fontsize = 16)data_moon= F['volts']

plt.subplot(122)
plt.plot(freq, power_moon)
plt.title('Power Spectrum of Moon', fontsize = 18)
plt.xlabel('Frequency(Hz)', fontsize = 16)
plt.ylabel('Power(W)', fontsize = 16)
plt.show()

F = np.load('3C144_03-28-2014_001926.npz')
F.files
data_crab= F['volts']
plt.plot(data_crab)
plt.title('Crab Nebula data with time', fontsize = 18)
plt.xlabel('Time(s)', fontsize = 16)
plt.ylabel('Voltage(V)', fontsize = 16)
plt.show()

F = np.load('moon_04-06-2014_033444.npz')
F.files
data_orion= F['volts']
plt.plot(data_orion)
plt.title('Orion data with time', fontsize = 18)
plt.xlabel('Time(s)', fontsize = 16)
plt.ylabel('Voltage(V)', fontsize = 16)


#Least Square fitting Crab Nebula
F = np.load('3C144_03-28-2014_001926.npz')
y = F['volts']
ha = lst_crab - ra_crab
ha2 = (ha*24)/(2*np.pi)
#z = np.arange(7,12.1)
dB_guess = []
sq_results = []
bguess = np.linspace(7,12,100)
for b in bguess:
            x = np.zeros([2, 14378])
            x[0] = np.cos(2*np.pi*b/2.5* np.cos(22)*np.sin(ha2))
            x[1] = np.sin(2*np.pi*b/2.5* np.cos(22)*np.sin(ha2))
            xx = np.dot(x, np.transpose(x))
            xxi = np.linalg.inv(xx)
            xy = np.dot(x, np.transpose(y))
            coeffs = np.dot(xy, xxi)
            ybar = np.dot(coeffs, x)
            yerr = y - ybar
            dB_guess = np.append(dB_guess, b)
            s_sq = np.sum(yerr**2)/(14378-2)
            sq_results = np.append(sq_results, s_sq)


plt.plot(dB_guess, sq_results)
plt.title('Baseline guess errors of Crab Nebula', fontsize = 18)
plt.xlabel('Baseline guess(m)', fontsize = 16)
plt.ylabel('Error', fontsize = 16)
plt.show()

#Error for Sun 
F = np.load('sun_04-02-2014_153105.npz')
F.files
y = F['volts']
ha = lst- ra
dec = F['dec']
phiguess = np.linspace(0,np.pi,100)
phi_guess = []
ssq_results = []
for p in phiguess:
            F = np.cos(400*np.cos(dec)*np.cos(ha2+p))
            x = np.zeros([3, 39503])
            x[0] = F
            x[1] = ha2*F
            x[2] = (ha2**2)*F
            xx = np.dot(x, np.transpose(x))
            xxi = np.linalg.inv(xx)
            xy = np.dot(x, np.transpose(y))
            coeffs = np.dot(xy, xxi)
            ybar = np.dot(coeffs, x)
            yerr = y - ybar
            phi_guess = np.append(phi_guess, p)
            s_sq = np.sum(yerr**2)/(39503-3)
            ssq_results = np.append(ssq_results, s_sq)

plt.plot(phi_guess,ssq_results)
plt.title('Phase shift guess errors of Sun', fontsize = 18)
plt.xlabel('Phase guess(rad)', fontsize = 16)
plt.ylabel('Error', fontsize = 16)
plt.show()

F = np.cos(400*np.cos(dec)*np.cos(ha2+.2))
x = np.zeros([3, 39503])
x[0] = F
x[1] = ha2*F
x[2] = (ha2**2)*F

P = np.load('sun_04-02-2014_153105.npz')
P.files
y = F['volts']
ymin = min(y)
N = 1000
n = np.linspace(-1000, 1000, 2000)
f = (1-(x/N)**2)**(0.5)*np.cos((2*np.pi*ff*R*x)/N)
rguess = np.linspace(0.2,0.5,100)
for l in rguess:
    def riemann((1-(x/N)**2)**(0.5)*np.cos((2*np.pi*ff*R*x)/N),-1000,1000,iterations=50):
        delta = (-1000-1000)/50
        area = 0.0
        for i in range(interations):
            x = -1000+i*delta
            boxarea = delta*f
            area 
    MF = (cdec*ccha)*summ*np.cos(-0.176x)


#Error for Moon
F = np.load('moon_04-06-2014_033444.npz')
F.files
y = F['volts']
hs = lst-ra
hs2 = (24*hs)/(2*np.pi)
phiguess = np.linspace(0,np.pi,100)
phi_guess = []
ssq_results = []
for p in phiguess:
            F = np.cos(400*np.cos(dec)*np.cos(ha2+p))
            x = np.zeros([3, 14365])
            x[0] = F
            x[1] = ha2*F
            x[2] = (ha2**2)*F
            xx = np.dot(x, np.transpose(x))
            xxi = np.linalg.inv(xx)
            xy = np.dot(x, np.transpose(y))
            coeffs = np.dot(xy, xxi)
            ybar = np.dot(coeffs, x)
            yerr = y - ybar
            phi_guess = np.append(phi_guess, p)
            s_sq = np.sum(yerr**2)/(39503-3)
            ssq_results = np.append(ssq_results, s_sq)

plt.plot(phi_guess,ssq_results)
plt.title('Phase shift guess errors of Moon', fontsize = 18)
plt.xlabel('Phase guess(rad)', fontsize = 16)
plt.ylabel('Error', fontsize = 16)
plt.show()
