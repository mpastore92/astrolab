import ephem
obs = ephem.Observer()
lat = print obs.lat #our latitude
long = print obs.long #our longitude
lst = print obs.disereal_time()

#obs.lat = 37.8732*3.141/180  	to convert to radians
#obs.long = -122.2573*3.141/180

sun = ephem.Sun()
sun.compute(obs)
sra = print sun.ra, float(sun.ra)
sdec = print sun.dec, float(sun.dec)

#Start rotation matix
ha = lst - sra
topRow = [np.cos(lst), np.sin(lst), 0]
midRow = [np.sin(lst), -np.cos(lst), 0]
botRow = [0, 0, 1]
Rot = [topRow, midRow, botRow]
print(Rot)

#Final rotation matrix
topRow2 = [-np.sin(lat), 0, cos(lat)]
midRow2 = [0, -1, 0]
botRow2 = [cos(lat), 0, sin(lat)]
Rot2 = [topRow2, midRow2, botRow2]
print Rot2

#make the x matrix
x = np.array([0., 0, 0])
x[0] = np.cos(sdec) * np.cos(sra)
x[1] = np.cos(sdec) * np.sin(sra)
x[2] = np.sin(sdec)

#apply rotation matrix Rot2
xp = np.dot(Rot2, x)
