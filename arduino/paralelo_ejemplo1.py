#Milton Orlando Sarria
#USC - Cali
#este ejemplo permite ilustrar como dos procesos se pueden sincronizar en 
#paralelo para ejecutar dos tareas diferentes pero que comparten informacion

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


#############################################################
#############################################################
#clase que permite generar un objeto que lee desde un archivo 
#para simular la lectura desde el puerto serial
#############################################################
#############################################################
class reader(threading.Thread):
      def __init__(self,datafile,tRead=100):
         threading.Thread.__init__(self) 
         self.datafile  = datafile
         self.rawdata   = '0\t0\n'
         self.tRead     = tRead/1e3
         self.read      = False
         self.stop      = False
         self.num_data  = np.array([])
         self.dataCount = 0
      def run(self):
         #read all lines and close file
         fh=open(self.datafile,'r')
         lines  = fh.readlines()
         fh.close()
         for line in lines:
            while not(self.read):
               pass

            self.rawdata=line
            self.num_data=np.append(self.num_data,float(self.rawdata[:-1].split('\t')[1]))
            self.dataCount+=1
            time.sleep(self.tRead)         
            if self.stop:
               break
         return
      
      def kill(self):
          self.read=False
          return

#este codigo corre en consola o tambien en IPython
#definir una funcion para actualizar la grafica
def update(i):
    buffersize = 500
    y_b   = np.array([])
    x_b   = np.array([])
    if readObj.dataCount>0:    
       y_data=readObj.num_data
       x_data=np.linspace(0,readObj.dataCount*readObj.tRead,y_data.size)
       if y_data.size<buffersize:
          y_b=y_data
          x_b=x_data
       else:
          y_b=y_data[y_data.size-buffersize:]
          x_b=x_data[x_data.size-buffersize:]
   
    ax.clear()
    ax.plot(x_b,y_b) 
    
#######################################################################
#### evaluar el codigo con un lector de texto
#######################################################################    
#definir variables
readObj= reader('data.txt')
readObj.read=True

#iniciar la figura donde se van a vizualizar los datos
fig = plt.figure()
ax  = fig.add_subplot(1,1,1)
ax.set_autoscaley_on(True)
ax.set_ylim(-1, 1)

#iniciar la lectura de datos (realmente los datos se actualizan cada x cantidad de tiempo)
readObj.start() #iniciar hilo para lectura de datos
ani = FuncAnimation(fig, update, interval=500)#, blit=True)
plt.show()

readObj.stop=True

