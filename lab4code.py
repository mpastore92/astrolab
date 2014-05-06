import numpy as np
import pylab as plt

F = np.load('May_4_final_final.npz')
F.files
freq = F['Freq']
temp = F['Temp']
plt.plot(freq,temp)
plt.title('Data Spectrum', fontsize = 18)
plt.xlabel('Frequency(MHz)', fontsize = 16)
plt.ylabel('Temperature(K)', fontsize = 16)
plt.show()
vel = ((1420.-freq)*3e5)/(1420.)
plt.plot(vel,temp)
plt.title('Velocity Spectrum', fontsize = 18)
plt.xlabel('Doppler Velocity(km/s)', fontsize = 16)
plt.ylabel('Temperature(K)', fontsize = 16)
plt.show()

l = F['l']
b = F['b']

R = np.zeros([3,3])
R[0] = [-0.054876, -0.873437, -0.483835]
R[1] = [0.494109, -0.444830, 0.746982]
R[2] = [-0.867666, -0.198076, 0.455984]
trans_R = np.transpose(R)

x = np.zeros([3,480])
x[0] = np.cos(b)*np.cos(l)
x[1] = np.cos(b)*np.sin(l)
x[2] = np.sin(b)
A = np.dot(trans_R, x) 

ra = np.arctan2(C[1], C[0])
dec = np.arcsin(C[2])
#get julian day
v_lsr = ugdoppler.ugdoppler(ra, dec, j_day)
v_tot = vel-v_lsr
alpha = np.arcsin((v_tot/200)+np.sin(75*(np.pi/180)))+75*(np.pi/180)
d_1 = 8*np.sin(90-l)
d_2 = 8*np.tan(90-alpha+l)
D = d_1+d_2
height = 8*np.tan(b)
plt.plot(D,temp)
plt.title('Distance and Temperature Relation', fontsize = 18)
plt.xlabel('Distance(kpc)', fontsize = 16)
plt.ylabel('Temperature(K)', fontsize = 16)
plt.show()

plt.title('Corrected Velocity Spectrum', fontsize = 18)
plt.xlabel('Corrected Velocity(km/s)', fontsize = 16)
plt.ylabel('Temperature(K)', fontsize = 16)
plt.show()

x = d
y = b
std_x = np.std(x)
std_y = np.std(y)
kernel = np.exp(-((x**2)+(y**2))/(2*sigma**2))
image = [[d],[b],[t]] #d is the distance, b is the latitude, and T is the temperature
image_1 = np.convolve(image,kernel)
h = []
d_l = []
d_f = []
for i in range (len(b)):
h.append(d[i]*np.tan(b[i]*np.pi/180)

for k in range(0, 35): 
    d_l.append(d[k])
    d_f = np.average(d_l)


        if math.isnan(d_f)==True:
           d[l] = 0
        elif abs(d_f) > 30:
            d[l] = 0
        else:
            pass
        

pylab.imshow(x)
pylab.colorbar()
pylab.title('Image of the Milky Way galaxy', fontsize = 18)
pylab.xlabel('Distance(kpc)', fontsize = 16)
pylab.ylabel('Height(kpc)', fontsize = 16)
pylab.show()

plt.ylim([-30,30])
plt.xlim([0, 50])
plt.title('Pointings for the Milky Way galaxy', fontsize = 18)
plt.ylabel('Height(kpc)', fontsize = 16)
plt.xlabel('Distance(kpc)', fontsize = 16)
plt.show()
