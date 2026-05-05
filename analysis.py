import numpy as np
import pylab as plt

def hello():
  print("hello")

def loadcsv(ifile):
  return pd.read_csv(ifile,header=None,sep=";").replace(",",".",regex=True).to_numpy().astype("float")

def pintar_imagen(filename,vmin=None,vmax=None,colormap="coolwarm"):
  plt.imshow(loadcsv(filename),cmap=colormap,vmin=vmin,vmax=vmax)
    
