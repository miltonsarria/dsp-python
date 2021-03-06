#Milton Orlando Sarria Paja
#USC
#Procesamiento digital de senales
#graficar audio en tiempo real
#plot audio data in real time

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import sounddevice as sd
import sys
from wav_rw import wavwrite
import time
#################################################################
try:
    import Queue as queue
except ImportError:
    import queue

#################################################################
def audio_callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print status, sys.stderr
    # Fancy indexing with mapping creates a (necessary!) copy:
    q.put(indata[::downsample, mapping])

#################################################################
'''
def update_plot(frame):
    """This function is called by matplotlib for each plot update. 
    Typically, audio callbacks happen more frequently than plot updates,
    therefore the queue tends to contain multiple blocks of audio data.
    """
    global plotdata, vector
       
    while True:
        try:
            data = q.get_nowait()
        except queue.Empty:
            break
        shift = len(data)
        plotdata = np.roll(plotdata, -shift, axis=0)
        plotdata[-shift:, :] = data
    #plotdata tiene un formato especifico que permite tener varios canales
    #solo se tomara un canal para vizualizar
    line1.set_data(t,plotdata[:, 0])
    
    
    vector=np.append(vector,data[:,0],axis=0)
    #print vector.shape
    if len(vector)>16000:
     wavwrite(vector,16000,'prueba.wav')
    
    
    return [line1]
'''    
def update_data():
  while True:
    global vector
       
    while True:
        try:
            data = q.get_nowait()
        except queue.Empty:
            break
    
    try:
     vector=np.append(vector,data[:,0],axis=0)
    except:
     pass
    #print vector.shape
    if vector.size>3*16000:
     wavwrite(vector,16000,'prueba.wav')
     break
    sd.sleep(100)
  return
    
#################################################################    
#################################################################
#to save data from stream in a separate thread
q = queue.Queue()
vector=np.zeros(5)
#define important parameters
window     = 500    #miliseconds  longitud ventana a mostrar en grafica
samplerate = 16000  #khz
downsample = 1      #para bajar la frecuencia de muestreo en un factor
channels   = [1]    #numero de canales
device     = 11      #dispositivo a utilizar
interval   = 100    #update plot every 'interval' ms

#Definir e inicializar variables para graficar
length     = int(window * samplerate / (1000 * downsample))
plotdata = np.zeros((length, len(channels)))
t=np.arange(0,length)/float(samplerate)  

#Definir e inicializar la figura y los ejes donde se va a graficar
'''
fig = plt.figure()

line1 = Line2D([], [], color='black')
ax1  = fig.add_subplot(1,1,1)

ax1.set_ylim(-1.2, 1.2)
ax1.set_xlim(0, window/1000.)

ax1.add_line(line1)
'''
#Mapeo para separar los canales
mapping = [c - 1 for c in channels] 

#Inicializar el canal de entrada de datos usando stream y los parametros definidos
stream = sd.InputStream(
        device=device, channels=max(channels),
        samplerate=samplerate, callback=audio_callback)

#iniciar la animacion
#ani1 = FuncAnimation(fig, update_plot, interval=interval,blit=True)

#iniciar el proceso
with stream:
    #plt.show()
    update_data() 


    








