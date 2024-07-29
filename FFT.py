import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft,fftfreq

t=np.linspace(0,1,200,endpoint=False)
print(f"{t}")

signal=np.sin(2*np.pi*100*t)
signal_fft=fft(signal)
freqs=fftfreq(len(signal),1/200)
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(t,signal)
plt.grid(True)

plt.subplot(1,2,2)
plt.plot(freqs,np.abs(signal_fft))
plt.grid(True)
plt.show()
