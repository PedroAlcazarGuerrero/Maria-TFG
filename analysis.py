import numpy as np
import pylab as plt

def hello():
  print("hello")

def pintar_imagen(filename,vmin=None,vmax=None,colormap="coolwarm"):
  plt.imshow(loadcsv(filename),cmap=colormap,vmin=vmin,vmax=vmax)
    
