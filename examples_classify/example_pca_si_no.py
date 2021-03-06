import numpy as np
import matplotlib.pyplot as plt
import h5py
from sklearn.linear_model import LogisticRegression
lista='lista_feats_si_no.txt'
hf = open(lista,'r')
lines=hf.readlines()
#load all feats
Y=[]
X=[]
for line in lines:
    hf = h5py.File(line[:-1], "r")
    feats = (hf.get('fbank')).value
    X.append(np.mean(feats,axis=0))
    lab=(hf.get('label')).value
    Y.append(lab)
    hf.close()
    
X=np.array(X)      
Y=np.array(Y)



#calcular media
meanX=X.mean(axis=0)
X=X-meanX
#calcular matriz de covarianzas
Sigma=np.cov(X.transpose())

u, s, vh = np.linalg.svd(Sigma, full_matrices=True)
Xp=np.dot(X,u)
plt.figure(1)
plt.plot(Xp[Y==0,0],Xp[Y==0,1],'ob')
plt.plot(Xp[Y==1,0],Xp[Y==1,1],'or')
plt.show()



