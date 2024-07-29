import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,1,1/1500/2)
seno=np.sin(t*2*np.pi*1000)
funcion=np.fft.fft(seno)
frecuencias=np.fft.fftfreq(len(funcion),1/1500/2)
plt.figure()
plt.plot(frecuencias,np.abs(funcion))
plt.show()
